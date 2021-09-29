posts = [1,4,1]

pole_1 = []
pole_2 = []
pole_3 = []
pole_4 = []
poles = [pole_1,pole_2,pole_3,pole_4]

i_disk = 1

for post in posts:
    poles[post-1].append(i_disk)
    i_disk += 1

pole_1.sort(reverse = True)
pole_2.sort(reverse = True)
pole_3.sort(reverse = True)
pole_4.sort(reverse = True)

print(pole_1,pole_2,pole_3,pole_4)
print()
