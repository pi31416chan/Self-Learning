# arr = [5, 4, 4, 2, 2, 8]
arr = [1, 2, 3, 4, 3, 3, 2, 1]


# Processing
arr.sort(reverse=True)
print(arr)

# Counting
rem_sticks_list = []
rem_sticks = 0
temp = 0
i = -1

for num in arr:
    i += 1

    if i == 0:
        temp += 1

    elif num == arr[i-1]:
        temp += 1

    else:
        rem_sticks += temp
        rem_sticks_list.insert(0,rem_sticks)
        temp = 1

else:
    rem_sticks += temp
    rem_sticks_list.insert(0,rem_sticks)

print(rem_sticks_list)
