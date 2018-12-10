def computepay(h,r):
    a=h-40
    b=a*(r*1.5)
    c=40*r
    p=b+c
    return p
hrs = input("Enter Hours:")
rate = input ("Enter Rate:")
h=float(hrs)
r=float(rate)
if h > 40:
    p = computepay(h,r)
else:
    p=h*r
print(p)
