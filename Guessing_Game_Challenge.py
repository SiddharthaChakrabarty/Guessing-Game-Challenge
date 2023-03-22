from random import randint
random_number = randint(1,100)
print("Welcome to the Guessing Game Challenge!")
print("The system generates a random number and you are supposed to guess that number.")
print("Rules for the game : ")
print("On a your first turn, if your guess is :")
print("1. Within 10 of the number, you will see WARM!")
print("2. Further than 10 away from the number, you will see COLD!")
print("On all subsequent turns, if your guess is")
print("1. Closer to the number than the previous guess, you will see WARMER!") 
print("2. Farther from the number than the previous guess, you will see COLDER!")
print("3. At the same difference as the previous guess, you will see NORMAL!")
print("The lesser number of guesses you take, the better you perform.")
print("So, let's start the game.")
guesses = []
while True:
    guess = int(input("Enter your guess\n"))
    guesses.append(guess)
    if(guess == random_number ):
        print("Congratulations!!! Correct Guess.")
        break
    if(guess<1 or guess>100):
        print("OUT OF BOUNDS!")
    elif (len(guesses) == 1):
        if (abs(guesses[-1]-random_number) <= 10):
            print("WARM!")
        elif (abs(guesses[-1]-random_number) > 10):
            print("COLD!")
    else:
        if (abs(guesses[-1]-random_number) < abs(guesses[-2]-random_number)):
            print("WARMER!")
        elif (abs(guesses[-1]-random_number) > abs(guesses[-2]-random_number)):
            print("COLDER!")
        elif (abs(guesses[-1]-random_number) > abs(guesses[-2]-random_number)):
            print("NORMAL")
print("You took {} attempts to guess the correct number.".format(len(guesses)))
print("Thank you for playing this game.")
