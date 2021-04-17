'''--------By: PJ Sheldon---------
	--------Date: 7/26/20---------
	step_3.py programming assignment 3
	SEC-290 Wilmington University'''

def text_to_morse(P):	# text to morse code function
	if question == 'P':                                                              # coding for P
		morseCode = '.--.'
		return print('The Morse Code for {} is: {}.'.format(question, morseCode))
	elif question == 'J':                                                            # coding for J
		morseCode = '.---'
		return print('The Morse Code for {} is: {}.'.format(question, morseCode)) 
	else:                                                                            # if the player chooses any of the other letters or lower case
		morseCode = 'not a match to the letter we are looking for.\nCan you please enter an upper case P or J? \nThank you' 
		return print('The Morse Code for {} is: {}.'.format(question, morseCode))

	

print('CONVERT LETTERS TO MORSE CODE')
print('')
print('Enter a letter in upper case to get the Morse Code') # extra writing when running the program
print('')	

question = input('Please enter an upper case letter: ') # first time asking
print('')
text_to_morse(question)
print('')
    
question = input('Please enter an upper case letter: ') # second time asking
print('')
text_to_morse(question)
print('')

question = input('Please enter an upper case letter: ') # third time asking
print('')
text_to_morse(question)
print('')

question = input('Please enter an upper case letter: ') # fourth time asking
print('')
text_to_morse(question)
print('')

question = input('Please enter an upper case letter: ') # 5th time asking
print('')
text_to_morse(question)
print('')

print('That is all she wrote, game over, Thanks for Playing') # thought this would be a good enging to the chances if people kept going.