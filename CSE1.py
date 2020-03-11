hours=input("Enter Work Hours: ")
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
    print("ERROR, please input numeric data")
exit()
