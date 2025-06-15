"""Flask server to deploy the emotion detection app."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """Process user input and return emotion analysis."""
    text_to_analyze = request.values.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        response = "Invalid text! Please try again!"
    else:
        response = (f"For the given statement, the system response is "
                    f"'anger': {result['anger']}, "
                    f"'disgust': {result['disgust']}, "
                    f"'fear': {result['fear']}, "
                    f"'joy': {result['joy']} and "
                    f"'sadness': {result['sadness']}. "
                    f"The dominant emotion is {result['dominant_emotion']}.")

    return render_template('index.html', response=response)

@app.route("/")
def index():
    """Render the main page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
