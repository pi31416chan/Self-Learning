# Input
s = "haveaniceday"



# Determining the rows and columns of the table
spaceless = s.replace(" ","")
length = len(spaceless)
print(length)

row = length ** 0.5
if row > int(row):
    row = int(row)
    column = row + 1
else:
    row = int(row)
    column = row
print(row,column)
j = 0



# Generating encrypted keys list
encrypted_keys = []
for n in range(column):
    encrypted_keys.append('')
# print(encrypted_keys)


for char in spaceless:

    if j == column:
        j = 0

    encrypted_keys[j] += char
    j += 1

encrypted_key = ' '.join(encrypted_keys)

print(encrypted_key)


