#0 - Не показівать процесс рисования, 1 - показівать процесс рисования
tracer = 0 

#Начальный угол черепашки
start_angle = -90 

#Начальное положение черепашки
start_position = [-400, -200]

#Генерация последовательности
sequence = {"iter": 4, #Кол-во итерация
			"start": "F++F-F++F", #Начальная строка последовательности
			"variables": "FX+-[]", #Список переменных, которые используются
			"rule": { #Список правил преобразования
				"F": "FF+[-FF-F+F+F]F-", #Первое правило
				}
			}

#Переместить - 0 Параметры: длина отрезка
#Рисовать - 1 Параметры: длина отрезка
#Повороот - 2 Параметры: 1,2 - поворот в лево в право, поворот в градусах
#Повороот рандом - 3 Параметры: 1,2 - поворот в лево в право, поворот в градусах, мин, макс
#Сохранить - 4
#Востановить - 5
functions = {"F": "1.3",
			"X": "1.4",
			"+": "2.30",
			"-": "2.-30",
			"[": "4",
			"]": "5",}

