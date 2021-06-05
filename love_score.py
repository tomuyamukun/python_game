# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
name_lower = name.lower()


T_count = name_lower.count("t")
R_count = name_lower.count("r")
U_count = name_lower.count("u")
E_count1 = name_lower.count("e")

true = T_count + R_count + U_count + E_count1

L_count = name_lower.count("l")
O_count = name_lower.count("o")
V_count = name_lower.count("v")
E_count2 = name_lower.count("e")

Love = L_count + O_count + V_count + E_count2
love = int(str(true) + str(Love))


if (love < 10) or (love > 90):
  print(f"Your score is {love}, you go together like coke and mentos.")
elif (love >=40) and (love <=50):
  print(f"Your score is {love}, you are alright together.")
else:
  print(f"Your score is {love} ,")
