import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

janken = [rock, paper, scissors]

vs = random.choice(janken)

visitor = input("let\'s is janken 0 is rock, 1 is paper, 2 is scissors ")

if visitor == '0':
  visitor = rock
elif visitor == '1':
  visitor = paper
elif visitor == '2':
  visitor = scissors
else:
  print("please 0, 1 or 2 ")


if vs == visitor:
  print(f"your choice\n{visitor}")
  print(f"computer choice\n{vs}")
  print("No Game")
elif (vs == rock) and visitor == scissors:
  print(f"your choice\n{visitor}")
  print(f"computer choice\n{vs}")
  print("your lose")
elif (vs == rock) and visitor == paper:
  print(f"your choice\n{visitor}")
  print(f"computer choice\n{vs}")
  print("you Win!")
elif (vs == paper) and visitor == rock:
  print(f"your choice\n{visitor}")
  print(f"computer choice\n{vs}")
  print("your lose")
elif (vs == paper) and visitor == scissors:
  print(f"your choice\n{visitor}")
  print(f"computer choice\n{vs}")
  print("you Win!")
elif (vs == scissors) and visitor == paper:
  print(f"your choice\n{visitor}")
  print(f"computer choice\n{vs}")
  print("your lose")
elif (vs == scissors) and visitor == rock:
  print(f"your choice\n{visitor}")
  print(f"computer choice\n{vs}")
  print("you Win!")

# 別の書き方
# visitor = int(input("let\'s is janken 0 is rock, 1 is paper, 2 is scissors "))


# computer_choice = random.randint(0, 2)

# if visitor == 0 and computer_choice == 2:
#   print("you win")
# elif computer_choice == 0 and visitor == 2:
#   print("you lose")
# elif computer_choice > visitor:
#   print("you lose")
# elif visitor >= 3 or visitor < 0:
#   print("you type miss")
# elif visitor > computer_choice:
#   print("you win!")
# elif computer_choice == visitor:
#   print("It's draw")