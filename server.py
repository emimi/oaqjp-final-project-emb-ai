from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"
    else:
        emotions = list(response.items())[:5]
        emotions_text = ", ".join(f"'{k}': {v}" for k, v in emotions[:-1]) + f", and '{emotions[-1][0]}': {emotions[-1][1]}"
        return "For the given statement, the system response is {}. The dominant emotion is {}.".format(emotions_text, response['dominant_emotion'])

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)