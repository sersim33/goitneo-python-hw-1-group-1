
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthday_greet = {}
    
    
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

            if weekday not in birthday_greet:
                birthday_greet[weekday] = [name]
            else:
                birthday_greet[weekday].append(name)
        
    formatted_greetings = ""
    for weekday, names in sorted(birthday_greet.items()):
        formatted_greetings += f"{weekday}: {', '.join(names)}\n"
    
    return formatted_greetings
    

vocab = [{"name": "Bill Gates", "birthday": datetime(1955, 2, 28)},
        {"name": "Morty bed", "birthday": datetime(1955, 3, 2)},
        {"name": "Tom HeS", "birthday": datetime(1955, 3, 3)},
        {"name": "Uter AWS", "birthday": datetime(1955, 3, 1)}]

print(get_birthdays_per_week(vocab))

    

    #if __name__ == '__main__':
    #{'Monday': ['Bill Gates'], 'Thursday': ['Jan Koum']}

    





