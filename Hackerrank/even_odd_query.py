import math

arr = [3, 2, 7, 3, 3, 2, 3, 8, 6, 1, 6, 0, 7, 1, 9, 1, 5, 0, 1, 4, 9, 6, 8, 2, 4, 6, 5, 3, 4, 7, 4, 7, 1, 4, 0, 4, 8, 3, 3, 4, 6, 1, 5, 5, 4, 6, 6, 9, 6, 7, 5, 6, 4, 3, 0, 5, 2, 5, 3, 8, 5, 0, 1, 6, 6, 7, 3, 4, 0, 4, 0, 3, 1, 5, 3, 5, 1, 1, 4, 0, 3, 1, 8, 5, 7, 8, 5, 1, 6, 0, 4, 1, 2, 4, 9, 0, 1, 4, 4, 3
]
queries = [
]
# queries = []
eo_list = []
gp_list = []


# Getting input
q = int(input("Input number of queries: "))

for query in range(q):
    queries.append(list(map(int,input().strip().split())))

# Determining the base number
for i,j in queries:
    # print(query)

    # base_num = arr[i-1]
    # print(base_num)

    # arr_sliced = arr[query[0]:query[1]]
    # print(arr_sliced)

    # Determining the gross power
    # gross_power = math.prod(arr_sliced)
    # print(gross_power)

    # if gross_power == 0:
    #     eo_list.append("Odd")

    # base_num_plus_one = arr[i]

    if i < len(arr) and arr[i] == 0 and i != j:
        eo_list.append("Odd")

    elif arr[i-1] % 2 == 0:
        # print("Even")
        eo_list.append("Even")

    else:
        # print("Odd")
        eo_list.append("Odd")

    # print()

print()
print(eo_list)
print(len(eo_list))