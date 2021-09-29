path = 'UDDDUDUUDDDUDUUU'


valley_flag = False
altitude = 0
valley_count = 0



# Count the number of valley by keeping track on altitude
for step in path:
    if step == 'U':
        altitude += 1
        if altitude >= 0 and valley_flag == True:
            valley_flag = False
    elif step == 'D':
        altitude -= 1
        if altitude < 0 and valley_flag == False:
            valley_flag = True
            valley_count += 1

print(valley_count)
