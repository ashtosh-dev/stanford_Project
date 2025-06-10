import requests
from bs4 import BeautifulSoup
from topics import HEADERS

def scrape_headlines(topic_url):
    try:
        res = requests.get(topic_url, headers=HEADERS, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')

        # Special handling for IMDb Top 250
        if "imdb.com/chart/top" in topic_url:
            # Grabs movie titles from IMDb Top 250 chart
            headlines = [a.get_text(strip=True) for a in soup.select("td.titleColumn a")]
        else:
            # Default for other topics (h2/h3 with some content)
            headlines = [tag.get_text(strip=True)
                         for tag in soup.find_all(['h2', 'h3'])
                         if len(tag.get_text(strip=True)) > 25]

        return headlines[:10]

    except Exception as e:
        print(f"[Error] Could not fetch headlines: {e}")
        return []
