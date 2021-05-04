import datetime

RSS = {
    'news':{
        'title': 'Top News',
        'feeds': [
            ('CNBC', 'https://www.cnbc.com/id/100003114/device/rss/rss.html'),
            ('BBC', 'http://feeds.bbci.co.uk/news/rss.xml'),
            ('WSJ', 'https://feeds.a.dj.com/rss/RSSWorldNews.xml'),
            ('ProPublica', 'http://feeds.propublica.org/propublica/main'),
            ('New York Times', 'https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/world/rss.xml'),
            ('Al Jazeera', 'https://www.aljazeera.com/xml/rss/all.xml'),
            ('CNN', 'http://rss.cnn.com/rss/edition_world.rss'),
            ('The Guardian', 'https://www.theguardian.com/world/rss'),
            ('Washington Post', 'http://feeds.washingtonpost.com/rss/world'),
            ('Vox', 'https://www.vox.com/rss/world/index.xml'),
            ('SCMP', 'https://www.scmp.com/rss/91/feed'),
        ]
    },
    'business': {
        'title': 'Business',
        'feeds': [
            ('Business Insider', 'https://markets.businessinsider.com/rss/news'),
            ('CNBC', 'https://www.cnbc.com/id/10001147/device/rss/rss.html'),
            ('BBC', 'http://feeds.bbci.co.uk/news/business/rss.xml'),
            ('WSJ', 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml'),
        ]
    },
    'tech': {
        'title': 'Tech',
        'feeds': [
            ('WIRED', 'https://www.wired.com/feed/rss'),
            ('Mashable', 'http://feeds.mashable.com/Mashable'),
            ('Y Combinator', 'https://news.ycombinator.com/rss'),
            ('CNBC', 'https://www.cnbc.com/id/19854910/device/rss/rss.html'),
            ('BBC', 'http://feeds.bbci.co.uk/news/technology/rss.xml'),
            ('WSJ', 'https://feeds.a.dj.com/rss/RSSWSJD.xml'),
            ('TechCrunch', 'http://feeds.feedburner.com/TechCrunch/'),
            ('New York Times', 'https://www.nytimes.com/svc/collections/v1/publish/https://www.nytimes.com/section/technology/rss.xml'),
        ]
    },
}

# KST Seoul UTC+9

TIMEZONE = datetime.timezone(datetime.timedelta(hours=9)) 

twitter_config = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_secret': '',
}

