import random

print("Welcome to the Palindrome game")
print("Tossed 3 dices")

#3 dices tossed simultaneously
dice1 = str(random.randint(1, 6))
dice2 = str(random.randint(1, 6))
dice3 = str(random.randint(1, 6))

formedNum = dice1 + dice2 + dice3
reversedNum = dice3 + dice2 + dice1

print(f"The dices formed a number of {formedNum}")
score = 0
i = 0

while i <= 100:
    if formedNum == reversedNum:
        score += 10
        print("It is a palindrome number\nDo you want to double your score?")
        try:
            userAns = input("Enter yes or no.")
            if userAns.lower() == "yes":
                dice4 = str(random.randint(1, 6))
                dice5 = str(random.randint(1, 6))
                dice6 = str(random.randint(1, 6))
                formedNum2 = dice4 + dice5 + dice6
                reversedNum2 = dice6 + dice5 + dice4
                if formedNum2 == reversedNum2:
                    score *= 2
                else:
                    score -= 10
            else:
                score = score
        except ValueError:
            print(f"Invalid input! Please enter only yes or no")
    elif formedNum != reversedNum:
        print("It is not a palindrome number")