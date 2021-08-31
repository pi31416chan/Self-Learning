import itertools
from math import factorial as fact



# Calculates modulo of large number factorials
# returns the modulo of the end answer
def factorial_mod(n,modular):
    if n == 0:
        return 1
    else:
        fct_mod = (n * factorial_mod(n-1,modular)) % modular
        # print(fct)
        return fct_mod

# Calculates the modulo of fraction
def frac_mod(a,d,modular):
    product = d

    # for num in range(modular-3):
    #     product = (product * (d% modular)) % modular

    product = pow(product,modular-2,modular)

    product = (product * a) % modular

    return product



# list_a = '11001'
n = 522
m = 575
str_101 = ''



# str_101 = str_101.join(n * '1' + m * '0')

# # Processing
# mod_nm = fact(n+m-1) % (10**9+7)
# mod_n_m = (fact(n)*fact(m-1)) % (10**9+7)

# unique_permut = frac_mod(mod_nm,mod_n_m,10**9+7)

# print(unique_permut)

x = factorial_mod(int(970),int(1e9+7))
print(x)