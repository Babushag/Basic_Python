def factorial(number):
  if number==1:
    return number
  return number*factorial(number-1)  
  

stringEnter=input("Enter the value")
num=int(stringEnter)
fact=factorial(num)
print(fact)
