def month_to_season(month):
    if 1 <= month <= 2 or month == 12:
        return "Зима"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    elif 3 <= month <= 5:
        return "Весна"
    else:
        return "Неверный номер месяца"


print(month_to_season(2))
