temp = [20,30,25,67]

z = map(lambda x: x*2, temp) #you dont need to call the function here coz the temp will be given as input to lambda
print(list(z))

f  = map(lambda T: (9/5)*T +32, temp)

print(list(f))
b = [42,12,45,66]
m = zip(temp,b)
x = map(lambda pair: max(pair), m)
print(list(x))
