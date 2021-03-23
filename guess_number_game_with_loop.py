import random

# magic_number = random.randint(1, 100)

# print(magic_number)
# magic_number = 0

game = "yes"
while game.lower() == "yes":
    magic_number = random.randint(1, 100)
    print(magic_number)
    guess = 0
    attempts = 0
    while guess != magic_number:
        print("I'm thinking of a magic number between 1 and 100. ")
        guess = int(input("What is your guess? "))
        attempts += 1
        pass
        if guess > magic_number:
            print("Too high! Guess again. ")
        elif guess < magic_number:
            print("Too low! Guess again. ")
        elif guess == magic_number:
            print(f"Congratulations! You guessed it right in {attempts} attempts. ")

        if attempts <= 1:
            print("You have guessed {} time. ".format(attempts))
        else:
            print("You have guessed {} times. ".format(attempts))
    game = input("Would you like to play again? ")


