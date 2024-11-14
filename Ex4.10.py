import random

def guess_the_number():
    while True:
        number_to_guess = random.randint(1, 1000)
        print("Guess my number between 1 and 1000 with the fewest guesses:")
        
        while True:
                guess = int(input("Your guess: "))
                if guess < number_to_guess:
                    print("Too low. Try again.")
                elif guess > number_to_guess:
                    print("Too high. Try again.")
                else:
                    print("Congratulations! You guessed the number!")
                    break
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again == 'no':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    guess_the_number()
