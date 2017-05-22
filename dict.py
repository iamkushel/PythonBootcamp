dict = {'CA': 'California', 'WY': 'Wyoming', 'NY': 'New York', 12: 'Kushel', 3:'Dooks'}




print(dict.keys())
print(dict.values())
print(dict.items())
k = list(dict.values())
print(k.sort())

#to perform anything on to the values first you need to give the
print(dict['CA'][0])

print('\n\n\n')
#nested Dicts

nd = {'k1': [1,2,{'k2':['this is tricky',{'toughie': [1,2,['hello']]}]}]}

print(nd['k1'][2]['k2'][1]['toughie'][2])
