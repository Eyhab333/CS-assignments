try:
  colors = []
  user_input = input("Enter the color you like: ").lower()
  colors.append(user_input)
  ask_user = input("Do you want to add more colors? Yes or No: ").lower()
  if ask_user.lower() == "yes":
    add_color = input("Add another color to the list: ").lower()
    colors.append(add_color)
    print(f"The colors you like are: {colors}")
  elif ask_user.lower() == "no":
    print(f"The color you like is: {user_input}") 
  else:
    print("Invalid entry")
    quit()
except:
  print("Enter valid choice")