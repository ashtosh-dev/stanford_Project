# CLI Quiz Game 🧠🎮

A fun command-line quiz game that fetches real-time headlines from popular websites and turns them into trivia questions! Choose your topic, test your knowledge, and see how many you can get right.

## Topics Available

- 🏈 Sports — [ESPN](https://www.espn.com)
- 🌐 Current Affairs — [BBC News](https://www.bbc.com/news)
- 💻 Tech — [TechCrunch](https://techcrunch.com)
- 🎬 Movies — [IMDb Top Movies](https://www.imdb.com/chart/top/)

## Features

- Real-time web scraping for current headlines
- Multiple choice questions generated from scraped content
- Random decoy options to make it more challenging
- Play until you type `q` or `quit` to exit
- Keeps track of your final score

# Requirements
requests==2.32.3
beautifulsoup4==4.13.4

# Install dependencies :
pip install -r requirements.txt

# How to Play
python main.py
Then choose a topic (1–4) or type q to quit.
