l = None
s = None
while True:
    sval= input("Enter a number: ")
    if sval =="done":
       break
    try:
       fval = int(sval)
    except ValueError:
       print("Invalid input")
    if l is None:
       l = fval
    if s is None:
       s = fval
    if fval > l:
       l = fval
    if fval < s:
       s = fval
print("Maximum is", l)
print("Minimum is" , s)
