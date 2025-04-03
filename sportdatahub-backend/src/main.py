from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import RaceSchedule
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

async def get_race_schedule():
    current_year = datetime.utcnow().year

    loop = asyncio.get_running_loop()
    schedule = await loop.run_in_executor(None, fastf1.get_event_schedule, current_year)

    races = []
    for _, row in schedule.iterrows():
        race = RaceSchedule(
                round=row["RoundNumber"],
                name=row["EventName"],
                location=row["Location"],
                country=row["Country"],
                date=row["EventDate"].to_pydatetime().replace(tzinfo=pytz.UTC),
                time=row["Session5Date"].strftime("%H:%M") if not pd.isna(row["Session5Date"]) else "TBD"
                )
        races.append(race)

    return races


@app.get("/api/schedule", response_model=list[RaceSchedule])
async def get_schedule():
    return await get_race_schedule()


@app.get("/api/schedule/next", response_model=RaceSchedule)
async def get_next_race():
    races = await get_race_schedule()
    now = datetime.utcnow().replace(tzinfo=pytz.UTC)

    future_races = [race for race in races if race.date > now]

    if not future_races:
        return races[-1]

    return future_races[0]


@app.get("/")
async def home():
    return {"message":"Welcome to SportDataHub v.0.1"}
