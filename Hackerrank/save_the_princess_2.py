n = 5

r = 3
c = 4

grid = ['-----',
        '-----',
        '----p',
        '----m',
        '-----']

bot_posi = [c,r]
p_posi = []
next_move = ""

# Get princess position
# The location follow top negative bottom positive, left negative right positive
for y in range(n):
    if 'p' in grid[y]:
        x = 0
        for char in grid[y]:
            if char != 'p':
                x += 1
            elif char == 'p':
                p_posi.append(x)
                p_posi.append(y)
                print(bot_posi)
                print(p_posi)
                break

distance = [p_posi[0] - bot_posi[0],p_posi[1] - bot_posi[1]]
print(distance)

# Determines the next move LEFT or RIGHT
if distance[0] < 0:
    next_move = 'LEFT'
elif distance[0] > 0:
    next_move = 'RIGHT'
elif distance[0] == 0:
    if distance[1] < 0:
        next_move = 'UP'
    elif distance[1] > 0:
        next_move = 'DOWN'

print(next_move)