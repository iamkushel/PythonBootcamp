#tuples are immutable

tup = (1,1,2,4,2,4,3,1,3)
print(len(tup))
a = tup.count(100) #count the number of times a value appeas in the tuple
print(a)
#when you want to print  the number of times a number has repeated

a = set(tup)
for i in a:
        l = [i, tup.count(i)]
        print(l)

