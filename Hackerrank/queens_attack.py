# Input
n,k,r_q,c_q = 5,3,4,3
obstacles = [
            (5, 5),
            (4, 2),
            (2, 3),
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
temp_diff = 0
i = -1
for coor in queen_loc:
    i += 1
    if (corner_tr[i] - coor) < temp_diff or temp_diff == 0:
        temp_diff = corner_tr[i] - coor

attack_range['tr'] = temp_diff
attack_range['bl'] = n - attack_range['tr'] - 1???????????????
print(attack_range['tr'],attack_range['bl'])