hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("enter rate:")
r = float(rate)
if h > 40 :
    a = h - 40
    z = r*1.5
    b = a*z
    c = 40*r
    d = b+c
    print (d)
else :
    x = h*r
    print(x)
