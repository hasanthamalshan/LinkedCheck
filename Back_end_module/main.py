from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random


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

@app.get('/check/{link}')
async def root(link : str):
    return {'title' : 'testing the endpoint' , 'data' : link}