from art import logo, vs
from game_data import data
import random
from replit import clear


# print文のデータをまとめている
def format_data(data):
  data_name = data["name"]
  data_description = data['description']
  data_country = data['country']
  return f"{data_name}, a {data_description}, from {data_country}"



def game():

  continue_game = True
  score = 0
  while continue_game == True:
    data_a = random.choice(data)
    data_b = random.choice(data)
    print(logo)

    if score > 0:
      print(f"You're right! Current score: {score}.")

    print(f"Compare A: {format_data(data_a)}")
    print(vs)
    print(f"Against B: {format_data(data_b)}")




    follower_a = data_a['follower_count']

    follower_b = data_b['follower_count']

    you_choice = input("Who has more followers? Type 'A' or 'B': ")

    # 大文字小文字区別しないで判定
    if you_choice.upper() == 'A':
      if follower_a > follower_b:
        score += 1
        clear()
      else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False
    elif you_choice.upper() == 'B':
        if follower_b > follower_a:
          score += 1
          clear()
        else:
          print(f"Sorry, that's wrong. Final score: {score}")
          continue_game = False
    else:
      clear()

game()