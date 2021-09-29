x = 1
y = 3
z = 2

output = ''

import math

if abs(x-z) < abs(y-z):
    output = 'Cat A'
elif abs(x-z) == abs(y-z):
    output = 'Mouse C'
else:
    output = 'Cat B'

print(output)