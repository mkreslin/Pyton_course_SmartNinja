#Homework 1.1: The mood checker

mood = input("What mood are you in (happy,nervous,sad,excited,relaxed,other)?:")


if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times!")
elif mood == "sad":
    print("Maybe one smile will help you!")
elif mood == "excited":
    print("Please, share with us your excitement!")
elif mood == "relaxed":
    print("Enjoy this moment!")
else:
    print("I don't recognize this mood!")

