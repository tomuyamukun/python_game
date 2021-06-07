def prime_checker(number):
  p = 0
  for k in range(1, number+1):
    if number % k == 0:
      p += 1
  if p > 2:
    print(f"It's not a prime number.")
  else:
    print("It's a prime number.")  

    

  



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


