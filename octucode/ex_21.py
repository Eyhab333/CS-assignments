import random


try:
    user_random_number = int(input("Enter a 4-digit PIN code: "))
    computer_random_number = random.randint(1000,9999)
    if user_random_number == computer_random_number:
        print("nice")
    elif len(str(user_random_number)) != 4 :
        print("enter 4 digites") 
    else:
        print("Failure! PIN code doesn't match")  
        print(f"The computer generated this PIN: {computer_random_number}")  
except:
    print("please provide a numeric input")
