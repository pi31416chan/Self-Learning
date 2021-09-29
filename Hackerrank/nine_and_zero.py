x = 9
i = -1
n = 1
zero = "0"
nine = "9"
y = ""
# print(x)

while x % n != 0:
    i = -1
    string_x = list(str(x))
    print(string_x,i)

    while string_x[i] == nine:
        i -= 1
        print(i)

        if -i > len(string_x):
            string_x.insert(0,zero)
            print(string_x,i)




    string_x[i] = nine
    print(string_x)
    i += 1
    while i < 0:
        string_x[i] = zero
        print(string_x)
        i += 1

    x = int("".join(string_x))
    print(x)

print()
print(x)








# x = 990909099
# print(x)
# string_x = list(str(x))
# print(string_x)
# x = int("".join(string_x))
# print(x)