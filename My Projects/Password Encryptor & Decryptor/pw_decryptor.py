# Imports
# import numpy as np



# Global Variables
decrypted_key = ''
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
hexatridec_table = {
'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8',
'9':'9','a':'10','b':'11','c':'12','d':'13','e':'14','f':'15','g':'16',
'h':'17','i':'18','j':'19','k':'20','l':'21','m':'22','n':'23','o':'24',
'p':'25','q':'26','r':'27','s':'28','t':'29','u':'30','v':'31','w':'32',
'x':'33','y':'34','z':'35',}
opr_seq = (9,7,4,9,4,4,5,9,2,3)



# Functions
def dec_long_num(string):
    '''
    Decoding the long chain of number into a string according to
    the random dictionary of characters as shown above
    '''
    long_num = string
    decrypted_key = ''
    two_char = ''

    for char in long_num:
        two_char += char
        if len(two_char) == 2:
            # print(two_char,anti_rand_dict[two_char])
            decrypted_key += anti_rand_dict[two_char]
            two_char = ''

    # print(decrypted_key)

    return decrypted_key

def dec_ex_long_num(string,sequence):
    '''
    Decoding long number from extra long number by doing operations
    according with preefined decryption operation sequence
    (/,+,-,/,+,-,...) 
    '''
    long_num = int(string)

    if len(sequence) % 3 == 0:
        opr_record = '/'
    elif len(sequence) % 3 == 2:
        opr_record = '+'
    else:
        opr_record = '-'

    for seq in sequence:
        if opr_record == '/':
            long_num //= seq
            # long_num = int(long_num)
            opr_record = '+'

        elif opr_record == '+':
            long_num += seq
            opr_record = '-'

        elif opr_record == '-':
            long_num -= seq
            opr_record = '/'

    # print(int(long_num))

    return str(int(long_num))

def dec_hexatridec(hexatridec_number):
    '''
    Decoding extra long number from hexatridecimal number
    '''
    ex_long_num = 0

    for char,i in zip(hexatridec_number,range(len(hexatridec_number))[::-1]):
        ex_long_num += int(hexatridec_table[char.lower()])*(36**i)

    # print(ex_long_num)
    
    return ex_long_num

def get_decryption_opr_seq(integer):
    '''
    Getting the actual decryption operation sequence from the input encryption key
    (full numerical integer ONLY without limitation on number of digits)
    '''
    decryption_opr_seq = []
    encryption_key = integer

    for i in str(encryption_key):
        decryption_opr_seq.append(opr_seq[int(i)])

    decryption_opr_seq = decryption_opr_seq[::-1]

    # print(decryption_opr_seq)

    return decryption_opr_seq

def input_1():
    input_message_1 = "Please enter the encryption key in FULL NUMERICAL INTEGER ONLY\n" \
                      "Number of digits are not limited\n" \
                      "Example: 1234567890\n" \
                      "Hint: NRIC of program creator\n" \
                      'Enter "quit" to quit the program\n'

    encryption_key = input(input_message_1)

    return encryption_key

def input_2():
    input_message_2 = "Please enter the encrypted key to be decrypted\n" \
                      "Number of characters are not limited\n" \
                      'Example: "SAD87V24786SDB23489SDO" (without quotes)\n' \
                      'Enter "quit" to quit the program\n'

    content = input(input_message_2)

    return content



# Test Program
# print(dec_hexatridec('XE2P8RQ0T4TKRXFNDZ35'))
# print(dec_ex_long_num(5611900,[4, 9, 4, 7]))
# print(get_decryption_opr_seq(940919085899))
# print(dec_long_num('72541294527601'))




# Program
'''
1st Input
User to enter the encryption key (FULL NUMERICAL INTEGER ONLY) that the
encryption algorithm will be based upon
'''
restart = True

while restart == True:
    reloop = True
    reloop_2 = True

    while reloop == True:
        
        encryption_key = input_1()

        if encryption_key == 'quit':
            exit()

        try:
            encryption_key = int(encryption_key)
            reloop = False
        
        except:
            print("\nWrong format entered!!!\n")
            reloop = True
            continue

        decryption_opr_seq = get_decryption_opr_seq(encryption_key)
        print()


    '''
    2nd Input
    User to enter the encrypted contents to be decrypted in string with almost any character
    '''
    encrypted_content = input_2()

    if encrypted_content == 'quit':
        exit()

    decrypted_key = dec_hexatridec(encrypted_content)
    decrypted_key = dec_ex_long_num(decrypted_key,decryption_opr_seq)
    decrypted_key = dec_long_num(decrypted_key)

    print("\nYour decrypted content is:")
    print(decrypted_key)

    while reloop_2 == True:
        cont = input("\nDo you want to continue another decryption? (Y/N)\n")

        if cont.lower() == 'y':
            restart = True
            reloop_2 = False
            print()

        elif cont.lower() == 'n':
            exit()

        else:
            print('\nPlease enter only "Y" or "N"!')
            reloop_2 = True