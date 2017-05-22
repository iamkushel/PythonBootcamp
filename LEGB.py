x = 50 #global declaration

def sum():
    x = 2
    print(x)
sum()
print(x)
#when you use global insie a function you are changing the value of the varibale globally
def sum():
    global x
    x = 2
    print(x)
sum()
print(x)

print(globals())
print(locals())
