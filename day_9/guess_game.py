print("Welcome to the Guessing Game! You have only 3 chances " \
"Please choose carefully otherwise you'll loose")
x= 30
attempts = 0

while attempts < 3:
    number = input("Enter your number: ")
    attempts += 1
    if int(number) < x:
        print(f"Your number {number} is low! Please try again")
    elif int(number) > x:
        print(f"Your number {number} is high! Please try again")
    else:
        print("Congratualtions! You have won the game")
        break
else:
    print("Out of guesses. I guess you have lost the game" \
    "buhahahha")

