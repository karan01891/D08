import random
import sys


def game():
	if (len(sys.argv) > 1):
		n = int(sys.argv[1])
		start_range = 10**(n-1) 
		end_range = (10**n) - 1
		x = random.randint(start_range,end_range)
		g1(n,x)
	else:
		x = random.randint(0,9)
		g2(x)

def g1(n,x):
	count = 0
	while True:
		guess = input("Enter a " + str(n) + "-digit number : " )
		if int(guess) == x :
			count += 1
			print ("Congratulations. You guessed the correct number in " + str(count) + " tries.")
			break
		elif int(guess) < x :
			print ("Try again. Guess a higher number: " + guess)
			count += 1
		elif int(guess) > x :
			print ("Try again. Guess a lower number:" + guess)
			count += 1

def g2(x):
	count = 0
	while True:
		guess = input("Enter a 1-digit number : " )
		if int(guess) == x :
			count += 1
			print ("Congratulations. You guessed the correct number in " + str(count) + " tries.")
			break
		elif int(guess) < x :
			print ("Try again. Guess a higher number: " + guess)
			count += 1
		elif int(guess) > x :
			print ("Try again. Guess a lower number:" + guess)
			count += 1

def main():
	print("Let's play the mimsmind0 game.")
	game()

if __name__ == '__main__':
    main()
