from app.main import app
from fastapi.testclient import TestClient 

client = TestClient(app)

def test_index():
    res = client.get('/')
    assert res.status_code == 200

def test_demo():
    res = client.get('/demo')
    assert res.status_code == 200

def test_analyze():
    res = client.post('/analyze', json={'text': "no it should not work"})
    assert res.status_code == 200
    res = res.json()
    assert res['sentiment'] == 'negative'