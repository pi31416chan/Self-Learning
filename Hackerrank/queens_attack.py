# Input
# n,k,r_q,c_q = 5,3,4,3
# obstacles = [
#             (5, 5),
#             (4, 2),
#             (2, 3),
#             ]

# n,k,r_q,c_q = 4,0,4,4
# obstacles = [
#             ]

# n,k,r_q,c_q = 1,0,1,1
# obstacles = [
#             ]

n,k,r_q,c_q = 100,100,48,81
obstacles = [
(54,87),
(64,97),
(42,75),
(32,65),
(42,87),
(32,97),
(54,75),
(64,65),
(48,87),
(48,75),
(54,81),
(42,81),
(45,17),
(14,24),
(35,15),
(95,64),
(63,87),
(25,72),
(71,38),
(96,97),
(16,30),
(60,34),
(31,67),
(26,82),
(20,93),
(81,38),
(51,94),
(75,41),
(79,84),
(79,65),
(76,80),
(52,87),
(81,54),
(89,52),
(20,31),
(10,41),
(32,73),
(83,98),
(87,61),
(82,52),
(80,64),
(82,46),
(49,21),
(73,86),
(37,70),
(43,12),
(94,28),
(10,93),
(52,25),
(50,61),
(52,68),
(52,23),
(60,91),
(79,17),
(93,82),
(12,18),
(75,64),
(69,69),
(94,74),
(61,61),
(46,57),
(67,45),
(96,64),
(83,89),
(58,87),
(76,53),
(79,21),
(94,70),
(16,10),
(50,82),
(92,20),
(40,51),
(49,28),
(51,82),
(35,16),
(15,86),
(78,89),
(41,98),
(70,46),
(79,79),
(24,40),
(91,13),
(59,73),
(35,32),
(40,31),
(14,31),
(71,35),
(96,18),
(27,39),
(28,38),
(41,36),
(31,63),
(52,48),
(81,25),
(49,90),
(32,65),
(25,45),
(63,94),
(89,50),
(43,41),
            ]




# Variables
queen_loc = (r_q,c_q)
corner_tl = (n,1)
corner_tr = (n,n)
corner_bl = (1,1)
corner_br = (1,n)
attack_range = {'t':0,
                'r':0,
                'b':0,
                'l':0,
                'tl':0,
                'tr':0,
                'bl':0,
                'br':0,}
block_deviation_tr = abs(queen_loc[1] - queen_loc[0])
block_deviation_tl = abs((n - queen_loc[1] + 1) - queen_loc[0])



'''Define an obstacle is useful or not'''
'''Determine direction of useful obstacle from queen's location'''
'''Calculates the absolute distance from queen to obstacle'''
def define_obs_useful(obstacle):
    temp_dist = y,x = (obstacle[0] - queen_loc[0],obstacle[1] - queen_loc[1])
    temp_direct = ''
    # print(temp_dist)

    if (abs(temp_dist[0]) == abs(temp_dist[1])) or (sum(temp_dist) == temp_dist[0]) or (sum(temp_dist) == temp_dist[1]):
        if temp_dist[0] > 0:
            temp_direct += 't'
        elif temp_dist[0] < 0:
            temp_direct += 'b'

        if temp_dist[1] > 0:
            temp_direct += 'r'
        elif temp_dist[1] < 0:
            temp_direct += 'l'

        if abs(y) > 0:
            return (True,temp_direct,abs(y))
        else:
            return (True,temp_direct,abs(x))

    else:
        return (False,None,None)



'''Calculation of queen attack range without obstacle'''
'''In eight directions'''
# Up-Down line
attack_range['t'] = n - queen_loc[0]
attack_range['b'] = n - attack_range['t'] - 1
# print(attack_range['t'],attack_range['b'])

# Left-Right line
attack_range['r'] = n - queen_loc[1]
attack_range['l'] = n - attack_range['r'] - 1
# print(attack_range['r'],attack_range['l'])

# Topright-Bottomleft line
if attack_range['t'] <= attack_range['r']:
    attack_range['tr'] = attack_range['t']
else:
    attack_range['tr'] = attack_range['r']
attack_range['bl'] = n - attack_range['tr'] - 1 - block_deviation_tr
# print(attack_range['tr'],attack_range['bl'])

# Topleft-Bottomright line
if attack_range['t'] <= attack_range['l']:
    attack_range['tl'] = attack_range['t']
else:
    attack_range['tl'] = attack_range['l']
attack_range['br'] = n - attack_range['tl'] - 1 - block_deviation_tl
# print(attack_range['tl'],attack_range['br'])
# print(sum(attack_range.values()))



'''Compare the useful obstacle with previous recorded obstacle'''
for obstacle in obstacles:
    obs_useful,obs_direct,abs_dist = define_obs_useful(obstacle)
    # print(obs_useful,obs_direct,abs_dist)

    if obs_useful == False:
        continue

    else:
        # print(obstacle,obs_direct,abs_dist)
        if abs_dist < attack_range[obs_direct]:
            attack_range[obs_direct] = abs_dist-1

print(sum(attack_range.values()))



