dict = {'arun': 26, 'ramesh': 42, 'kushel': 25, 'sharath': 27}

print("Unsorted:", sorted(dict.items())) #unsorted dictionary
print("\nsorted by value: ", sorted(dict.items(), key = lambda x: x[1], reverse = True))
print("\nsorted by value: ", sorted(dict.items(), key = lambda x: -x[1]))#sortby value
print("\nsorted by value: ", sorted(dict.items(), key = lambda x: x[1]))
print("\nsorted by key:", sorted(dict.items(), key= lambda x:x[0])) #sort by key
print("\nsorted by len of key:", sorted(dict.items(), key = lambda x: len(x[0])))

