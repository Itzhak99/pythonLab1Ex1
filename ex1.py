from random import randint

def func1(number):
    for i in range(number):
        var = randint(0,256)
        print(f'{var+3:b}')

def func2():
    number = input("Enter a number:")
    v = set()
    for char in number:
        if char.isdigit():
            v.add(int(char))
    return v

def func3():
    print("hello")

def func4():
    v = []
    while True:
        try:
            x = int(input("Enter a positive number (or a non-positive number to stop): "))
            if x <= 0:
                break
            v.append(x)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    print("List/Array has finished receiving numbers")
    return v

def func5():
    v = func4()
    v.sort()
    res = sum(v,0)
    v_max = max(v)
    v_min = min(v)
    v.clear()
    v.append(v_min)
    v.append(res)
    v.append(v_max)
    return v

def func6():
    a = func4()
    b = func4()
    c = []
    if a.__len__() != b.__len__():
        print("Invalid input. arrays should have the same size.")
        return a,b
    for i in range(a.__len__()):
        for j in range(b[i]):
            c.append(a[i])
    print("Final Result:")
    return c

def func7():
    pass

def func8():
    v = []
    for i in range(1000):
        x = randint(1,10)
        v.append(x)
    return v

print(func6())