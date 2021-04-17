'''--------By: PJ Sheldon---------
	--------Date: 7/26/20---------
	step_2.py programming assignment 3
	SEC-290 Wilmington University'''

def text_to_morse(P):  # text to morse function
	if question == 'P': # morse code for P                                                      
		morseCode = '.--.'
		return print('The Morse Code for {} is: {}.'.format(question, morseCode))
	elif question == 'J': # morse code for J 
		morseCode = '.---'
		return print('The Morse Code for {} is: {}.'.format(question, morseCode))
	else: # for any lower case or other letter then PJ 
		morseCode = 'not a match to the letter we are looking for.\nCan you please enter an upper case P or J? \nThank you'
		return print('The Morse Code for {} is: {}.'.format(question, morseCode))

print('CONVERT LETTERS TO MORSE CODE')
print('')
print('Enter a letter in upper case to get the Morse Code') # intro to the program
print('')	

question = input('Please enter an upper case letter: ') # input question
print('')

text_to_morse(question) # function with question