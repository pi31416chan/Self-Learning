n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
colors = {}



# Categorise all the socks into different color list
for sock in ar:

    if sock not in colors:
        colors[sock] = 1

    else:
        colors[sock] += 1

# Counting how many pairs are there in the sample
pairs = 0

for num_sock in colors.values():
    print(num_sock/2)
    pairs += num_sock//2

# pairs = int(pairs // 1)
    
print(pairs)