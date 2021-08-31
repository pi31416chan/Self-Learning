import math

c = [0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0
]

step = 0
ignore = []
i = -1
bad_cloud = 0

min_jump = int(math.ceil((len(c)-1)/2))

# True = Even, False = Odd
even_jump = True

for cloud in c:
    i += 1

    if (even_jump == True) and (i % 2 == 0) and (cloud == 1):
        even_jump = False
        bad_cloud += 1
        # step += 1

    elif (even_jump == False) and (i % 2 == 1) and (cloud == 1):
        even_jump = True
        bad_cloud += 1
        # step += 1
    # print(i,bad_cloud)
    # elif i % 2 == 0:
    #     step += 1

# if c[-2] == 1:
print(int(math.floor(bad_cloud/2) + min_jump))
# else:
#     print(bad_cloud + min_jump)