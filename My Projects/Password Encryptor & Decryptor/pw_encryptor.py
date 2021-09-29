# Imports
import numpy as np


# Global Variables
encrypted_key = ''

rand_dict = {
'r': '00', 'o': '01', 'k': '02', '<': '03', '@': '04', 'd': '05', 
't': '06', 'l': '07', '7': '08', 'x': '09', '8': '10', 'y': '11', 
'e': '12', 'q': '13', '}': '14', '?': '15', '$': '16', 'h': '17', 
'!': '18', ' ': '19', 'c': '20', '9': '21', 'm': '22', '>': '23', 
'6': '24', '4': '25', ',': '26', '1': '27', '0': '28', '_': '29', 
'{': '30', '/': '31', '(': '32', '5': '33', 'f': '34', '|': '35', 
'b': '36', '\\': '37', ')': '38', '~': '39', '[': '40', 'w': '41', 
'.': '42', '%': '43', '3': '44', '^': '45', '`': '46', 'g': '47', 
']': '48', '#': '49', 'v': '50', '=': '51', ':': '52', 'p': '53', 
'z': '54', ';': '55', '2': '56', '*': '57', "'": '58', '+': '59', 
'a': '60', '&': '61', '"': '62', 'n': '63', 'j': '64', '-': '65', 
's': '66', 'u': '67', 'i': '68'}

opr_seq = [7,3,3,4,9,3,7,3]


# Functions
def conv_long_num(string):
	'''
	Converting the input string into a long chain of number according to
	the random dictionary of characters as shown above
	'''
	long_num = ''

	for char in string:
		long_num += rand_dict[char]

	return long_num

def conv_ex_long_num(string):
	'''
	Converting the input long number into an even longer number by 
	doing operations according to predefined operation sequence 
	(+,-,*,+,-,*,...) 
	'''
	ex_long_num = int(string)
	opr_record = '+'

	for seq in opr_seq:
		if opr_record == '+':
			ex_long_num += seq
			opr_record = '-'

		if opr_record == '-':
			ex_long_num -= seq
			opr_record = '*'

		if opr_record == '*':
			ex_long_num *= seq
			opr_record = '+'

	return ex_long_num

def conv_hexa(integer):
	dec_int = integer

	hexa_int = f"{dec_int :x}".upper()

	return hexa_int


# Program
print(conv_hexa(168041110593473887200923342224221149715840))