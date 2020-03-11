hours=input("Enter Work Hours: ")
try:
    hours=float(hours)
except:
    print("Please input numeric data.")
    exit()

rate=input("Enter Rate: ")
try:
    rate=float(rate)
except:
    print("Please input numeric data.")
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
