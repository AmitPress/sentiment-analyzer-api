from setfit import SetFitModel
from .models import AnalyzeRequest
model = SetFitModel.from_pretrained("AmitPress/bestsenti")



# result = ['negative', 'neutral', 'positive']
# for pred in preds:
#     print(result[pred])

from fastapi import FastAPI, Request
import json
app = FastAPI()

@app.get('/')
def index():
    """
    Application Home
    """
    response = {
        "message": "Welcome to the sentiment inference engine powered by SetFit constructed by Amit Malaker"
    }
    return response

@app.get('/demo')
def demo():
    """
    A Demo endpoint that demonstrates the remote inference model for the hardcoded values
    """
    text1 = "i somewhat love the spiderman movie!"
    text2 = "pineapple on pizza is the worst 🤮"
    text3 = "The sky appears clear and the temperature is moderate."
    text4 = "Who is there?"
    texts = []
    texts.append(text1)
    texts.append(text2)
    texts.append(text3)
    texts.append(text4)
    response = {}
    preds = model(texts)
    result = ['negative', 'neutral', 'positive']
    for text, pred in zip(texts, preds):
        response[f"{text}"] = result[pred]
    
    return response

@app.post('/analyze')
def analyze(req: AnalyzeRequest):
    """Endpoint to analyze text sentiment
    Args:
        req (AnalyzeRequest): This argument itself is the request from the client
    Returns:
        json (Json): This return value is of json type and it holds the sentiment field which tells us about the sentiment of the given text
    """
    response = {}
    predictions = model([req.text])
    prediction = predictions[0]
    result = ['negative', 'neutral', 'positive']
    return {"sentiment": result[prediction]}