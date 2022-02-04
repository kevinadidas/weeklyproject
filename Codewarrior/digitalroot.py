def digital_root(n):
    # recursive is going down to base layer and up again
    # a + b < 10

    if n < 10:
    	print(n)
    	return n
    else: 
        #recursive case
        x = [int(num) for num in str(n)]

        n = sum(x)

        digital_root(n)


digital_root(942)