a = [1,2,3,4,5,6,7]
k = 2
querries = [0,1,2]

querries_answer = []
k = k % len(a)

# slice_a = a[:len(a)-k]
# print(slice_a)
# rev_a = a[-k:]
# print(rev_a)

final_list = a[-k:] + a[:len(a)-k]
print(final_list)

for index in querries:
    querries_answer.append(final_list[index])

print(querries_answer)