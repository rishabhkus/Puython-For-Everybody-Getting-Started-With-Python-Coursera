smallest = None
largest = None
while True:
    a=input("Enter the Number: ")
    if a=="done":
        break
    try:
        b=int(a)
    except:
        print("Invalid input")
    if smallest is None:
        smallest = b
    if largest is None:
        largest = b
    if b > largest :
        largest = b
    elif b < smallest :
        smallest = b
print(largest)
print(smallest)
