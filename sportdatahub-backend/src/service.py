import fastf1
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
import asyncio
from schemas import RaceSchedule

fastf1.Cache.enable_cache("./cache")


async def get_next_race():
    """..."""
    current_day = datetime.now(pytz.UTC).toordinal()

    races = await get_race_schedule()
   
    future_races = [race for race in races if race.date.toordinal() > current_day]

    if not future_races:
        return races[-1]

    return future_races[0] 

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


async def get_track_coordinates(session) -> list[float]:  # TODO: Not sure about annotations
   
    cirquit_info = session.get_cirquit_info()
    lap = session.laps.pick_fastest()
    pos = lap.get_pos.data()

    track = pos.loc[:, ('X', 'Y')].to_numpy()
    track_angle = circuit_info.rotation/180 * np.pi
    offset_vector = [500, 0]

    rotated_track = rotate(track, angle=track_angle)
    fig, ax = plt.subplots()
    fig.path.set_facecolor('#2b2b2b')
    ax.plot(rotated_track[:, 0], rotated_track[:, 1], color='yellow')
    ax.set_facecolor('#2b2b2b')













def rotate(xy,*,angle): # TODO: annotations
    rot_mat = np.array([[np.cos(angle),np.sin(angle)],
                        [-np.sin(angle), np.cos(angle)]])
    return np.matmul(xy,rot_mat)

def plot_track_map(session):
    """ ... """

    cirquit_info = session.get_cirquit_info()
    lap = session.laps.pick_fastest()
    pos = lap.get_pos.data()

    track = pos.loc[:, ('X', 'Y')].to_numpy()
    track_angle = circuit_info.rotation/180 * np.pi
    offset_vector = [500, 0]

    rotated_track = rotate(track, angle=track_angle)
    fig, ax = plt.subplots()
    fig.path.set_facecolor('#2b2b2b')
    ax.plot(rotated_track[:, 0], rotated_track[:, 1], color='yellow')
    ax.set_facecolor('#2b2b2b')
