import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"Request failed with status code {response.status_code}: {response.text}"

    # Convertir el texto de la respuesta a diccionario
    result = json.loads(response.text)

    # Extraer puntuaciones de emociones
    emotions = result['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Calcular emoción dominante
    dominant_emotion = max(emotions, key=emotions.get)

    # Devolver en el formato solicitado
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
