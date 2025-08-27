import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        # Return None values if input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=input_json)
    if response.status_code == 400:
        # Return None values if API returns 400
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    response_dict = response.json()
    emotions = response_dict['emotionPredictions'][0]['emotion']
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
    }
    output['dominant_emotion'] = max(output, key=output.get)
    return output