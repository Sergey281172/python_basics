"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""

time_in_sec = int(input("Enter your local time in sec: "))
hours = time_in_sec // 3600
residue = time_in_sec % 3600
minutes = residue // 60
sec = residue % 60
print(f"Now is {hours}:{minutes}:{sec} ")
