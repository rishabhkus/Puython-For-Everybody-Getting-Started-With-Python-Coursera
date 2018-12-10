score = input("Enter Score: ")
b = float(score)
if b > 1:
    print ("error")
elif b >= 0.9 :
    print ("A")
elif b >= 0.8 :
    print ("B")
elif b >= 0.7 :
    print ("C")
elif b >= 0.6 :
    print ("D")
elif b < 0.6 :
    print ("F")
