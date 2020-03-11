hours=input("Enter Work Hours: ")
try:
    hours=float(hours)
except:
    print("ERROR, please enter numeric input.")
    exit()
rate=input("Enter Rate: ")

try:
    hours=float(hours)
    rate=float(rate)

    if hours<=40:
        pay=hours*rate
    if hours>40:
        pay=(hours-40)*1.5*rate+40*rate

    print("Your Pay is: " + str(pay))

except:
    print("ERROR, please enter numeric input.")
exit()
