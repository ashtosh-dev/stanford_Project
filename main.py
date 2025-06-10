from topics import TOPIC_URLS
from scraper import scrape_headlines
from quiz import build_questions, ask_question

def play_game():
    print("\n===== QUIZ GAME =====")
    for key, (name, _) in TOPIC_URLS.items():
        print(f"{key}. {name}")

    choice = input("\nChoose a topic (1-4 or 'q' to quit): ").strip().lower()
    if choice in ['q', 'quit', 'exit']:
        print("Exiting game. Goodbye!")
        return

    if choice not in TOPIC_URLS:
        print("Invalid choice. Exiting.")
        return

    topic_name, url = TOPIC_URLS[choice]
    print(f"\nFetching headlines for: {topic_name}...\n")
    headlines = scrape_headlines(url)

    if not headlines:
        print("Sorry, no data available. Try again later.")
        return

    print("Type 'q' or 'quit' anytime to exit.\n")

    score = 0
    total = 0
    used_headlines = set()

    while True:
        qdata = build_questions(headlines, used_headlines)
        if qdata is None:
            print("No more questions available. Ending game.")
            break

        question, options, correct = qdata
        result = ask_question(total + 1, question, options, correct)

        if result is None:
            break
        elif result:
            score += 1

        total += 1

    print(f"\nGame Over! You scored {score}/{total}\nThanks for playing!\n")

if __name__ == "__main__":
    play_game()
