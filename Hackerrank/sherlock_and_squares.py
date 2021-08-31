import math

a = 17
b = 49



# Determining the starting root number
start_num = int(math.sqrt(a))
test_num = start_num
count = 0

while True:
    # print(test_num)

    if test_num ** 2 < a:
        test_num += 1
        continue

    elif test_num ** 2 > b:
        break

    else:
        count += 1
        test_num += 1

print(count)


