l = 30
b = 42



def findDivisor(number):
    divisor = 0
    divisors = []

    while (divisor + 1) not in divisors:

        divisor += 1

        if number % divisor == 0:
            dividend = number / divisor
            dividend = int(str(dividend).replace('.0',''))
            if divisor == dividend:
                divisors.append(divisor)
            else:
                divisors.append(divisor)
                divisors.append(dividend)
            # print(divisors)

    divisors.sort()
    return divisors



def squareDetect(big,small):
    import math

    divisors_big = list(findDivisor(big))
    divisors_small = list(findDivisor(small))
    print(divisors_big)
    print(divisors_small)

    common_divisor = []

    for divisor in divisors_big:
        if divisor in divisors_small:
            common_divisor.append(divisor)

    # print(common_divisor)
    # common_divisor.sort(reverse = True)
    # print(common_divisor)

    bread_area = big * small

    square_count = bread_area / (max(common_divisor) ** 2)
    square_count = int(str(square_count).replace('.0',''))
    
    return square_count

    # i = -1
    # while -i <= len(common_divisor):

    #     if bread_area % (common_divisor[i] ** 2) == 0:
    #         square_count = bread_area / common_divisor



if l == b:
    print(1)

elif l > b:
    print(squareDetect(l,b))

elif l < b:
    print(squareDetect(b,l))
    