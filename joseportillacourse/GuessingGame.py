from random import randint

correct_answer = randint(0, 100)
print("-====- Guessing game -====-")

guesses = []

while True:
    guess = int(input("Guess a number between 0 - 100: "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    if guess == correct_answer:
        print("GJ! Correct!")
        break

    guesses.append(guess)

    # guesses[-2] (dla pustego da false) -> wiecej niz jedna runda
    # len(guesses) < 2
    if len(guesses) < 2:
        if abs(correct_answer - guess) > 10:
            print("Cold")
        else:
            print("Warm")
    else:
        if abs(correct_answer - guess) > abs(correct_answer - guesses[-2]):
            print("Colder")
        else:
            print("Warmer")
