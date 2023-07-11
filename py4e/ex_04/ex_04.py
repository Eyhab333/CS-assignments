
def computepay(hours, rate) :
    if hours > 40:
        regular_pay = hours * rate
        over_time_pay = (hours - 40.0) * (rate * 0.5)
        extra_pay = regular_pay + over_time_pay
    else:
        extra_pay = hours * rate
    return extra_pay    


string_hours = input("Enter Hours: ")
string_rate = input("Enter Rate: ")

try:
    float_hours = float(string_hours)
    float_rate = float(string_rate)
except:
    print('Error, please enter numric number')
    quit()

x = computepay(float_hours, float_rate)


print("Pay:", x)
