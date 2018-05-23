import requests
import datetime
import time

import telebot

def bus(last_chat_id):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
	keyboard.add(*[types.KeyboardButton(name) for name in ['Курчатова', 'Факультет Радиофизики']])
	answer = skaffer.send_message(last_chat_id, 'Время прибытия ближайшего автобуса к какой остановке вам нужно?', reply_markup = keyboard)

	print(answer)

	current_time = list((str(datetime.datetime.now().time())).split(':'))
	hour = int(current_time[0]) + 3
	minute = int(current_time[1])

	day_bus = list(time.ctime().split())
	day_now = day_bus[0]

	if day_now != 'Sat' and day_now != 'Sun':
		with open('database/47_bus_timetable.txt') as bus_timetable:
			time_leave = list(str(i) for i in bus_timetable.readline().strip().split(':'))
			time_bus = []
		
			while time_leave != ['']:
				min_hour = 24
				min_minute = 60

				true_time = []
				minute_table = int(time_leave[1])
				hour_table = int(time_leave[0])

				if hour_table - hour == 0:
					if minute_table - minute <= min_minute and minute_table - minute >= 0:
						time_bus = time_leave
						min_minute = minute_table - minute
						break
				elif hour_table - hour >= 0:
					time_bus = time_leave
					break

				time_leave = list(str(i) for i in bus_timetable.readline().strip().split(':'))

			if time_bus == []:
				skaffer.send_message(last_chat_id, 'На сегодня втобус 47с окончил движение')
			else:
				message_time = 'Следующий автобус в '
				message_time += time_bus[0]
				message_time += ':'
				message_time += time_bus[1]
				message_time += ' на остановке "Курчатова"'
				skaffer.send_message(last_chat_id, message_time)
	else:
		skaffer.send_message(last_chat_id, 'По выходным автобус 47с не ходит')