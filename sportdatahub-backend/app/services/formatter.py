from tabulate import tabulate


def format_schedule_cli(schedule):
    """Formatting schedule output for cli, making good table using tabulate module."""
    calendar_text = f"Календарь сезона {schedule.year}: \n\n"
    data = [["Номер Гран-При", "Название", "Страна проведения", "Дата"]]
    for _, race in schedule.iterrows():
        round_number = race["RoundNumber"]
        event_name = race["EventName"]
        country = race["Country"]
        date = race["EventDate"].strftime("%d.%m.%Y")
        row = [round_number, event_name, country, date]
        data.append(row)
    calendar_text = tabulate(data[1:], headers=data[0], tablefmt="grid")
    return calendar_text
