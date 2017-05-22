for i in range(1,11):
    if i%2 == 0:
        print("even :",i)

#list comprehensions

l = [i for i in range(0,100,10)]
print(l)

#sum of mus in the list
z =0
for i in l:
    z +=i
print(z)
###########IMPORTANT#######################IMPORTANT#############IMPORTANT##########################################################
lst = [(1,2),(2,3),(4,5),(9,20)]

for (item1,item2) in lst:
    print(item1, item2)
else:
    print("here is your list!!!!!!!!!!!!!!!!!!!!!")

#to traverse a dict through a for loop
dict = {'CA': 'California', 'WY': 'Wyoming', 'NY': 'New York', 12: 'Kushel', 3:'Dooks'}
for (k,v) in dict.items():
    print(v)
