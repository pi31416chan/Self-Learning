a = [66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
     66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
     66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
     66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
     66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,
     66,66,66,66,66

     ]

def multiCounterWithTarget(countee_range,sample):
    count_result = {}

    for item in countee_range:
        count_result[item] = 0

    for num in sample:
        if num in countee_range:
            count_result[num] += 1
    
    return count_result

def uniqueList(sample):
    unique_list = []

    for item in sample:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


countee_range = uniqueList(a)
countee_range.sort()
counts = multiCounterWithTarget(countee_range,a)
length = 0
max_length = 0
print(countee_range)
print(counts)
# print(countee_range[3])
# print(counts[countee_range[2]])

i = -1
for key, count in counts.items():
    
    if i+2 < len(countee_range):
        i += 1
        # print(i)
        if countee_range[i+1] - key <= 1:
            length = count + counts[countee_range[i+1]]
            if length > max_length:
                max_length = length
                # print('lll',max_length)
                # print()

if max_length == 0:
    max_length = max(counts.values())
# print()
print(max_length)