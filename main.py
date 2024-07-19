import random 
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

computer_num = random.randint(0,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
guesses = 0
user_guess = ""

def easy():
  return guesses + 10

def hard():
  return guesses + 5

  
  
def game_plan(guesses, user_guess, computer_num):
  print(f"You have {guesses} attempts remaining to guess the number.")
  print(computer_num)
  if guesses == 0:
    print("You ran out of guesses. You lose")
  else: 
    for num in range(guesses):
      user_guess = int(input("Make a guess: "))
      if user_guess == computer_num:
        print(f"You got it! The answer was {computer_num}")
        break
      elif user_guess < computer_num:
        guesses -= 1
        print("Too low.\nGuess again.")
        print(f"You have {guesses} attempts remaining to guess the number.")
      elif user_guess > computer_num:
        guesses -= 1
        print("Too high.\nGuess again.")
        print(f"You have {guesses} attempts remaining to guess the number.")
      
  
  
if difficulty == "easy":
  game_plan(guesses = easy(), user_guess = user_guess, computer_num = computer_num )
else:
  game_plan(guesses = hard(), user_guess = user_guess, computer_num = computer_num)