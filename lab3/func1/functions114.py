from game_helpers import greet_user, generate_number, give_feedback

def play_game():
    name = greet_user()
    number = generate_number()
    attempt_count = 0
    guessed = False

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    while not guessed:
        print("Take a guess.")
        guess = int(input())
        attempt_count += 1
        
        if guess == number:
            guessed = True
        else:
            give_feedback(guess, number, name, attempt_count)

    give_feedback(guess, number, name, attempt_count)

if __name__ == "__main__":
    play_game()
