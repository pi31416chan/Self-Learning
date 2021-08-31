n = 1012



# Divisor list
divisors = [1]

# Pre-determining of divisors of single digit numbers
# 8 and 9 are tested separately to skip 2,3, and 4
divisor_samples = [2,3,4,5,6,7,8,9]

for sample in divisor_samples:
    if n % sample == 0:
        divisors.append(sample)

# Splitting to each digit number
digit_list = list(str(n))
# print(digit_list)
count = 0

for digit in digit_list:
    if int(digit) in divisors:
        count += 1

print(count)