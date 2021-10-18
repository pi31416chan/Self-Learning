# Imports
# import numpy as np



# Global Variables
encrypted_key = ''
rand_dict = {
'V': '00', ';': '01', '7': '02', 'Z': '03', ' ': '04', 'c': '05', 'r': '06', 
'M': '07', '6': '08', 'R': '09', 'T': '10', '9': '11', 'l': '12', ']': '13', 
'$': '14', 'y': '15', "'": '16', '"': '17', '3': '18', 'O': '19', 's': '20', 
')': '21', '>': '22', ':': '23', 'B': '24', 'b': '25', '{': '26', '2': '27', 
'~': '28', 'g': '29', 'm': '30', 'w': '31', 'F': '32', 't': '33', 'U': '34', 
'*': '35', 'z': '36', '1': '37', 'p': '38', 'q': '39', '0': '40', '@': '41', 
'S': '42', 'v': '43', 'e': '44', '4': '45', '(': '46', 'I': '47', '%': '48', 
'#': '49', 'Q': '50', '/': '51', 'Y': '52', 'X': '53', '\\': '54', 'D': '55', 
'E': '56', 'L': '57', 'C': '58', 'f': '59', '?': '60', '^': '61', ',': '62', 
'.': '63', 'j': '64', 'a': '65', '!': '66', 'i': '67', '}': '68', '|': '69', 
'k': '70', 'H': '71', '&': '72', '<': '73', 'x': '74', 'h': '75', 'P': '76', 
'n': '77', '-': '78', 'K': '79', '`': '80', '[': '81', 'G': '82', 'd': '83', 
'N': '84', 'o': '85', '8': '86', 'W': '87', '+': '88', 'u': '89', '_': '90', 
'5': '91', '=': '92', 'J': '93', 'A': '94'}
anti_hexatri_table = {
'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8',
'9':'9','10':'a','11':'b','12':'c','13':'d','14':'e','15':'f','16':'g',
'17':'h','18':'i','19':'j','20':'k','21':'l','22':'m','23':'n','24':'o',
'25':'p','26':'q','27':'r','28':'s','29':'t','30':'u','31':'v','32':'w',
'33':'x','34':'y','35':'z'}
opr_seq = (9,7,4,9,4,4,5,9,2,3)



# Functions
def conv_long_num(string):
	'''
	Converting the input string into a long chain of number according to
	the random dictionary of characters as shown above
	'''
	long_num = ''

	for char in string:
		long_num += rand_dict[char]

	print(long_num)

	return long_num

def conv_ex_long_num(string,sequence):
	'''
	Converting the input long number into an even longer number by 
	doing operations according to predefined operation sequence 
	(+,-,*,+,-,*,...) 
	'''
	ex_long_num = int(string)
	opr_record = '+'

	for seq in sequence:
		if opr_record == '+':
			ex_long_num += seq
			opr_record = '-'

		elif opr_record == '-':
			ex_long_num -= seq
			opr_record = '*'

		elif opr_record == '*':
			ex_long_num *= seq
			opr_record = '+'

	print(ex_long_num)

	return ex_long_num

def conv_hexatridec(dec_number):
    # Determine the maximum power of 36
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
        # print(digit,remainder)

        max_pow -= 1

        if max_pow == 0:
            hexatridec_output += anti_hexatri_table[str(remainder)]
            break

    print(hexatridec_output.upper())

    return hexatridec_output.upper()

def get_encryption_key(integer):
	'''
	Getting the actual encryption operation sequence from the input encryption key
	(full numerical integer ONLY without limitation on number of digits)
	'''
	encryption_opr_seq = []
	encryption_key = integer

	for i in str(encryption_key):
		encryption_opr_seq.append(opr_seq[int(i)])

	print(encryption_opr_seq)

	return encryption_opr_seq

def input_1():
	input_message_1 = "Please enter the encryption key in FULL NUMERICAL INTEGER ONLY\n" \
					  "Number of digits are not limited\n" \
					  "Example: 1234567890\n" \
					  "Hint: NRIC of program creator\n" \
					  'Enter "quit" to quit the program\n'

	encryption_key = input(input_message_1)

	return encryption_key

def input_2():
	input_message_2 = "Please enter the username/email and password to be encrypted\n" \
					  "Number of characters are not limited\n" \
					  'Example: "ali891204 5478!235*&72" (without quotes)\n' \
					  'Enter "quit" to quit the program\n'

	content = input(input_message_2)

	return content



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

		encryption_opr_seq = get_encryption_key(encryption_key)
		print()


	'''
	2nd Input
	User to enter the contents to be encrypted in string with almost any character
	'''
	content = input_2()

	if content == 'quit':
		exit()

	encrypted_key = conv_long_num(content)
	encrypted_key = conv_ex_long_num(encrypted_key,encryption_opr_seq)
	encrypted_key = conv_hexatridec(encrypted_key)

	print("\nYour encrypted key is:")
	print(encrypted_key)

	while reloop_2 == True:
		cont = input("\nDo you want to continue another encryption? (Y/N)\n")

		if cont.lower() == 'y':
			restart = True
			reloop_2 = False
			print()

		elif cont.lower() == 'n':
			exit()

		else:
			print('\nPlease enter only "Y" or "N"!')
			reloop_2 = True