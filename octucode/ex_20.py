import random
user_random_number = int(input("Enter a 4-digit PIN code: "))
computer_random_number = random.randint(2000,9000)
if user_random_number == computer_random_number:
    print("nice")
elif user_random_number == "":
    print("enter numbers") 
else:
    print("Failure! PIN code doesn't match")  
    print(f"The computer generated this PIN: {computer_random_number}")  