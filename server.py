"""
Web application to use the emotion detector
"""

# Import the flash related packages
from flask import Flask, render_template, request

# Import the emotion detector wrapper function
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_prediction()
        function. The output returned shows the emotion scores and
        the dominant emotion.
    '''
    text_to_analyze = request.args['textToAnalyze']

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return { 'message': 'invalid iuput'}, 400

    print(f'Analying text: {text_to_analyze}')
    response = emotion_detector(text_to_analyze)

    if response['anger'] is None:
        return 'Unable to process provided text. Try again with different text.'

    return f"For the given statement, the system response is 'anger': {response['anger']}, " \
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, " \
    f"'joy': {response['joy']} and 'sadness': {response['sadness']}. " \
    f"The dominant emotion is <b>{response['dominant_emotion']}</b>."

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template('index.html')

if __name__ == "__main__":
    # """
    # This functions executes the flask app and deploys it on localhost:5000
    # """
    app.run(host='0.0.0.0', port=5000, debug=True)
