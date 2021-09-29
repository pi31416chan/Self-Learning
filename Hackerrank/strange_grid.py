r = 22
c = 1



import math
num = 0



# Determines row is divisible by 2
if r % 2 == 0:
    num += 1
    print(num)

# Determines row base number
# 10*ROUNDDOWN((K1-1)/2,0)
num += 10 * (math.floor((r-1)/2))
print(num)

# Determines column additional number
# (L1-1)*2
num += 2 * (c-1)
print(num)