#Write a Python Program to Find Armstrong Number in an Interval

a=int(input("Enter Start Limit:"))
b=int(input("Enter end Limit:"))
for i in range(a,b):
	n=i
	s=0
	while(n>0):
		d=n%10
		n=int(n/10)
		s=s+(d*d*d)
	if(s==i):
		print(i)
