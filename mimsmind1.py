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
		x = random.randint(000,999)
		g2(x)

def g1(n,x):
	print(x)
	count = 0
	chance = 1
	limit = (2**n) + n 
	lst = str(x)


	while chance <= limit :
		try:
			guess = int(input("Enter a " + str(n) + "-digit number : " ))
			lat = str(guess)
			chance += 1 
			count += 1
		except:
			print("Invalid input. Try again")
		cb = [0,0]
		for a in range(len(lat)):
			if lat == lst:
				print ("Congratulations. You guessed the correct number in " + str(count) + " tries.")
				quit()
			elif lat[a] == lst[a]:
				cb[1] += 1	
			elif lat[a] in lst:
				cb[0] += 1

		print (str(cb[1]) + " bull(s) , " + str(cb[0]) + " cows. Try again : " + str(guess) )

	print("Sorry. You did not guess the number in " + str(limit) + " tries. The correct number is " + str(x))



def g2(x):
	print(x)
	count = 0
	chance = 1
	limit = 11
	lst = str(x)

	while chance <= limit :
		try:
			guess = int(input("Enter a 3 digit number : " ))
			lat = str(guess)
			chance += 1 
			count += 1
		except:
			print("Invalid input. Try again")
		cb = [0,0]
		for a in range(3):
			if lat == lst:
				print ("Congratulations. You guessed the correct number in " + str(count) + " tries.")
				quit()
			elif lat[a] == lst[a]:
				cb[1] += 1	
			elif lat[a] in lst:
				cb[0] += 1

		print (str(cb[1]) + " bull(s) , " + str(cb[0]) + " cows. Try again : " + str(guess) )

	print("Sorry. You did not guess the number in " + str(limit) + " tries. The correct number is " + str(x))




def main():
	print("Let's play the mimsmind1 game.")
	game()

if __name__ == '__main__':
    main()
