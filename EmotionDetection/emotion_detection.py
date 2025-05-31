"""
Emotion detection
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Run the Emotion Predict function of the Watson
    NLP Library.
    """

    # URL of the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network'
    url += '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Custom header specifying the model ID for the emotion predict service
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Constructing the request payload in the expected format
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Sending a POST request to the emotion predict API
        response = requests.post(url, json=myobj, headers=headers, timeout=300)

        if response.status_code == 500:
            print('Error response from Watson NLP API:')
            print(json.dumps(response.json(), indent=2))
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        # Parsing the JSON response from the API
        data = response.json()
        # Initialize the emotion data
        emotion_data = {}

        if 'emotionPredictions' in data:
            # Get the emotion data (or empty dict if not found in "data")
            emotion_data = data['emotionPredictions'][0].get('emotion', {})
            
        # Build the response
        result = {
            'anger': emotion_data.get('anger', 0),
            'disgust': emotion_data.get('disgust', 0),
            'fear': emotion_data.get('fear', 0),
            'joy': emotion_data.get('joy', 0),
            'sadness': emotion_data.get('sadness', 0)
        }
        # Determine the dominant emotion (the max of the emotions)
        result['dominant_emotion'] = max(result, key=result.get)

        # Return the result
        return result
    except requests.exceptions.RequestException as exc:
        print(f'Error while using Watson NLP API: {exc}')
        return {
            'message': 'API Error'
        }, 500
    except Exception as exc:
        print(f'Unexpected error: {exc}')
        return {
            'mesage': 'API Error'
        }, 500
