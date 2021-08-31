c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2



e = 100



# Processing
c_modified = c[:]
c_modified.append(c[0])
print(c_modified)

# Energy decreased without thunder
e -= len(c)/k

# Energy decreased by thunder
step_count = 0
e_thunder = 0

while step_count < len(c):
    step_count += k

    if c_modified[step_count] == 1:
        e_thunder += 2

    print(step_count,e_thunder)
    print()

e_final = round(e - e_thunder)

print(e_final)
