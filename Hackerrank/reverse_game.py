n = 3
k = 1

# Determine k belongs to left or right half
import math
half_point = math.floor(n/2)

print(half_point)

if k >= half_point:
    pos = 2 * (n - 1 - k)
elif k < half_point:
    pos = 1 + (2 * k)

print(pos)