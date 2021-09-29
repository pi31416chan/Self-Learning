n = 12



divisors = []
divisor = 0
digit_sums = []
digit_sum = 0
winner = 0
winner_digit_sum = 0
i = 0



# Find the divisor
if n == 1:
    winner = 1

else:

    while (divisor + 1) not in divisors:

        divisor += 1

        if n % divisor == 0:
            dividend = n / divisor
            dividend = int(str(dividend).replace('.0',''))
            if divisor == dividend:
                divisors.append(divisor)
            else:
                divisors.append(divisor)
                divisors.append(dividend)
            # print(divisors)

    divisors.sort()
    # print(divisors)
    # print()


    # Determines the digits sum
    for num in divisors:
        if num % 10 == num:
            digit_sum = num
            digit_sums.append(digit_sum)
            # print(digit_sums)

        else:
            temp = []
            for digit in list(str(num)):
                temp.append(int(digit))
                # print(temp)
            digit_sum = sum(temp)
            digit_sums.append(digit_sum)

        if digit_sum > winner_digit_sum:
            winner = num
            winner_digit_sum = digit_sum
            # print(winner)
        # elif digit_sum < winner_digit_sum:
            # print("No Change")
        elif digit_sum == digit_sums[i-1]:
            if num < winner:
                winner = num
                winner_digit_sum = digit_sum
                # print(winner)
            # else:
            #     print("No Change")

# print()
print(winner)
