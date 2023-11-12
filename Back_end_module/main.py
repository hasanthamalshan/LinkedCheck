from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import scraper # custom module for scraping the data 
import inputProcessor
import predictor


app = FastAPI()

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {'result' : 'API is running...'}

@app.get('/check/{link}')
async def getResults(link : str):
    job_data = scraper.scrape(link)
    new_record = inputProcessor.processInput(job_data)

    # new_record = {
    #     'title': job_data["job_title"],
    #     'employment_type': job_data["employment_type"],
    #     'required_experience': job_data["seniority_level"],
    #     'text_length': len(job_data["job_description"])
    # }

    new_predictions =predictor.predict(new_record)

    print(new_predictions)

    return {'prediction' : new_predictions , 'title' : job_data["job_title"]}