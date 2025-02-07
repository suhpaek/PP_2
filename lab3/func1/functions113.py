import random

def greet_user():
    print("Hello! What is your name?")
    name = input()
    return name

def generate_number():
    return random.randint(1, 20)

def give_feedback(guess, number, name, attempt_count):
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in {attempt_count} guesses!")
