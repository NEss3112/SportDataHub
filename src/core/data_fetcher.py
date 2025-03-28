import fastf1

def get_event_schedule(year:int):
    """Gets event schedule for choosen year"""
    return fastf1.get_event_schedule(year, backend='fastf1')

