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
#     rand_dict[rand_seq[i]] = f"{i :=02d}"

# print(rand_dict)



# rand_seq = []

# for i in range(len(x)):
#     picked = np.random.choice(x)
#     rand_seq.append(picked)
#     x.remove(picked)

# print(rand_seq, len(rand_seq))



x = 3867183745370805756577041837453791112708914541587487

def conv_hexatridec(dec_number):
    # Determine the maximum power of 36
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
    max_pow = 0
    hexatridec_output = ''
    remainder = dec_number
    digit = 0

    i = 0
    while True:
        i += 1

        if dec_number/(36**i) >= 1.0:
            max_pow = i
            continue

        if dec_number/(36**i) < 1.0:
            break

    while True:
        digit = int(remainder/(36**max_pow))
        hexatridec_output += anti_hexatri_table[str(digit)]

        remainder = remainder%(36**max_pow)
        print(digit,remainder)

        max_pow -= 1

        if max_pow == 0:
            hexatridec_output += anti_hexatri_table[str(remainder)]
            break

    return hexatridec_output

print(conv_hexatridec(x).upper())

