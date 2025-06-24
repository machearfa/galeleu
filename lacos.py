#criar uma variavel chamada soma
#soma = 0 
#for o in range(10):
  #  soma = soma + 1
  #  print(o)

import turtle
import time

#while True:
    #print()
#soma = 0 
#while soma < 1000: # enquanto soma for menor que 1000
   # soma = soma + 10 #soma o valor antigo
   # print(soma) #logo em seguida printa o resultado em tela

turas = turtle.Turtle()


turas.back(60)
turas.color('red')
turas.shapesize(30)
while True:
    turas.circle(70)
    turas.shapesize(-1)
    turas.shapesize(+1)
