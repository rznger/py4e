hours=input("Enter Hours: ")
rate=input("Enter Rate: ")

try:

    hours=float(hours)
    rate=float(rate)

    if hours>40:
        pay=(hours-40)*1.5*rate+40*rate
        return pay
    else:
        pay=hours*rate
        return pay
    float(pay)

print("Pay: " + str(pay))
