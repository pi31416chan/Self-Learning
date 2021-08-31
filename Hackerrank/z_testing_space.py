# import itertools
import math



def factorial_mod(n,modular):
    if n == 0:
        return 1
    else:
        fct_mod = (n * factorial_mod(n-1,modular)) % modular
        # print(fct)
        return fct_mod

def pow_mod(a,n,modular):
    product = a

    for num in range(n-1):
        product = (product * a) % modular

    return product

def inv_mod(d,modular):
    product = d

    for num in range(modular-3):
        product = (product * d) % modular

    return product

def frac_mod(a,d,modular):
    product = d

    for num in range(modular-3):
        product = (product * d) % modular

    product = (product * a) % modular

    return product

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

