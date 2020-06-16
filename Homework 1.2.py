#Homework 1.2: Guess the secret number

secret = 5

guess = int(input("Guess the secret number:"))

if guess == secret:
    print("Congratulation!")
else:
    print("You are wrong, try another time!")
