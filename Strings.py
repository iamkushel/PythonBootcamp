import re
a = "kushel is awesome"
b = [10]
b[0] = 1
print(b)

print(a[0])

print(a[-3:])

print(a[:-3]) #when - is used moves to last so and -3 indicates move to third position from last, so this will print from first till 3rd position from last
print(a[::2]) #skips one character and prints #output: Kse saeoe
print(a[::-2]) #skips a character nd prints from back #output: eoeas esK

z = "nitin"
p = z[::1]
if p == z:
    print('It is palindrome')


# to change a string you need to convert it list first

new_list = list(a)
new_list[0] = 'z'
new_list = ''.join(new_list)
print(new_list)
new_list = ':'.join(new_list)
print(new_list)

if a.islower():
    print("True")
else:
    print("false")

print(a.split(' '))

