
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthday_greetings = {}
    
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date*
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = birthday_this_year.strftime("%A")
            if weekday in ["Saturday", "Sunday"]:
                birthday_this_year += timedelta(days=(7 - delta_days))

            if weekday not in birthday_greetings:
                birthday_greetings[weekday] = [name]
            else:
                birthday_greetings[weekday].append(name)
        
    formatted_greetings = ""
    for weekday, names in sorted(birthday_greetings.items()):
        formatted_greetings += f"{weekday}: {', '.join(names)}\n"
    
    return formatted_greetings
    

vocab = [{"name": "Bill Gates", "birthday": datetime(1955, 3, 1)},
        {"name": "Morty bed", "birthday": datetime(1955, 3, 2)},
        {"name": "Tom HeS", "birthday": datetime(1955, 3, 2)}]

print(get_birthdays_per_week(vocab))

    

    #if __name__ == '__main__':
    #{'Monday': ['Bill Gates'], 'Thursday': ['Jan Koum']}

    





