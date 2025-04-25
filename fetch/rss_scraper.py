import feedparser
from pathlib import Path
import re
from newspaper import Article

rss_feeds = [
    "https://rss.cnn.com/rss/edition.rss",
    "http://feeds.bbci.co.uk/news/rss.xml"
]

output_dir = Path("articles")
output_dir.mkdir(exist_ok=True)

def clean_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)

for feed_url in rss_feeds:
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        title = entry.get("title", "untitled")
        link = entry.get("link", None)
        published = entry.get("published", "No date")

        if not link:
            continue

        # Use newspaper3k to fetch and parse the full article
        try:
            article = Article(link)
            article.download()
            article.parse()
            full_text = article.text.strip()
        except Exception as e:
            print(f"❌ Failed to extract article: {link}\nReason: {e}")
            continue

        safe_title = clean_filename(title)
        file_path = output_dir / f"{safe_title}.txt"

        text = f"{title}\n\nPublished: {published}\nLink: {link}\n\n{full_text}"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

print("✅ Full articles saved as .txt files in the 'articles/' folder.")