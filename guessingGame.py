import random
number = random.randint(1, 9)
chanceCount = 0
while (chanceCount < 5):
    introString = int(input("enter the number between 1-9: "))
    if (introString > number):
        print("Your guess is too high")
    elif (introString == number):
        print("Congratulation YOU WON")
    else :
        print("Your guess is too low")
    chanceCount = chanceCount + 1
if (chanceCount > 5):
    print("You loss!! The number was", number)