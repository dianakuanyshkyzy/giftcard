from dotenv import load_dotenv
load_dotenv()
import os 
token = 'token' # token here
from giftcards.router import router as Giftcards_router
from database import database
import requests

# app = FastAPI()

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

# app.include_router(Giftcards_router, prefix="/giftcards", tags=["giftcards"])

from fastapi import FastAPI, HTTPException, Body
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import requests
from starlette.middleware.cors import CORSMiddleware

# FastAPI app instance
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PostgreSQL database configurations
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(Giftcards_router, prefix="/posts", tags=["giftcards"])

@app.post('/posts/gift_card')
def generate_ad(keywords:str):
    token = os.environ.get("TOKEN")
    headers = {
        'Authorization': "Bearer " + token
    }
    response = requests.post('Your_API', headers=headers, json={ #put your API here
        "input_text": f"generate a gift card in 100 words using these keywords: {keywords}"
    })
    body = response.json()
    return {
        "text": body['output']
    }

