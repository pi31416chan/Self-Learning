import math



n = 9
transmission = 3
acceptance = 2



n0 = 1
r = 2
cum_r = 2



for num in range(n - n0):
    r = math.floor(r * transmission / acceptance)
    cum_r += r

print(cum_r)