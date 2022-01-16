# -*- coding:utf-8 -*-

import webbrowser
import tweepy
import json
import time
import datetime

import sys
import re
import os
import traceback

from .common import p
from .config import twitter_config, TIMEZONE


def do(page=2):
    flag = False
    consumer_key, consumer_secret = "", ""
    access_token, access_secet = "", ""

    oauth_config_filename = os.path.join(p["path_data"], "oauth_twitter")
    if os.path.exists(oauth_config_filename):
        with open(oauth_config_filename, "r") as f:
            d = f.read().split("\n")
            try:
                consumer_key = str(d[0].strip())
                consumer_secret = str(d[1].strip())
                access_token = str(d[2]).strip()
                access_secret = str(d[3]).strip()

                auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback="oob")
                auth.set_access_token(access_token, access_secret)
                flag = True
            except:
                pass

    if not flag:

        if twitter_config.get("consumer_key"):

            auth = tweepy.OAuthHandler(twitter_config["consumer_key"], twitter_config["consumer_secret"], callback="oob")
            consumer_key = twitter_config["consumer_key"]
            consumer_secret = twitter_config["consumer_secret"]

        elif consumer_key == "":

            url = "https://developer.twitter.com/en/apps"

            print("\nFirst, create your own Twitter app on the Twitter Developer Site and copy the consumer key.\nURL : %s\n" % url)
            webbrowser.open(url, new=2)

            time.sleep(2)

            consumer_key = input("Consumer Key : ").strip()
            consumer_secret = input("Consumer Secret : ").strip()
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback="oob")

        if twitter_config.get("access_token"):

            auth.set_access_token(twitter_config["access_token"], twitter_config["access_secret"])

        else:
            try:
                auth_url = auth.get_authorization_url()
            except:
                sys.exit("Invalid consumer key.")

            print("\nSign in to twitter in the web browser and copy the PIN...\nURL : %s\n" % auth_url)
            webbrowser.open(auth_url, new=2)

            time.sleep(2)

            pin = input("PIN : ").strip()

            try:
                auth.get_access_token(pin)
                auth.set_access_token(auth.access_token, auth.access_token_secret)
            except:
                sys.exit("Invalid PIN.")

            print("\nOK. You've granted access to Twitter.")

    if auth.access_token != access_token:
        with open(os.path.join(p["path_data"], "oauth_twitter"), "w") as f:
            f.write("%s\n%s\n%s\n%s" % (consumer_key, consumer_secret, auth.access_token, auth.access_token_secret))

    api = tweepy.API(auth)
    tweets = []

    for i in range(0, page):
        try:
            tweets += api.home_timeline(count=200, page=i, tweet_mode="extended")
        except tweepy.error.TweepError as e:
            d = json.loads(e.reason.replace("'", '"'))
            raise Exception(d[0]["message"])
        except:
            traceback.print_exc()
            return None

    if not tweets:
        return None

    rslt = []

    for tweet in tweets:
        at = tweet.created_at.replace(tzinfo=datetime.timezone.utc).astimezone(TIMEZONE)

        pubDate = at.strftime("%H:%M" if at.date() == datetime.date.today() else "%b %d, %H:%M")

        ts = time.mktime(at.timetuple())

        entries = {
            "id": tweet.id,
            "user_id": tweet.user.id,
            "nickname": tweet.user.name,
            "nicknameS": "@%s" % tweet.user.screen_name,
            "username": tweet.user.screen_name,
            "ts": ts,
            "pubDate": pubDate,
            "in_reply_to_user_id": tweet.in_reply_to_user_id,
            "in_reply_to_screen_name": tweet.in_reply_to_screen_name,
            "permalink": "https://twitter.com/%s/status/%s" % (tweet.user.screen_name, tweet.id),
        }

        if hasattr(tweet, "full_text"):
            entries["text"] = tweet.full_text
        else:
            entries["text"] = tweet.text

        if "extended_tweet" in tweet._json and tweet._json["extended_tweet"].get("full_text"):

            entries["text"] = tweet._json["extended_tweet"]["full_text"]

        if tweet.favorite_count:
            entries["like"] = tweet.favorite_count

        urls = tweet.entities.get("urls")

        if urls:
            entries["links"] = [d["expanded_url"] for d in urls]

        medias = tweet.entities.get("media")

        if medias:
            entries["medias"] = [d["media_url"] for d in medias]

        if hasattr(tweet, "retweeted_status"):
            rt = tweet.retweeted_status

            entries["rt"] = {
                "user_id": rt.user.id,
                "username": rt.user.screen_name,
                "nickname": rt.user.name,
                "count": tweet.retweet_count,
            }

            if "extended_tweet" in tweet._json["retweeted_status"] and tweet._json["retweeted_status"]["extended_tweet"].get("full_text"):
                entries["textS"] = tweet._json["retweeted_status"]["extended_tweet"]["full_text"]
            elif hasattr(rt, "full_text"):
                entries["textS"] = "RT @%s: %s" % (rt.user.screen_name, rt.full_text)
            elif tweet._json["retweeted_status"].get("text"):
                entries["textS"] = "RT @%s: %s" % (rt.user.screen_name, tweet._json["retweeted_status"]["text"])
            else:
                entries["textS"] = "RT @%s: %s" % (rt.user.screen_name, entries["text"])

            entries["nicknameS"] = "RT by %s" % entries["nickname"]
            entries["nickname"] = "RT %s" % entries["rt"]["nickname"]
            entries["RTheaderS"] = entries["textS"].split(":")[0]

            entries["text"] = re.sub("RT([^:]+):\s", "", entries["textS"]).strip()

        for key in ["text", "textS"]:
            if key not in entries:
                continue
            entries[key] = entries[key].replace("\n", " ").replace("\r", " ").replace("&lt;", "<").replace("&gt;", ">") + " "
            entries[key] = re.sub("https://([^\s]+)", "", entries[key]).strip()

            entries[key] += " 🖼️ " if "medias" in entries else "  "
            entries[key] = entries[key].strip()

        entries["isLink"] = "🔗" if "links" in entries else "  "

        rslt.append(entries)

    rslt = {"entries": rslt, "created_at": int(time.time())}

    twitter_feed_filename = os.path.join(p["path_data"], "twitter_home.json")

    with open(twitter_feed_filename, "w", encoding="UTF-8") as f:
        f.write(json.dumps(rslt, ensure_ascii=False))

    return rslt


if __name__ == "__main__":
    do()
