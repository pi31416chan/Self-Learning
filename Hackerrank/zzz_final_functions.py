# Find the divisor
# Enter any number to show a list of its all divisors
# Output in list format
def findDivisor(number):
    import math
    divisor = 0
    divisors = []

    while (divisor + 1) <= int(math.sqrt(number)):

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



# Single target counter
# countee = any number or string to be counted from the sample
# sample = the large sample that the countee is counted from
# Output in number format
def singleCounter(countee,sample):
    count_result = 0

    for item in sample:
        if item == countee:
            count_result += 1
    
    return count_result



# Multi target counter without target
# Default counts all elements from the given list of numbers
# ONLY numbers are supported, otherwise cannot control the correct sequence
# Significantly faster counttime in extremely large sample size
# Output in list format
def multiCounterNoTarget(sample):
    count_result = [0] * 5

    for num in sample:
        count_result[num-1] += 1

    return count_result



# Multi target counter with specified targets
# countee_range = list of numbers or items to be counted
# sample = the large sample where items are counted from
# output in dictionaries format
def multiCounterWithTarget(countee_range,sample):
    count_result = {}

    for item in countee_range:
        count_result[item] = 0

    for num in sample:
        if num in countee_range:
            count_result[num] += 1
    
    return count_result



# Unique list generator
def uniqueList(sample):
    unique_list = []

    for item in sample:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

