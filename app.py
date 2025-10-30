from flask import Flask, jsonify, request, session
from flask_cors import CORS
from topics import TOPIC_URLS
import os

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = os.urandom(24)

@app.route("/api/topics", methods=["GET"])
def get_topics():
    topics = [{"id": key, "name": name} for key, (name, _) in TOPIC_URLS.items()]
    return jsonify(topics)

@app.route("/api/quiz", methods=["POST"])
def start_quiz():
    from scraper import scrape_headlines  # Lazy import
    data = request.get_json()
    topic_id = data.get("topic_id")

    if not topic_id or topic_id not in TOPIC_URLS:
        return jsonify({"error": "Invalid topic ID"}), 400

    _, url = TOPIC_URLS[topic_id]
    headlines = scrape_headlines(url)

    if not headlines:
        return jsonify({"error": "Could not fetch headlines"}), 500

    session['headlines'] = headlines
    session['used_headlines'] = []
    session['score'] = 0

    return jsonify({"message": "Quiz started"})


@app.route("/api/question", methods=["GET"])
def get_question():
    from quiz import build_questions  # Lazy import
    headlines = session.get('headlines')
    used_headlines = set(session.get('used_headlines', []))

    if not headlines:
        return jsonify({"error": "Quiz not started"}), 400

    qdata = build_questions(headlines, used_headlines)

    if qdata is None:
        return jsonify({"message": "No more questions", "score": session.get('score',0), "total": len(session.get('used_headlines',[])) })

    question, options, correct = qdata
    session['used_headlines'] = list(used_headlines | {correct})
    session['correct_answer'] = correct

    return jsonify({
        "question": question,
        "options": options,
    })

@app.route("/api/answer", methods=["POST"])
def submit_answer():
    data = request.get_json()
    answer = data.get("answer")
    correct_answer = session.get('correct_answer')

    if not answer or not correct_answer:
        return jsonify({"error": "Invalid request"}), 400

    is_correct = (answer == correct_answer)
    if is_correct:
        session['score'] = session.get('score', 0) + 1

    return jsonify({
        "is_correct": is_correct,
        "correct_answer": correct_answer,
        "score": session.get('score')
    })


if __name__ == "__main__":
    app.run(debug=True)
