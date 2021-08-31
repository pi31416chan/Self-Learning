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

# Calculates the modulo of fraction a/d
def frac_mod(a,d,modular):
    product = d

    # for num in range(modular-3):
    #     product = (product * (d% modular)) % modular

    product = pow(product,modular-2,modular)

    product = (product * a) % modular

    return product