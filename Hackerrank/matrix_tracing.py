import itertools
from math import factorial as fact



# Calculates modulo of large number factorials
# returns the modulo of the end answer
def factorial_mod(n,modular):
    product = 1
    temp = 1
    while n > temp:
        temp += 1
        product = (product * (temp % modular)) % modular

    return product




# Calculates the modulo of fraction
def frac_mod(a,d,modular):
    product = d

    # for num in range(modular-3):
    #     product = (product * (d% modular)) % modular

    product = pow(product,modular-2,modular)

    product = (product * a) % modular

    return product



m = 1012
n = 1208



mn_a_mod = factorial_mod(m+n-2,10**9+7)
m_d_mod = factorial_mod(m-1,10**9+7)
n_d_mod = factorial_mod(n-1,10**9+7)
mn_d_mod = (m_d_mod * n_d_mod) % (10**9+7)

# print(mn_a_mod,mn_d_mod)

combi = frac_mod(mn_a_mod,mn_d_mod,10**9+7)

print(combi)

# x = factorial_mod(13,10**9+7)
# print(x)