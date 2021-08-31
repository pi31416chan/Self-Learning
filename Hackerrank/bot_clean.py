posr = 0
posc = 0
board = ['b---d',
        '-d--d',
        '--dd-',
        '--d--',
        '----d']



b_posi = [posr,posc]
d_count = 0
dirt_loc = []
distance = [0,0]

# Determine the dirt location
y = -1
for layer in board:
    y += 1
    x = -1
    for char in layer:
        x += 1
        if char == 'd':
            d_count += 1
            dirt_loc.append([y,x])



# For routing optimization, can add a dirt_loc rearranging algorithm here
# Can disable closest dirt determination if route optimization is added



# Getting the first dirt from dirt_loc list and get the direction towards it
# Checking if it is already landed on any dirt within the dirt_loc list
# If yes, will perform a CLEAN directly and remove the dirt from dirt_loc list


while dirt_loc:

    #Determines the closest dirt
    closest_dirt_loc = [0,0]
    closest_distance = 0
    for dirt in dirt_loc:
        if closest_dirt_loc == [0,0]:
            closest_dirt_loc = dirt
            closest_distance = (((dirt[0] - b_posi[0]) ** 2) + ((dirt[1] - b_posi[1]) ** 2))
        elif (((dirt[0] - b_posi[0]) ** 2) + ((dirt[1] - b_posi[1]) ** 2)) < closest_distance:
            closest_distance = (((dirt[0] - b_posi[0]) ** 2) + ((dirt[1] - b_posi[1]) ** 2))
            closest_dirt_loc = dirt

    # print(closest_dirt_loc)
    # print(closest_distance)
    # print(dirt_loc)
    dirt_loc.remove(closest_dirt_loc)
    dirt_loc.insert(0,closest_dirt_loc)
    # print(dirt_loc)
    # print()


    # Determines the distance from the first dirt
    distance[0] = dirt_loc[0][0] - b_posi[0]
    distance[1] = dirt_loc[0][1] - b_posi[1]

    # Determines the next direction to move
    # x-axis positive means going RIGHT
    # y-axis positive means going DOWN
    if b_posi in dirt_loc:
        dirt_loc.remove(b_posi)
        print('CLEAN')
    elif distance[0] > 0:
        b_posi[0] += 1
        print('DOWN')
    elif distance[0] < 0:
        b_posi[0] -= 1
        print('UP')
    elif distance[1] > 0:
        b_posi[1] += 1
        print('RIGHT')
    elif distance[1] < 0:
        b_posi[1] -= 1
        print('LEFT')

    # print()
# print(b_posi)
# print(dirt_loc)

