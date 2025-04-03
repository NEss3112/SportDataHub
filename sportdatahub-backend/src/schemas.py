from pydantic import BaseModel
from datetime import datetime

class RaceSchedule(BaseModel):
    round: int
    name: str
    location: str
    country: str
    date: datetime
    time: str # HH:MM
