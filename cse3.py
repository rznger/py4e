score=input("Enter Score: ")

def compute(score):

    try:
        score=float(score)

        if score>1.0:
            print("Bad Score")

        elif score>=0.9:
            print("A")
        elif score>=0.8:
            print("B")
        elif score>=0.7:
            print("C")
        elif score>=0.6:
            print("D")
        elif score<0.6:
            print("F")

    except:
        print("Bad Score")

print=compute(score)
exit()
