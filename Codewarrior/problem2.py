#def dig_pow(n,p):

	#make numbers with powers f.e 89,1 = 8^1 + 9^2 = 89 *1
	#46288,3 = 4^3^+6^4+2^5+8^6+8^7 = 2360688 = 46288 * 51 

	#1. split long number and make powers +1 from p
	#2. itarate through range and divide, if it == 0, then print out. if not, -1. 

n = 46288
k = [int(a) for a in str(n)]
print(k)

p=3
newlist = []

for num in k:
	x = num ** p
	p += 1
	newlist.append(x)

result = 0

for num in newlist:
	result += num

print(result)

final = 0

for i in range(1,result):
	if (result / i) == n:
		final = i
		break
	else:
		final = -1

print(final)