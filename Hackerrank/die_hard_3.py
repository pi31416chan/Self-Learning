abc = [601,430,430]


a = abc[0]
b = abc[1]
c = abc[2]



jugs_list = []
diff_list = []
excep_list = []
reloop = True


# Determines record two jugs into a same list
jugs_list.append(a)
jugs_list.append(b)
# print(jugs_list)



# Function of substraction
def substraction_from_jugs(diff_list):
    for diff in diff_list:
        # excep_list.append(diff)
        # print(excep_list)

        for jug in jugs_list:
            diff_a = abs(jug - diff)
            # print(diff_a)

            if diff_a not in diff_list and diff_a not in jugs_list:
                diff_list.append(diff_a)
                # print(diff_list)

    return diff_list



# Get basic substraction from two jugs for first number
diff = abs(a - b)
diff_list.append(diff)
# print(diff_list)

substraction_from_jugs(diff_list)

# print(diff_list)

if c in diff_list:
    print("YES")
    
else:
    print("NO")