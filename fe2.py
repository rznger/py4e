def computegrade(score):

    try:
        score=float(score)
        if score>1.0:
            return("Data not in range.")
        elif score>=0.9:
            return("A")
        elif score>=0.8:
            return("B")
        elif score>=0.7:
            return("C")
        elif score>=0.6:
            return("D")
        elif score<0.6:
            return("F")
    
        else:
            return("Data not in range.")
    except:
        return("Data not in range.")

print(computegrade(input("Enter Score: ")))
