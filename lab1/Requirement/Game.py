import random


# TODO [1]: implement the guessing_game function
def guessing_game(max: int, *, attempts: int) -> tuple[bool, list[int], int]:
    target_number: int = random.randint(1, max)
    guesses: list[int] = []
    attempt: int = 0
    
    while attempt < attempts:
        attempts_left: int = attempts - attempt
        try:
            user_input: str = input(f"Attempt {attempt + 1}/{attempts}: Enter your guess (1-{max}): ")
            guess: int = int(user_input)
        except ValueError:
            print(f"Invalid input! Please enter a valid integer. {attempts_left} attempts left.")
            continue
        
        if guess < 1 or guess > max:
            print(f"Invalid range! Please enter a number between 1 and {max}. {attempts_left} attempts left.")
            continue
        
        attempt += 1
        guesses.append(guess)
        
        if guess == target_number:
            print("Congratulations! You've guessed the number!")
            return True, guesses, target_number
        elif guess < target_number:
            print(f"Too low! Try again. {attempts_left - 1} attempts left.")
        else:
            print(f"Too high! Try again. {attempts_left - 1} attempts left.")
    
    print(f"Sorry, you've used all attempts. The number was {target_number}.")
    return False, guesses, target_number
# TODO [2]: implement the play_game function
def play_game() -> None:
    """
    Main game loop that calls guessing_game with max=20 and attempts=5.
    Validates results with assertions and asks to play again only if the player lost.
    """
    max_value: int = 20
    attempts: int = 5
    
    while True:
        print("\nWelcome to the Guessing Game!")
        print(f"I'm thinking of a number between 1 and {max_value}.")
        print(f"You have {attempts} attempts to guess the number.")
        
        is_won, guesses, chosen_int = guessing_game(max_value, attempts=attempts)
        
        if is_won:
            # Player won: assert chosen_int is in guesses, then end
            assert chosen_int in guesses, f"Error: {chosen_int} should be in guesses {guesses}"
            print(f"\n You won! The number was {chosen_int}. Your guesses: {guesses}")
            print("Thanks for playing! Goodbye!")
            break
        else:
            # Player lost: assert chosen_int is NOT in guesses, then ask to play again
            assert chosen_int not in guesses, f"Error: {chosen_int} should not be in guesses {guesses}"
            print(f"\n You lost! The number was {chosen_int}. Your guesses: {guesses}")
            
            play_again: str = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing! Goodbye!")
                break


if __name__ == "__main__":
    play_game()

