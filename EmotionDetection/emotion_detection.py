import requests
import json

def emotion_detector(text_to_analyze):
    """Detect emotions in text using Watson NLP API via HTTP POST request."""
    # The URL of the Watson Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Required headers specifying the model ID
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send POST request to the Watson NLP API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Check if the status code is 200 (Success)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        
        # Extract the emotions dictionary
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # Extract individual emotion scores
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        # Determine the dominant emotion (key with the highest score)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Format the output dictionary
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    # Check if the status code is 400 (Bad Request / Empty input)
    elif response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Fallback for any other status code
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        
    return result