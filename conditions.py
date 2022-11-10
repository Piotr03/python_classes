p = True
q = False

if p:
    print('p is True')
else:
    print('p is not True')

if not p:
    print('p is True')
else:
    print('p is not True')

print('---------------')

if p and q:
    print('p and q is True')
else:
    print('p and q is not True')

if p or q:
    print('p and q is True')
else:
    print('p or q is not True')

print('---------------')

v = None
if v:
    print(f'v={v}')
else: print('not v')

print('---------------')

# comparisons
w = 10
z = 11

if w >= z:
    print('w >= z')
else:
    print(print('not w >= z'))

if w == z:
    print('w = z')
else:
    print(print('w != z'))

y = 10 if w == 11 else 50
print(f'y={y}')