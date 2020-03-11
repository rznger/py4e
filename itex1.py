sum = 0
count = 0
num = 0

while True:
    num = input("Enter a number: ")
    if num =="done":
        break

    try:
        num = float(num)

    except:
            print("Invalid input")
            continue
    sum = (sum + num)
    count = (count + 1)
    ave = sum/count

print("Sum: "+str(sum), "Count: "+str(count), "Average: "+str(ave))
        
