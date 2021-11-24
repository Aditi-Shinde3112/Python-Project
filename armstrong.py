num=int(input("Enter Number:"))
sum=0
temp=num
while(temp>0):
   rem=temp%10
   sum=sum+rem*rem*rem
   temp=int(temp/10)
if(num==sum):
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")	
