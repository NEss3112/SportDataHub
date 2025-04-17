from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import RaceSchedule
from service import *
import fastf1
import pandas as pd
from datetime import datetime
import pytz
import asyncio

app = FastAPI(title="SportDataHub API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/schedule", response_model=list[RaceSchedule])
async def get_schedule():
    return await get_race_schedule()


@app.get("/api/schedule/next", response_model=RaceSchedule)
async def get_next():
    return await get_next_race()


@app.get("/")
async def home():
    return {"message":"Welcome to SportDataHub v.0.1"}


@app.get("/api/session")
async def get_session(year: int, gp: int, session_type):
    return await get_session_data(year, gp, session_type)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
