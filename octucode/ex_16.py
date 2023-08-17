
age = float(input("Enter your age: "))
have_license = input("Do you have a license? Choose (Yes) or (No): ")
if age >= 18 and have_license.lower() == "yes":
    print("You can drive")
elif age < 18 or have_license.lower() == "no":
    print("Sorry, you can not drive")    
else:

    print(f"Sorry, your entery of [ {have_license} ] is not understood")
    