import fastf1.events
import pytest
from sportdatahub.data_fetcher import get_event_schedule

def test_get_event_schedule():
    schedule = get_event_schedule(2025)
    assert isinstance(schedule, fastf1.events.EventSchedule), "received schedule is not an EventSchedule instance"
    assert "EventName" in schedule


def test_get_event_schedule_invalid_year():
    with pytest.raises(ValueError):
        get_event_schedule(1000)

