"""
This is the file to run the server
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    This is the call to the EmotionDetector model. It handles any blanks, as 
    well as returns all emotions as a message, highlighting the dominant one
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    emotions = list(response.items())[:5]
    emotions_text = ", ".join(f"'{k}': {v}"
        for k, v in emotions[:-1]) + f", and '{emotions[-1][0]}': {emotions[-1][1]}"
    sentence = (
        f"For the given statement, the system response is {emotions_text}." + \
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return sentence

@app.route("/")
def render_index_page():
    """ To render index page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
