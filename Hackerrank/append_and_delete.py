s = 'abcd'
t = 'abcdert'
k = 10

# Processing
s = list(s)
t = list(t)

# Determine the common character from the left
i = -1
count = 0

for char in s:
    i += 1

    if i == len(t)-1:
        break

    elif char == t[i]:
        count += 1

    else:
        break

# Calculates the character to remove
removal_count = len(s) - count
# print(removal_count)

# Calculates the character to add
addition_count = len(t) - count
# print(addition_count)

move = removal_count + addition_count
# print(move)

if move <= k and ((k-move)%2) == 0:
    print( "Yes")

elif move <= k and (removal_count + 2*len(s) + addition_count) <= k:
    print("Yes")

else:
    print( "No")