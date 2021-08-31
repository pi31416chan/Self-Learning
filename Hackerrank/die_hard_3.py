a = 5
b = 3
c = 4



jugs_list = []
diff_list = []
excep_list = []
reloop = True


# Determines record two jugs into a same list
jugs_list.append(a)
jugs_list.append(b)



# Function of substraction
def substraction_from_jugs(diff_list):
    for diff in diff_list:
        excep_list.append(diff)

        for jug in jugs_list:
            diff = abs(jug - diff)

            if diff not in diff_list and diff not in jugs_list:
                diff_list.append(diff)

    return diff_list



# Get basic substraction from two jugs for first number
diff = abs(a - b)
diff_list.append(diff)

substraction_from_jugs(diff_list)

print(diff_list)
