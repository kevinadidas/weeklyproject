#def get_sum(a,b):

a = 0
b = 1

smalltolarge = []

if a <= b:

	for i in range(a,b+1):
		num = i
		print(num)
		smalltolarge.append(num)
		num = num + 1
		print(num)

	print(smalltolarge)

else:

	for i in range(b,a+1):
		num = i
		print(num)
		smalltolarge.append(num)
		num = num + 1
		print(num)

	print(smalltolarge)

result = 0

for i in smalltolarge:
	result += i

print(result)
