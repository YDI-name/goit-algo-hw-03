from datetime import datetime

def get_days_from_today(date):
    try:
        # Ця частина коду перетворює вхідній рядок даті на об'єкт дати та часу
        given_date = datetime.strptime(date, '%Y-%m-%d')
        # return повертає текст який вказує на те що дата була введена не вірно
    except ValueError:
        return "Дата введена не вірно. Введіть будь ласка 'YYYY-MM-DD'."

    # Отримуємо поточну дату та час, витягуємо лише частину дати, ігноруючи години, хвилини та секунди
    today = datetime.now().date()
    given_date_only = given_date.date()

    # Обчислюємо різницю між сьогоднішньою датою та заданою датою
    delta = today - given_date_only

    # Та повертаємо кількість днів як ціле число
    return delta.days

# Як приклад, викликаємо функцію з різними датами
print(f"Number of days from '2020-10-09' to today: {get_days_from_today('2017-10-09')}")
print(f"Number of days from '2026-03-25' to today: {get_days_from_today('2028-06-25')}")
print(f"Number of days from '2025-09-23' to today: {get_days_from_today('2025-09-19')}")
print(f"Result for invalid date '2025-13-35': {get_days_from_today('2005-18-45')}")