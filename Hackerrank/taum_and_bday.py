# Input
b = 7
w = 7
bc = 4
wc = 2
z = 1



# Variables
bc_low = 0
wc_low = 0
min_cost = 0



# Determining lowest cost of b
bc_low = min(bc,wc+z)
print(bc_low)



# Determining lowest cost of w
wc_low = min(wc,bc+z)
print(wc_low)



# Calculating total minimum cost
min_cost = b*bc_low + w*wc_low
print(min_cost)