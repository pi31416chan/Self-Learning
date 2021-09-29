import numpy as np
import time
# from timeit import timeit
# from numpy.random import random as random_np
# from random import random as random_py

# def change_title(string):
#     return string.title()

# def batch_func(list,f):
#     return [f(string) for string in list]

# s = ['cxw','niama','sifat','aXa','pi31416chan']

# print(batch_func(s,change_title))



# def f(a=[1,2,3,4,5],b=[10,20,30,40,50]):
#     c = [i*j for i,j in zip(a,b)]
#     return c

# def g(a=np.array([1,2,3,4,5]),b=np.array([10,20,30,40,50])):
#     c = a*b
#     return c



# t1 = [1,2,3,4,5] * 100
# t2 = [10,20,30,40,50] * 100
# t3 = np.array(t1)
# t4 = np.array(t2)
# f(t1,t2)
# g(t3,t4)



# def d():
#     a = range(100000)
#     b =range(0,1000000,10)
#     c = [i*j for i,j in zip(a,b)]
#     return c

# def e():
#     a = np.array(range(100000))
#     b =np.array(range(0,1000000,10))
#     c = a*b
#     return c

# d()
# e()

#python ['0.04s', '0.04s', '0.04s']
#numpy ['0.02s', '0.02s', '0.02s']



# n_runs = 10000000
# t_builtin = timeit(random_py, number=n_runs)
# t_numpy = timeit(random_np, number=n_runs)

# print(f"Built-in random:\t{t_builtin}s")
# print(f"NumPy random:   \t{t_numpy}s")


# size = 1000
# n_runs = 10000
# t_builtin_list = timeit(
#     "[random_py() for _ in range(size)]",
#     setup=f"from random import random as random_py; size={size}",
#     number=n_runs
# )
# t_numpy_array = timeit(
#     "random_np(size)",
#     setup=f"from numpy.random import random as random_np; size={size}",
#     number=n_runs
# )

# print(f"Built-in random with lists:\t{t_builtin_list}s")
# print(f"NumPy random with arrays:  \t{t_numpy_array}s")



# import numpy as np

# my_arr = np.arange(1000000)

# my_list = list(range(1000000))

# for _ in range(10): my_arr2 = my_arr * 2

# for _ in range(10): my_list2 = [x * 2 for x in my_list]


# x = np.eye(7,dtype='int64')
# y = x.astype('bool')
# print(x,'\n'*2,y)
# print("X dim:",x.ndim,"Y dim:",y.ndim)



arr = np.array([[1., 2., 3.], [4., 5., 6.]])

arr2 = arr[0] + arr[1]

x = arr2 > arr

print(x.dtype)