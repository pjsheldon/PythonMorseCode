'''--------By: PJ Sheldon---------
	--------Date: 7/26/20---------
	step_1.py programming assignment 3
	SEC-290 Wilmington University'''

print('CONVERT LETTERS TO MORSE CODE')
print('')
print('Enter a letter in upper case to get the Morse Code')# program opening
print('')	

question = input('Please enter an upper case letter: ') # input question
print('')

if question == 'P': # if question for P
	morseCode = '.--.'
elif question == 'J': # elif for J 
	morseCode = '.---'
else: # else for any lower case letter or other alphabet letter that is not P or J
	morseCode = 'not a match to the letter we are looking for.\nCan you please enter an upper case P or J? \nThank you'

print('The Morse Code for {} is: {}.'.format(question, morseCode))# result answer
