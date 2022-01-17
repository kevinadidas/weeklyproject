def alphabet_position(text):
	#give alphabet an index
	#return index

	#for every letter, check with index
	#if its not in the dictionairy, then skip

	alphabet = ["0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	keys = range(1,len(alphabet))

	numbers_dict = {}

	for i in (keys):
		numbers_dict[i] = alphabet[i]




	textlower = text.lower()


	textsplit = []

	for a in textlower:
		textsplit.append(a)

	print(textsplit)


	#for letter in textsplit: 
	#	if 
	finalstring = []


	for letter in textsplit: 
		for i in numbers_dict:
			if letter == numbers_dict[i]:
				finalstring.append(i)


	result = ""
	for i in finalstring:
		result += (str(i)+" ")

	print(result)
	return result
