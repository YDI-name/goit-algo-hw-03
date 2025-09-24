import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка вхідніх параметрів на коректність
    if not (1 <= min <= max <= 1000 and 0 and (max - min + 1) >= quantity):
        # Вертаємо порожній список для некоректних параметрів
        return []

    # Створюємо порожню множину для зберігання унікальних чисел
    unique_numbers = set()

    # Генеруйте унікальні випадкові числа, до потрібної кількості
    while len(unique_numbers) < quantity:
        # Генеруємо випадкове число в заданому діапазоні
        random_number = random.randint(min, max)
        # Додоємо число до множини (автоматично унікальне)
        unique_numbers.add(random_number)

    # Перетворюємо множину в відсортований список
    sorted_numbers = sorted(list(unique_numbers))

    return sorted_numbers

# Пріклад виклику функції:
lottery_ticket = get_numbers_ticket(1, 49, 6)
if lottery_ticket:
    print("Your lucky lottery numbers:", lottery_ticket)
else:
    print("Invalid parameters. Please check your input.")