import fastf1
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
import asyncio
from schemas import RaceSchedule

fastf1.Cache.enable_cache("./cache")


async def get_closest_race():
    """..."""
    current_day = datetime.now(pytz.UTC).toordinal()

    schedule = await get_race_schedule()
    closest_events = [event for event in schedule if ((event.date.toordinal() \
            - datetime.now(pytz.UTC).toordinal())) in range (0,40)] 

    return closest_events[0]

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


async def get_track_coordinates(session:Session) -> list[float]:  # TODO: Not sure about annotations
   
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
