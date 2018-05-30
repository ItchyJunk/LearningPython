'''
while True:
	try:
		word = str(input('Enter word:'))
		break

	except ValueError:
		print ('Please enter a valid string:')
'''
#import pdb; pdb.set_trace()
word = ''

while word.upper() != 'EXIT':
	word = input('Enter word or type exit:')
	if word == word[::-1]:
		print('The word {} is a Palindrome'.format(word))
	else:
		print('The word {} is not a Palindrome'.format(word))