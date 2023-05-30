import random

generatedNum = random.randint(0, 99)
userAns = 0
attemptNum = 0

while userAns != generatedNum:
    while True:
        try:
            print("Guess a number between 0 and 99.")
            userAns = int(input("What's your number?"))
            attemptNum += 1
            if userAns == generatedNum:
                print("Congrats, you guess the number correctly.")
                print(f"You have attempted {attemptNum} numbers of times.")
            elif userAns > generatedNum:
                print("Try again your number is too high.")
            else:
                print("Try again your number is too low.")
        except ValueError:
            print("Invalid input! Please enter an integer number only.")