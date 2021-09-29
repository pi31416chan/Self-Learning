# s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
s = [[4, 8, 2],
[4, 5, 7],
[6, 1, 6]]



# List of all possible magic square
magic_sq = [[8,1,6,3,5,7,4,9,2],
            [6,1,8,7,5,3,2,9,4],
            [4,9,2,3,5,7,8,1,6],
            [2,9,4,7,5,3,6,1,8],
            [8,3,4,1,5,9,6,7,2],
            [4,3,8,9,5,1,2,7,6],
            [6,7,2,1,5,9,8,3,4],
            [2,7,6,9,5,1,4,3,8]]

# converting input list into one list
input_sq = []

for layer in s:
    for unit in layer:
        input_sq.append(unit)

# print(input_sq)

# getting difference between input list and all magic square

lowest_diff = 0

if input_sq in magic_sq:
    print(0)

else:
    for sq in magic_sq:
        difference = []
        for n in range(9):
            diff = abs(input_sq[n] - sq[n])
            difference.append(diff)

        # print(difference)
        if lowest_diff == 0:
            lowest_diff = sum(difference)
            # print(lowest_diff)

        elif sum(difference) < lowest_diff:
            lowest_diff = sum(difference)
            # print(lowest_diff)

print(lowest_diff)