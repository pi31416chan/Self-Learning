import math



n = 8



def findDivisor(number):
    divisor = 0
    divisors = []
    last_dividend = number
    count = 0

    while (divisor + 1) <= int(math.sqrt(number)):

        divisor += 1

        if number % divisor == 0:
            # dividend = number / divisor
            # dividend = int(str(dividend).replace('.0',''))
            # last_dividend = dividend
            last_dividend = number / divisor
            if divisor == last_dividend and divisor % 2 == 0:
                # divisors.append(divisor)
                count += 1
                break
            else:
                if divisor % 2 == 0:
                    # divisors.append(divisor)
                    count += 1
                if last_dividend % 2 == 0:
                    # divisors.append(last_dividend)
                    count += 1
            # print(divisors)
            # print(last_dividend)

    # divisors.sort()
    # return divisors
    return count
    # print(count)



# count = 0
divisors = findDivisor(n)
print(divisors)

# for divisor in divisors:
#     if divisor % 2 == 0:
#         count += 1

# print(len(divisors))
# print(divisors)