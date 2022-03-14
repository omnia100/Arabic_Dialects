# Set-ExecutionPolicy RemoteSigned
import joblib as joblib
from fastapi import FastAPI
import uvicorn
from preprocessing_fuctions import preprocess

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/tweet/")
async def dialect(tweet: str):
    tweet_proc = preprocess(tweet)
    tweet_tfidf = tfidf.transform([tweet_proc])
    tweet_clf = clf.predict(tweet_tfidf)
    pred = names[tweet_clf[0]]
    return {f'{tweet}': f'{pred}'}

if __name__ == '__main__':
    tfidf = joblib.load('tfidf.pkl')
    clf = joblib.load('ML.pkl')
    names = {0: 'AE', 1: 'BH', 2: 'DZ', 3: 'EG', 4: 'IQ', 5: 'JO', 6: 'KW', 7: 'LB', 8: 'LY', 9: 'MA', 10: 'OM',
             11: 'PL', 12: 'QA', 13: 'SA', 14: 'SD', 15: 'SY', 16: 'TN', 17: 'YE'}
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

    #uvicorn main:app --reload
    #http://127.0.0.1:8000/docs
