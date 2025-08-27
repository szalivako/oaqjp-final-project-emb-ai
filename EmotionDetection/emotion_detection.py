import requests
import json

def emotion_detector(text_to_analyze):
    # API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Required headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON payload
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Make the POST request
    response = requests.post(url, headers=headers, json=input_json)

    # Convert response to JSON
    response_dict = response.json()

    # Extract emotions
    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Build dictionary
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
    }

    # Find dominant emotion
    dominant_emotion = max(output, key=output.get)
    output['dominant_emotion'] = dominant_emotion

    return output