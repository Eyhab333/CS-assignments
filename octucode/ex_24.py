user_input = input("Enter the color you like: ").lower()
colors = []
colors.append(user_input)
ask_user = input("Do you want to add more colors? Yes or No").lower()
if ask_user.lower == "yes":
  add_color = input("Add another color to the list: ").lower()
  colors.append(ask_user)
elif ask_user.lower == "no":
  print(f"The color you like is: {ask_user}") 
else:
  print("Invalid entry")
  quit()   