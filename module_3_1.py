# Глобальная переменная для подсчёта вызовов
calls = 0

# Функция для подсчёта вызовов
def count_calls():
    global calls
    calls += 1

# Функция для получения информации о строке
def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    return len(string), string.upper(), string.lower()

# Функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower

# Примеры вызовов функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

# Вывод общего количества вызовов
print(calls)
