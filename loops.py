# loop is used to run a code multiple times

for i in range(5):
    print(f'i={i}')

print('---------------')
v = 0
for i in range(5):
    print(f'i={i}')
    v = v + 1

print(f'v={v}')

print('---------------')
for i in range(1, 5):
    print(f'i={i}')

print('---------------')
for i in reversed(range(1, 10, 2)):
    print(f'i={i}')

print('---------------')
j = 0
while j < 7:
    j += 1
    print(f'j={j}')
# without j += 1 we would have an ifinite loop

print('---------------')
j = 0
while j < 7:
    j += 1
    if j == 3:
        continue
    if j == 5:
        break
    print(f'j={j}')

print('---------------')
