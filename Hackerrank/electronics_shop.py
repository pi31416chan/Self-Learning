b = 10
keyboards = [3, 1]
drives = [5, 2, 8]

# keyboards = [5]
# drives = [4]



highest = 0



if min(keyboards) + min(drives) > b:
    print(-1)

else:
    keyboards.sort(reverse = True)
    drives.sort(reverse = True)
    print(keyboards,drives)

    for keyboard in keyboards:

        if keyboard + drives[0] <= highest:
            break

        for drive in drives:
            

            if (keyboard + drive) <= highest:
                break

            elif (keyboard + drive) > highest and (keyboard + drive) <= b:
                highest = (keyboard + drive)

    print(highest)