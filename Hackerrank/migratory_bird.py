n = 11
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
# counts = []
winner = 0
winner_count = 0

# print(len(arr))

def multiCounterWithTarget2(countee_range,sample):
    count_result = {}

    for item in countee_range:
        count_result[item] = 0
    print(count_result)
    
    i = -1

    for num in sample:
        i += 1
        if num in countee_range:
            count_result[num] += 1
    print(count_result)
    
    return count_result



countee_range = [value for value in range(1,6)]

counts = multiCounterWithTarget2(countee_range,arr)


for countee,count in counts.items():

    if count > winner_count:
        winner = countee
        winner_count = count
        # print(winner)

print(winner)



# Approach B
# counts = [0] * 5

# for num in arr:
#     counts[num-1] += 1

# i = 0
# for count in counts:
#     i += 1
#     if count > winner_count:
#         winner = i
#         winner_count = count
#         # print(winner)

# print(winner)