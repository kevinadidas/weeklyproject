def move_zeros(array):
	
	result = array
	counter = 0

	for i in array:
		if i == 0:
			counter += 1
			array.remove(i)
			result.append(0)

	return result


move_zeros([1,2,0,3,0,4,3,0])

