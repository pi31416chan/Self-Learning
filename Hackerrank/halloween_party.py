k = 7



k_half = int(k/2)

if k % 2 == 1:
    k_half += k_half**2

elif k % 2 == 0:
    k_half = k_half**2

print(k_half)