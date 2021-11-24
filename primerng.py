#Write a Python Program to Print all Prime Numbers in an Interval
a=int(input("Enter Start Limit:"))
b=int(input("Enter End Limit:"))
print("prime numbers are::")
for n in range(a,b+1):
	if(n>1):
		for i in range(2,n):	
			if(n%i==0):
				break
			else:
				print(n)
				break




