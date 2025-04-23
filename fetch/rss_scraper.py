# fetch/rss_scraper.py

import feedparser
import json
from datetime import datetime

# Add your preferred RSS feed URLs here
RSS_FEEDS = [
    "https://www.aljazeera.com/xml/rss/all.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
]

def fetch_articles():
    articles = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            article = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published if "published" in entry else str(datetime.now())
            }
            articles.append(article)

    # Save the articles to a file
    with open("article_list.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)

    print(f"Fetched {len(articles)} articles.")
    return articles

if __name__ == "__main__":
    fetch_articles()