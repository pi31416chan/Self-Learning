i = 20
j = 23
k = 6
beu_day = 0



for number in range(i,j+1):
    rev_number = str(number)[::-1]
    # print(int(rev_number))
    mod_diff = abs((number % k) - (int(rev_number) % k))

    if mod_diff == 0:
        beu_day += 1

print(beu_day)