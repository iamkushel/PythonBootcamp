def square(num):
    num= num*num
    return print(num)

def square1(num):
    return print(num*num)
square(8)
square1(8)

def square2(num): return print(num*num)
square2(5)

square3 = lambda num: num*num
print(square3(4))

string = "Kushel"
rev = lambda x : x[::-1]
print(rev(string))
