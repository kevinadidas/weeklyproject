def binom(n,k):
	if n == k or k == 0:
		return 1
	
	return binom(n-1,k-1) + binom(n-1,k)


	
print(binom(5,3))