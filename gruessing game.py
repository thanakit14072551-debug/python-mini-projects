import random

def play():
    secret = random.randint(1, 100)
    tries = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("Your guess: ")

        if not guess.isdigit():
            print("Numbers only")
            continue

        guess = int(guess)
        tries += 1

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Got it! The number was {secret}. You took {tries} tries.")
            break

while True:
    play()
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Bye!")
        break