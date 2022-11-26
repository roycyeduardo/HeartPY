from turtle import *
from termcolor import colored

print("\n>-=========->")
print(colored("\nQual o nome do amor da sua vida?", 'red'))
nome = input()
print(colored("\n😍 Eu te amo " + nome + "!", 'red'))
print("\n>-=========->")

begin_fill() # Começa desenhar
bgcolor('black')
color("red")
pensize(10)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill() # Termina o desenho

print("\nPressione (Enter) para sair do programa:") 
input()