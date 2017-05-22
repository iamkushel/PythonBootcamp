l = [1,1,2,2,3,3,4,4,1,3,4,5,2,4,1,2,4,5]
a = set(l)
a.add(6)
print(a)
if len(a) == len(l):
    print("No dups")
else:
    print("Dups are present")
a.clear()
print(a)
