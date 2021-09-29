# Input
# topic = [
#         '10101',
#         '11110',
#         '00010',]

topic = [
        '10101',
        '11100',
        '11010',
        '00101',]



# Variables
strongest_team = 0
topic_count = 0
i = -1



for top in topic:
    i += 1
    j = i
    # print(i)

    if i == len(topic) - 1:
        break

    else:
        while j < len(topic) - 1:
            one_count = 0
            j += 1
            for a,b in zip(topic[i],topic[j]):
                if a == '1' or b == '1':
                    one_count += 1

            # print(i,one_count)
            if one_count > topic_count:
                topic_count = one_count
                strongest_team = 1

            elif one_count == topic_count and one_count != 0:
                strongest_team += 1

            # print(i,j,one_count,strongest_team)

print(topic_count,strongest_team)