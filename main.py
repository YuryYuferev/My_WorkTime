import datetime

# start_date = input('Введите дату последнего рабочего дня (в формате ДД.ММ.ГГГГ.): ')
start_date = ('03.03.2021.')

target_date = input('Введите дату, которую нужно найти (в формате ДД.ММ.ГГГГ.): ')

start_date = datetime.datetime.strptime(start_date, '%d.%m.%Y.')
target_date = datetime.datetime.strptime(target_date, '%d.%m.%Y.')

days_diff = (target_date - start_date).days

start_day = ['рабочий день (сутки)', '1-й выходной день', '2-й выходной день', '3-й выходной день']

if days_diff % 4 == 0:
    print(f"Это {start_day[0]}")
elif days_diff % 4 == 1:
    print(f"Это {start_day[1]}")
elif days_diff % 4 == 2:
    print(f"Это {start_day[2]}")
else:
    print(f"Это {start_day[3]}")

input()
