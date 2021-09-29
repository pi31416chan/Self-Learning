p = [5,2,1,3,4]



new_p = {}
p_y = []
pp_y = []



for i in range(len(p)):
    new_p[p[i]] = i + 1

for i in range(len(p)):
    p_y.append(new_p[i+1])

# print(p_y)

for num in p_y:
    pp_y.append(new_p[num])

print(pp_y)