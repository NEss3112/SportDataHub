import fastf1

fastf1.Cache.enable_cache("./cache")

def get_event_schedule(year: int):
    """Gets event schedule for chosen year."""
    return fastf1.get_event_schedule(year, backend="fastf1")


def get_session(year, event, session):
    """Gets event information from fastf1 for chosen year, event and session."""
    session = fastf1.get_session(year, event, session, backend="fastf1")
    session.load()
    return session
