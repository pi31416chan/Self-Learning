# s = [278,   576,    496,    727,    410,    124,    338,    149,    209,    702,    282,    718,    771,    575,    436,
# ]
# s = [19,10,12,10,24,25,22]
s = [1,7,2,4]
k = 4







"""Generating a modulo dictionary with counts of each modulo from the
array s"""
mod_dict = {}



for num in s:
    m = num % k

    if m in mod_dict:
        mod_dict[m] += 1

    elif m not in mod_dict:
        mod_dict[m] = 1

# print(mod_dict)

"""Calculating the biggest size of s'"""
k_half = k/2
size = 0
mod_list = [modulo for modulo in mod_dict.keys()]
mod_list.sort()
done_list = []

# print(mod_list)

for modulo in mod_list:
    if modulo == 0 or modulo == k_half:
        size += 1
        done_list.append(modulo)

    elif k-modulo not in done_list:
        # print(modulo,k-modulo,mod_dict.get(k-modulo,0))
        if mod_dict[modulo] > mod_dict.get(k-modulo,0):
            size += mod_dict[modulo]
            done_list.append(modulo)

        else:
            size += mod_dict.get(k-modulo,0)
            done_list.append(modulo)
    # print(modulo,size)

print(size)