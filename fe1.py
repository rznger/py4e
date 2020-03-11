hours=input("Enter Work Hours: ")
try:
    hours=float(hours)
except:
    print("ERROR, please enter numeric input.")
    exit()

rate=input("Enter Rate: ")
try:
    rate=float(rate)
except:
    print("ERROR, please enter numeric input.")
    exit()

def computepay(hours, rate):
    if hours>40:
        pay=(hours-40)*1.5*rate+40*rate
        return pay
    else:
        pay=hours*rate
        return pay

x=computepay(hours, rate)
print("Your Pay is: " + str(x))
