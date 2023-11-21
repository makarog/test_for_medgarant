import datetime

busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]


# Функция для преобразования времени из строки в объект datetime
def parse_time(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return datetime.datetime.combine(datetime.datetime.today(), datetime.time(hours, minutes))


# Время начала и окончания работы доктора
start_time = parse_time('09:00').time()
end_time = parse_time('21:00').time()

# Создание списка всех возможных окон
window_duration = datetime.timedelta(minutes=30)
current_time = datetime.datetime.combine(datetime.datetime.today(), start_time)
end_datetime = datetime.datetime.combine(datetime.datetime.today(), end_time)
all_windows = []
while current_time + window_duration <= end_datetime:
    all_windows.append((current_time.time(), (current_time + window_duration).time()))
    current_time += window_duration

# Удаление занятых окон
available_windows = all_windows.copy()
for appointment in busy:
    appointment_start = parse_time(appointment['start']).time()
    appointment_end = parse_time(appointment['stop']).time()
    available_windows = [(start, end) for start, end in available_windows if
                         end <= appointment_start or start >= appointment_end]

# Печать списка свободного времени
for window in available_windows:
    start_time = window[0].strftime('%H:%M')
    end_time = window[1].strftime('%H:%M')
    print(f"Свободно с {start_time} до {end_time}")
