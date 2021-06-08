from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! the answer is {answer}")

def set_dificulty():
  dificulty = input(" 難易度選択： 'easy' or 'hard'")
  if dificulty == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
  

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = random.randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_dificulty()

  guess = 0

  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("you lose")
      return 
    elif guess != answer:
      print("Guses again")

game()