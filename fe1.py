hours=input("Enter Work Hours: ")
hours=float(hours)

rate=input("Enter Rate: ")
rate=float(rate)


def computepay(hours, rate):
    if hours>40:
        pay=(hours-40)*1.5*rate+40*rate
        return pay
    else:
        pay=hours*rate
        return pay

x=computepay(hours, rate)
print("Your Pay is: " + str(x))
