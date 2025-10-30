from scraper import scrape_headlines
from topics import TOPIC_URLS

try:
    # Test with the "Sports" URL
    url = TOPIC_URLS["1"][1]
    print(f"Scraping {url}...")
    headlines = scrape_headlines(url)
    print("Headlines found:")
    for h in headlines:
        print(f"- {h}")
except Exception as e:
    print(f"An error occurred: {e}")
