#def get_middle(s):
	s = "aaaaf"
	letters = list(s)


	if len(s)%2==0:
		x = letters[int((len(s)/2)-1)]+""+letters[int(len(s)/2)]
		return x
	else:
		x = letters[int(len(s)/2)]
		return x