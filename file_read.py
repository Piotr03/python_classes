my_file = 'hello'
#approach 1
# f = open(my_file, 'r')
# #r for reading w for writing
# lines = f.readlines()
# i = 0
# for line in lines:
#     i+=1
#     print(f'{i}: {line}', end='')
# f.close()

#approach 2
with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')


print(-------------)

#approach 3 - reading txt file line by line
with open(my_file, 'r') as f:
    i = 0
    while line:=f.readline()
        i += 1
        print(f'{i}: {line}', end='')