# import pytest # no need to uncomment it while using cli tool
from app.main import app
from fastapi.testclient import TestClient 

client = TestClient(app)

def test_analyze_text0():
    msg = ""
    res = client.post('/analyze', json={"text": msg})
    assert res.status_code == 422

def test_analyze_text1():
    msg = "Spekter seems an awesome name!"
    res = client.post('/analyze', json={"text": msg})
    res = res.json()
    assert res['sentiment'] == "positive"

def test_analyze_text2():
    msg = "Hope I will get the job there."
    res = client.post('/analyze', json={"text": msg})
    res = res.json()
    assert res['sentiment'] == "positive"

def test_analyze_text3():
    msg = "Where is the company based in?"
    res = client.post('/analyze', json={"text": msg})
    res = res.json()
    assert res['sentiment'] == "neutral"

def test_analyze_text4():
    msg = "Let's have a chat!"
    res = client.post('/analyze', json={"text": msg})
    res = res.json()
    assert res['sentiment'] == "positive"

def test_analyze_text5():
    msg = "Some candidates will be rejected."
    res = client.post('/analyze', json={"text": msg})
    res = res.json()
    assert res['sentiment'] == "negative"

def test_analyze_text6():
    msg = "Hope I am none of them."
    res = client.post('/analyze', json={"text": msg})
    res = res.json()
    assert res['sentiment'] == "negative"
