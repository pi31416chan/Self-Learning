n = 6
p = 5



    # Determines the number of flip from page 1
    if p % 2 == 0:
        from_1 = int((p + 1 - 1) // 2)
        print('1')
    else:
        from_1 = int((p - 1) // 2)
        print('2',from_1)

    # Determines the number of flip from last page
    if p % 2 == 0:
        from_last = int((n - p) // 2)
        print('3')
    else:
        from_last = int((n - (p - 1)) // 2)
        print('4',from_last)

    if from_1 < from_last:
        print(f"one {from_1}")
    else:
        print(f"last {from_last}")