def solution(number):
	
	if number > 0:

		threes = []
		fives = []

		#1 find all multiples of 3

		for i in range(number):
			if i%3==0:
				threes.append(i)
			if i%5==0:
				fives.append(i)
			else:
				continue

		combination = list(set(threes+fives))

		result = sum(combination)

		return result

	else:
		
		return 0



	#2 find all multiples of 5
	#3 make a set together of them 
	#4 add up numbers in the set
	#5 create overall if statement for number is negative()
 