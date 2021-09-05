import turtle as ttt           # Подключаем модуль turtle
from settings import *
from random import randint

#Кривая Коха
# start = "F"
# rule = {
# "F": "F+F-F-F+F",
# "+": "+",
# "-": "-"
# }

res = sequence["start"]
for i in range(sequence["iter"]):
     resTemp = ""
     for x in res:

          if x in list(sequence["rule"]):
               resTemp += sequence["rule"][x]
          else:
               resTemp += x
               
     res = resTemp

print(res)


win_width, win_height = 1920, 1080

turtle = ttt
turtle.setup()
turtle.screensize(win_width, win_height)
turtle.color('#363636')

turtle.tracer(tracer)
turtle.right(start_angle)
turtle.pensize(1)
turtle.up()
turtle.goto(start_position[0], start_position[1])
turtle.down()
temp = []


for x in res:
     try:
          if functions[x][0] == "" : #Переместить
               turtle.up()
               turtle.forward(int(functions[x][2:]))
               turtle.down()

          if functions[x][0] == "1" : #Рисовать
               turtle.forward(int(functions[x][2:]))

          elif functions[x][0] == "2": #Повороот
               turtle.right(int(functions[x][2:]))
                    
          elif functions[x][0] == "3": #Повороот
               k = functions[x][2:].split(".")
               turtle.right(randint(int(k[0]), int(k[1])))     

          elif functions[x][0] == "4": #Сохранить
               tt = turtle.position()
               temp.append((tt[0], tt[1], turtle.heading()))

          elif functions[x][0] == "5": #Востановить
               tt = temp[-1]
               turtle.up()
               turtle.goto(tt[0], tt[1])
               turtle.setheading(tt[2])
               turtle.down()
               temp.pop(-1)


     except Exception as e:
          print(e)



turtle.up()             # Поднять перо (закончить рисовать)


input()

ts = turtle.getscreen()
ts.getcanvas().postscript(file="duck.eps")