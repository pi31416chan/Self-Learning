import itertools

# multiple_input = input().rstrip().split()

string = 'HACK'
digit = 2

# string = str(multiple_input[0])
# digit = int(multiple_input[1])

sorted_string = []
for char in string:
    sorted_string.append(char)

sorted_string.sort()
# print(''.join(sorted_string))

k = list(itertools.permutations(sorted_string,digit))

for combi in k:
    print(''.join(combi))
