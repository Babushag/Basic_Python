stringEnter=input("Enter the value")
num=int(stringEnter)
fact=1
while(num>1):
  fact=fact*num
  print("fact",fact)
  num=num-1
  print("num",num)
print("factorial of the number is",fact)
