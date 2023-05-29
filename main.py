while (True):
    a = input("введите выражение").split()
    x = int(a[0])
    y = a[1]
    z = int(a[2])
    if y == "+": 
        print(x+z)
    elif y == "-":
        print(x-z)
    elif y == "*":
        print(x*z)
    elif y == "/":
        print(x/z)



