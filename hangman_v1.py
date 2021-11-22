import random

words = ["silla", "mesa", "desk", "piso", "techo"]
pepe = random.choice(words)
lives = 5
while lives > 0:
    guess = input("please input a word at a time: \n")
    if guess == pepe:
        print("correct")
        break
    else:
        print("Wrong")
        lives -= 1