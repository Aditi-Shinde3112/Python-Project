#Write a Python Program to Find the Factorial of a Numbers
num=int(input("Enter Number"))
fact=1
for i in range(1,num+1):
	fact=fact*i;
print("Factorial of",num,"=",fact)
