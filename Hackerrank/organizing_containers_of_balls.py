# Input
container =[
[997612619,934920795,998879231,999926463],
[960369681,997828120,999792735,979622676],
[999013654,998634077,997988323,958769423],
[997409523,999301350,940952923,993020546],
]


# Variables
container_cap = []
ball_count = []
n = len(container[0])



# Calculating containers' capacities
for cont in container:
    container_cap.append(sum(cont))

container_cap.sort()
# print(container_cap)



# Calculating balls' count
for i in range(n):
    temp_count = 0

    for j in range(n):
        temp_count += container[j][i]

    ball_count.append(temp_count)

ball_count.sort()
# print(ball_count)

if container_cap == ball_count:
    print("Possible")
else:
    print("Impossible")