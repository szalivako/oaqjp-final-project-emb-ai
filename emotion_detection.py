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

    # Return the text attribute from the response JSON
    return response.json()