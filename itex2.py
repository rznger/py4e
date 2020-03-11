num = 0
sum = 0
count = 0
list = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = float(num)
    except:
        print ("Invalid input")
        continue

    sum = (sum + num)
    count = (count + 1)
    ave = sum/count
    list.append (num)

print ("Sum: "+str(sum), "Count: "+str(count), "Min: "+str(min(list)), "Max: "+str(max(list)))
