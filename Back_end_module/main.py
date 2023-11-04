from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import scraper

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
    return job_data