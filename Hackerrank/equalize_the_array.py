# Input
arr = [3, 3, 2, 1, 3]



# Variables
count_dict = {}
min_del = 0



'''counting the number of each non-repeated element inside the array'''
for elem in arr:

    if elem not in count_dict:
        count_dict[elem] = 1
    elif elem in count_dict:
        count_dict[elem] += 1

min_del = sum(count_dict.values()) - max(count_dict.values())
print(min_del)