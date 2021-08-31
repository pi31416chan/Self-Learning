# n = 715950220 
# m = 876882456 
# s = 195550680


while True:
    input_list = input().strip().split()

    # print(input_list)

    n = int(input_list[0])
    m = int(input_list[1])
    s = int(input_list[2])

    # print(n,m,s)

    remainder = m % n
        
    last_person = ((s - 1) + remainder) % n

    if last_person == 0:
        last_person = n

    print()
    print(last_person)