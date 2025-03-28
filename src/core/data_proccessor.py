from data_fetcher import *
from tabulate import tabulate

def format_schedule(schedule):
    """ Formatting schedule output, making good table using tabulate module """
    # TODO: Эта история не сильно подходит для тг бота, но хороша для терминала
    calendar_text = f"Календарь сезона {schedule.year}: \n\n"
    data = [["Номер Гран-При", "Название", "Страна проведения","Дата"]]
    for _, race in schedule.iterrows():
        round_number = race['RoundNumber']
        event_name = race['EventName']
        country = race['Country']
        date = race['EventDate'].strftime("%d.%m.%Y")
        row = [round_number,event_name,country,date]
        data.append(row)
    calendar_text = tabulate(data[1:], headers = data[0], tablefmt ="grid")
    return calendar_text


def main():
    user_year = int(input("Введите желаемый год: "))
    print(f"Скачиваю данные на {user_year} год...")
    user_schedule = get_event_schedule(user_year)
    print("Подготавливаю данные...") 
    user_calendar = format_schedule(user_schedule)
    print(user_calendar)


if __name__ == "__main__":
    main()
