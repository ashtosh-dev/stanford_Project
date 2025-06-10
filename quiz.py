import random

def build_questions(headlines, used_headlines):
    valid_headlines = [h for h in headlines if h not in used_headlines and len(h.split()) > 4]
    if not valid_headlines:
        return None

    correct = random.choice(valid_headlines)
    used_headlines.add(correct)

    wrong_choices = random.sample([h for h in headlines if h != correct], 3)
    options = [correct] + wrong_choices
    random.shuffle(options)

    return (f"Which of the following was in the news?", options, correct)

def ask_question(question_num, question, options, correct):
    print(f"\nQ{question_num}: {question}\n")
    for i, opt in enumerate(options):
        print(f"  {chr(65+i)}. {opt}")

    ans = input("\nYour answer (A/B/C/D or Q to quit): ").strip().lower()
    if ans in ['q', 'quit']:
        return None

    ans_idx = ord(ans.upper()) - 65
    if 0 <= ans_idx < 4 and options[ans_idx] == correct:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect. Correct answer was: {correct}\n")
        return False
