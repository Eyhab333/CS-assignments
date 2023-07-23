str_length = input("Please type Length: \n")
str_width = input("Please type Width: \n")
str_pay = input("How much for 1 meter: \n")
# convert type
length = float(str_length)
width = float(str_width)
pay = float(str_pay)
# find area
area = length * width
guy_pay = area * pay
print("The total area is:", area)
print("Give the guy:", "$", guy_pay)