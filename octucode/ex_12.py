try:
    guess = int(input("Inter your guess number:\n"))
    if guess == 12:
        print("You won")
    else:
        print("You lose") 
except:
    print('Error, please enter numric number')
    quit()           