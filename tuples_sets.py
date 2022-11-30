t1 = (1413, 254346)
t2 = (2, 4, 6, 7)
print(t1[1])
print(t2[3])
# TUPLES ARE READ ONLY, IMMUTABLE, NOT POSSIBLE TO CHANGE, IF I WOULD DO
# t1[1] = 24 it would generate error

#but we can create subtuples:
t3 = t2[1:3]
print(t3)


print ('---------------')
l4 = [321, 26, 23163, 3267, 89, 26, 3267, 89]
print(l4)
s1 = set(l4)
print(s1)
print ('---------------')
#set is unordered, list is, duplicates are removed - unique values only
#not possible to adress the element of list, so e.g. print(s1[3])
for el in s1:
    print(el)

l5 = list(s1)
print(l5)