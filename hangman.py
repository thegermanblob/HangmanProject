import random

words = ["silla", "mesa", "desk", "piso", "techo"]
vowels = ['a','e','i','o','u']
pepe = list(random.choice(words))
hint = 0
for vowel in vowels:
    if vowel in pepe:
        hint = hint + 1
guesslist = [""] * len(pepe)
lives = 5
print(f"the word has {len(pepe)} letters\n and {hint} vowels")
while lives > 0:
    guess = input("please input one letter at a time: \n")
    if guess in pepe:
        for i, value in enumerate(pepe):
            if value == guess:
                guesslist[i] = guess

        print("correct")
    else:
        print("wrong")
        lives = lives - 1
    if guesslist == pepe:
        print("you win")
        break
    print(guesslist)

