largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        x = int(num)
    except :
        print("Invaild input")
        continue

    if largest is None :
        largest = x
    elif x > largest :
            largest = x
    if smallest is None :
        smallest = x
    elif x < smallest :
        smallest = x

print("Maximum is", largest)
print("Minimum is", smallest)
