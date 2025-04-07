import fastf1
import pandas as pd
from datetime import datetime
import pytz
import asyncio
from schemas import RaceSchedule

fastf1.Cache.enable_cache("./cache")

def get_session(year, event, session):
    """Gets event information from fastf1 for chosen year, event and session."""
    session = fastf1.get_session(year, event, session, backend="fastf1")
    session.load()
    return session


async def get_race_schedule():
    current_year = datetime.now().year

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
