from flask import Flask, request, render_template, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    # Loads the provided index.html from templates/
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    if request.method == "GET":
        text_to_analyze = request.args.get("textToAnalyze", "")
    else:
        data = request.get_json()
        text_to_analyze = data.get("text", "")

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)