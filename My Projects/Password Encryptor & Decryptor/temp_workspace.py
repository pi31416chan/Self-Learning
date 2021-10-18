# Imports
import numpy as np



# Global Variables
x = [
"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i",
"j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B",
"C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U",
"V","W","X","Y","Z","`","-","=",";","'",",",".","/",":",'"',"<",">","?","\\",
"|","~","!","@","#","$","%","^","&","*","(",")","_","+","[","]","{","}"," ",
]

rand_seq = [
'V', ';', '7', 'Z', ' ', 'c', 'r', 'M', '6', 'R', 'T', '9', 'l', ']', '$', 
'y', "'", '"', '3', 'O', 's', ')', '>', ':', 'B', 'b', '{', '2', '~', 'g', 
'm', 'w', 'F', 't', 'U', '*', 'z', '1', 'p', 'q', '0', '@', 'S', 'v', 'e', 
'4', '(', 'I', '%', '#', 'Q', '/', 'Y', 'X', '\\', 'D', 'E', 'L', 'C', 'f', 
'?', '^', ',', '.', 'j', 'a', '!', 'i', '}', '|', 'k', 'H', '&', '<', 'x', 
'h', 'P', 'n', '-', 'K', '`', '[', 'G', 'd', 'N', 'o', '8', 'W', '+', 'u', 
'_', '5', '=', 'J', 'A'
]


# Functions



# Program
# rand_dict = {}

# for i in range(len(rand_seq)):
#     rand_dict[f"{i :=02d}"] = rand_seq[i]

# print(rand_dict)



# rand_seq = []

# for i in range(len(x)):
#     picked = np.random.choice(x)
#     rand_seq.append(picked)
#     x.remove(picked)

# print(rand_seq, len(rand_seq))



x = 3867183745370805756577041837453791112708914541587487

hexatridec_table = {
'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8',
'9':'9','a':'10','b':'11','c':'12','d':'13','e':'14','f':'15','g':'16',
'h':'17','i':'18','j':'19','k':'20','l':'21','m':'22','n':'23','o':'24',
'p':'25','q':'26','r':'27','s':'28','t':'29','u':'30','v':'31','w':'32',
'x':'33','y':'34','z':'35',}
anti_hexatri_table = {
'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8',
'9':'9','10':'a','11':'b','12':'c','13':'d','14':'e','15':'f','16':'g',
'17':'h','18':'i','19':'j','20':'k','21':'l','22':'m','23':'n','24':'o',
'25':'p','26':'q','27':'r','28':'s','29':'t','30':'u','31':'v','32':'w',
'33':'x','34':'y','35':'z'}

hexatridec_number = 'CZC9XSJG7TY321ZRAQ9VKFM45G1H32TDCY9'

ex_long_num = 0

for char,i in zip(hexatridec_number,range(len(hexatridec_number))[::-1]):
    ex_long_num += int(hexatridec_table[char.lower()])*(36**i)

print(ex_long_num)



opr_seq = (9,7,4,9,4,4,5,9,2,3)
decryption_opr_seq = []
encryption_key = 1234

for i in str(encryption_key):
    decryption_opr_seq.append(opr_seq[int(i)])

# decryption_opr_seq = 



temp = 623541
ex_long_num = 5611900
sequence = [4, 9, 4, 7]

# if len(sequence) % 3 == 0:
#     opr_record = '/'
# elif len(sequence) % 3 == 2:
#     opr_record = '+'
# else:
#     opr_record = '-'

# for seq in sequence:
#     if opr_record == '/':
#         ex_long_num /= seq
#         opr_record = '+'

#     elif opr_record == '+':
#         ex_long_num += seq
#         opr_record = '-'

#     elif opr_record == '-':
#         ex_long_num -= seq
#         opr_record = '/'

# print(ex_long_num)



string = '26812984134190490791'
anti_rand_dict = {
'00': 'V', '01': ';', '02': '7', '03': 'Z', '04': ' ', '05': 'c', '06': 'r', 
'07': 'M', '08': '6', '09': 'R', '10': 'T', '11': '9', '12': 'l', '13': ']', 
'14': '$', '15': 'y', '16': "'", '17': '"', '18': '3', '19': 'O', '20': 's', 
'21': ')', '22': '>', '23': ':', '24': 'B', '25': 'b', '26': '{', '27': '2', 
'28': '~', '29': 'g', '30': 'm', '31': 'w', '32': 'F', '33': 't', '34': 'U', 
'35': '*', '36': 'z', '37': '1', '38': 'p', '39': 'q', '40': '0', '41': '@', 
'42': 'S', '43': 'v', '44': 'e', '45': '4', '46': '(', '47': 'I', '48': '%', 
'49': '#', '50': 'Q', '51': '/', '52': 'Y', '53': 'X', '54': '\\', '55': 'D', 
'56': 'E', '57': 'L', '58': 'C', '59': 'f', '60': '?', '61': '^', '62': ',', 
'63': '.', '64': 'j', '65': 'a', '66': '!', '67': 'i', '68': '}', '69': '|', 
'70': 'k', '71': 'H', '72': '&', '73': '<', '74': 'x', '75': 'h', '76': 'P', 
'77': 'n', '78': '-', '79': 'K', '80': '`', '81': '[', '82': 'G', '83': 'd', 
'84': 'N', '85': 'o', '86': '8', '87': 'W', '88': '+', '89': 'u', '90': '_', 
'91': '5', '92': '=', '93': 'J', '94': 'A',}

long_num = string
decrypted_key = ''
two_char = ''

# for char in long_num:
#     two_char += char
#     if len(two_char) == 2:
#         print(two_char,anti_rand_dict[two_char])
#         decrypted_key += anti_rand_dict[two_char]
#         two_char = ''

# print(decrypted_key)

print(3*355218156489087631357257865196031672477912260486889472)