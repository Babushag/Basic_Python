stringEnter=input("Enter the value")
number=int(stringEnter)
sum=0
while number>0:
  numb=number%10
 # print(numb)
  sum=sum+(numb**3)
 # print(sum)
  number=number//10

if number==sum:
print("number is armstrong")
else:
print("number is not armstrong")
