try:
  age = float(input("Enter your age: "))
  have_license = input("Do you have a license? Choose (Yes) or (No): ")
  if age >= 18 and have_license.lower() == "yes":
      print("You can drive")
  else:
      print("Sorry, you can not drive")    
except:
   print("please provide a numeric value in age")
   quit()
        