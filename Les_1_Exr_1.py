

dur = int(input('Введите продолжительность в секундах(целое положительное число): '))

# Задаем константы временных отрезков для минут, часов и дней

MIN = 60
HOUR = MIN * 60
DAY = HOUR * 12

# Получаем временные отрезки для конкретного промежутка

days = dur // DAY

hours = (dur % DAY) // HOUR

minutes = (dur % HOUR) // MIN

seconds = (dur % MIN) % MIN

#Применяем ветвление для того, чтобы отбросить ненужные временные промежутки

if days == 0 and hours != 0:
    print(f'{hours} ч {minutes} мин {seconds} сек')
elif days == 0 and hours == 0 and minutes != 0:
    print(f'{minutes} мин {seconds} сек')
elif days == 0 and hours == 0 and minutes == 0 and seconds != 0:
    print(f'{seconds} сек')
elif days == 0 and hours == 0 and minutes == 0 and seconds == 0:
    print(f'{seconds} сек')
else:
    print(f'{days} дн {hours} ч {minutes} мин {seconds} сек')