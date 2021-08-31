arr_a = [3,2,7,4]

# q = [1,2]
q = [1,3]



import math


# Processing
mod_temp = arr_a[q[0]-1] % 2
arr_slice = arr_a[q[0]-1:q[1]]

print(mod_temp)
print(arr_slice)

gross_power = math.prod(arr_slice)

mod_temp = pow(mod_temp,gross_power,2)

print(mod_temp)