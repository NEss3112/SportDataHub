from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import RaceSchedule
from service import get_race_schedule
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
async def get_next_race():
    races = await get_race_schedule()
    now = datetime.now(pytz.UTC)

    future_races = [race for race in races if race.date > now]

    if not future_races:
        return races[-1]

    return future_races[0]


@app.get("/")
async def home():
    return {"message":"Welcome to SportDataHub v.0.1"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
