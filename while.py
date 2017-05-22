i =0
while i < 10:
    i = i+1
    if(i==5):
        continue
    print(i)
j=0
while j < 10:
    j = j+1
    if(j==5):
        break
    print(j)
k=0
while k < 10:
    k = k+1
    if(k==5):
        pass
    print(k)
l =  [i for i in 'name']
print(l)

print([x**2 for x in range(0,10)])

c = [20,34,37.4, -40]
fa = [temp*(9/5.0) + 32 for temp in c]
print(fa)
