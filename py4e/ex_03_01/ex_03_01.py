string_hours = input("Enter Hours: ")
string_rate = input("Enter Rate: ")

try:
    float_hours = float(string_hours)
    float_rate = float(string_rate)
except:
    print('Error, please enter numric number')
    quit()

if float_hours > 40:
    regular_pay = float_hours * float_rate
    over_time_pay = (float_hours - 40.0) * (float_rate * 0.5)
    extra_pay = regular_pay + over_time_pay
else:
    extra_pay = float_hours * float_rate
print("Pay:", extra_pay)
