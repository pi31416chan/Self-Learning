# Import modules
import json

#Input Section
f = open('test samples.json','r')
users_dict = json.load(f)
# print(users_dict)
users = users_dict["users"]
f.close()
# print(users)



"""Reference table from 0 to 9 then a to z
Expandable by adding more character:index pair into this table"""
sequence_ref = {
    '0':1,'1':2,'2':3,'3':4,'4':5,'5':6,'6':7,'7':8,'8':9,'9':10,
    'a':11,'b':12,'c':13,'d':14,'e':15,'f':16,'g':17,'h':18,
    'i':19,'j':20,'k':21,'l':22,'m':23,'n':24,'o':25,'p':26,
    'q':27,'r':28,'s':29,'t':30,'u':31,'v':32,'w':33,'x':34,
    'y':35,'z':36,
}



# Variables
sorted_list = []
dec_index_list = []



# Function to calculate the decimal index of each string
def get_decimal_index(string):
    decimal_index = 0.0
    digit = 0

    for char in string:
        digit += 1
        decimal_index += (sequence_ref[char]/len(sequence_ref)) / len(sequence_ref)**(digit-1)

    return decimal_index

# Function to detect and insert character in str into a list 
def insert_char_to_list(string,decimal_index):
    i = -1

    if sorted_list:

        for dec_index in dec_index_list:
            i += 1

            if decimal_index > dec_index:
                try:
                    if dec_index_list[i+1]:
                        continue
                except:
                    dec_index_list.append(decimal_index)
                    sorted_list.append(string)
                    break
            elif decimal_index < dec_index:
                dec_index_list.insert(i,decimal_index)
                sorted_list.insert(i,string)
                break
            else:
                dec_index_list.insert(-1,decimal_index)
                sorted_list.insert(-1,string)

    else:
        dec_index_list.append(decimal_index)
        sorted_list.append(string)

    # print(dec_index_list)
    # print(sorted_list)
    # return sorted_list

# Function to define the location of any alphabet or number
def sort_without_builtin(sample_list):

    for item in sample_list:
        insert_char_to_list(item,get_decimal_index(item))

    return sorted_list



sort_without_builtin(users)

# Output section
sorted_users = {
                "users":sorted_list
                }

f = open("output.json",'w')
json.dump(sorted_users,f)