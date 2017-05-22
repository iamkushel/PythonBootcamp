my_list = [0,1,2,3,4,5,6, "Kushel", "Dooks"]

print(my_list[::-1])

new_list = ["live", "laugh", "love"]

my_list = my_list + new_list + ['Forever', 12*3]

print(my_list)

my_list.append(new_list)
print(my_list)
print(my_list[-1:])

new_list.sort()
print(new_list)

m = [1,2,3]
n = [4,5,6]
o = [7,8,9]

matrix = [m, n, o]
print(matrix)
print(matrix[0][2])
print(m.index(3)) #it will return which position the particular value is 3 is at index 2
