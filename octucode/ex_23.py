import random
print("Welcome to the Coin Guessing Game!")
print("Chosse a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")

# try:
choice = input("Enter your choice (1 or 2): ")
if choice == "1":
  random_random = random.random()
  if random_random >= 0.5:
    computer_choice = "Heads"
  else:
    computer_choice = "Tails" 
elif choice == "2":
  random_randint = random.randint(0, 1)
  if random_randint >= 5:
    computer_choice = "Heads"
  else:
    computer_choice = "Tails"
else:
  print("Invalid choice, enter 1 or 2")
  quit()

user_choice = input("Enter your Guess (Heads or Tails): ")
if user_choice.lower() == computer_choice.lower():
  print("You Won!")
else:
  print("Sorry, you lost")        
# except:
  # print("Invalid choice, enter 1 or 2")
print(f"The computer's coin toss result was: {computer_choice}")  
# try:
choice = input("Enter your choice (1 or 2): ")
if choice == "1":
  random_random = random.random()
  if random_random >= 0.5:
    computer_choice = "Heads"
  else:
    computer_choice = "Tails" 
elif choice == "2":
  random_randint = random.randint(0, 1)
  if random_randint >= 5:
    computer_choice = "Heads"
  else:
    computer_choice = "Tails"
else:
  print("Invalid choice, enter 1 or 2")
  quit()

user_choice = input("Enter your Guess (Heads or Tails): ")
if user_choice.lower() == computer_choice.lower():
  print("You Won!")
else:
  print("Sorry, you lost")        
# except:
  # print("Invalid choice, enter 1 or 2")
print(f"The computer's coin toss result was: {computer_choice}")  