import random 
number = random.randint(1,9)
chance = 0
print("You have 5 chances")

#numList = [1,2,3,4,5,6,7,8,9]
#randomNum = random.choice(numList)

while chance<5:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == number:
        print("Yay!You guessed the correct number!")
        break
    elif guess > number:
        print("Too high :(, Try again")
    else:
        print("Too low :(, Try again")
    chance = chance + 1

    if not chance<5:
        print("YOU LOSE!! The number is: ",+number)
    