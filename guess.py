import random
guesses_made = 0
name = input('Hello!, who are you?\n')

number = random.randint(1, 20)
print ('Well, {0}, I am thinking of number between 1 and 20.'.format(name))

while guesses_made < 6:
	guess = int(input('Take a guess: '))
	guesses_made += 1

	if guess < number:
		print ('Your guess is too low.')

	if guess > number:
		print ('Your guess is too high.')

	if guess == number:
		break

if guess == number:
	print('Good job, {0}! the number is correct, after {1} guesses'.format(name, guesses_made))
else:
	print('Wrong. The number was {0}'.format(number))