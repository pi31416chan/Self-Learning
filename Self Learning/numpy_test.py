import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)



# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('2nd element on 1st dim: ', arr[0, 1])



# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print(arr[0, 1, 2])



# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print('Last element from 2nd dim: ', arr[1, -1])



# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[-3:-1])
# print(arr)



# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5:2])



# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[::2])



# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[1, 1:4])
# print(arr)



# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[:, 1:4])
# print(arr.dtype)



# arr = np.array([1, 2, 3, 4])

# print(arr.dtype)



# arr = np.array(['apple', 'banana', 'cherry'])

# print(arr.dtype)



# arr = np.array([1, 2, 3, 4], dtype='S')

# print(arr)
# print(arr.dtype)



# arr = np.array([1, 2, 3, 4], dtype='i4')

# print(arr)
# print(arr.dtype)



# arr = np.array([1.1, 2.1, 3.1])

# newarr = arr.astype('i')

# print(newarr)
# print(newarr.dtype)



# arr = np.array([1, 0, 3])

# newarr = arr.astype(bool)

# print(newarr)
# print(newarr.dtype)



# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(4, 3)

# # print(newarr)

# arr_3d = np.array([newarr,newarr.copy()])
# print(arr_3d)
# print()
# print(arr_3d[0,3],arr_3d[1,1,2])



# arr = np.array([1, 2, 3])

# x=np.ndenumerate(arr)
# print(list(x))





# sns.distplot([0, 1, 2, 3, 4, 5], hist=True)

# plt.show()



# sns.distplot(np.random.normal(10,size=100), hist=False)

# plt.show()

# sns.distplot(np.random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
# sns.distplot(np.random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
# sns.distplot(np.random.poisson(lam=2, size=100), kde=False)
# sns.distplot(np.random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
# sns.distplot(np.random.poisson(lam=10, size=1000), hist=False, label='poisson')
# sns.distplot([4, 1, 4, 1, 2, 1, 1, 3, 3, 2])

# plt.show()
# print(sum([4, 1, 4, 1, 2, 1, 1, 3, 3, 2])/10)


print(np.info(np.random.randn))


# x = np.array([-np.inf, 0., np.inf])
# y = np.array([2, 2, 2])
# print(x,y)
# np.isposinf(x, y)
# print(x,y)



# array=np.zeros(10)
# print("An array of 10 zeros:")
# print(array)
# array=np.ones(10)
# print("An array of 10 ones:")
# print(array)
# array *= 5
# print("An array of 10 fives:")
# print(array)