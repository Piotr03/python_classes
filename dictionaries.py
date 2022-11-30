d1 = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March'}
print(d1)
#adding new value to the key will replace the value
d1 = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Jan': 'Styczen'}
print(d1)

print(d1['Feb'])
d1['Apr'] = 'April'
print(d1)
d1['Apr'] = 'Aprilo'
print(d1)
print('---------------')
for k in d1.keys():
    print(f'{k}: {d1[k]}')
    #in a format where k is printed as value of key
print('---------------')