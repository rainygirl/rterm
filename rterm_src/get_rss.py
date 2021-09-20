import feedparser
import json
import time
import datetime
import sys

from .common import p
from .config import RSS, TIMEZONE


def do(target_category=None, log=False) :

    def getRSS(category, urls, log=False) :

        rslt = {}

        for source,url in urls :
            try:
                if log :
                    sys.stdout.write('- %s' % url)

                d = feedparser.parse(url)

                if log :
                    sys.stdout.write(' - Done\n')

            except:
                sys.exit(' - Failed\n' if log else 0)

            for feed in d.entries :

                try:
                    at = datetime.datetime(*feed.published_parsed[:6]).replace(tzinfo=datetime.timezone.utc).astimezone(TIMEZONE)
                except:
                    continue

                pubDate = at.strftime('%H:%M' if at.date() == datetime.date.today() else '%b %d, %H:%M')

                ts = int(time.mktime(feed.published_parsed))

                entries={
                    'id': ts,
                    'sourceName': source,
                    'pubDate': pubDate,
                    'timestamp': ts,
                    'url': feed.link,
                    'title': feed.title,
                }

                rslt[entries['id']] = entries

        rslt = [val for key,val in sorted(rslt.items(), reverse=True)]

        rslt = {
            'entries': rslt,
            'created_at': int(time.time())
        }

        with open(p['path_data']+'rss_%s.json' % category, 'w', encoding='utf-8') as f: 
            f.write(json.dumps(rslt, ensure_ascii=False))

        return rslt

    if target_category :
        return getRSS(target_category, RSS[target_category]['feeds'], log)

    for category, d in RSS.items() :
        getRSS(category, d['feeds'], log)


if __name__ == '__main__':
    do()
 
