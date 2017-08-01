#stringEnter="Hi how are you"
stringEnter=input("Enter the value")
checklist=set(['A','E','I','O','U','a','e','i','o','u'])
print(checklist)
count=0
for i in stringEnter:
   if i in checklist:
     count=count+1
    # print(i)
     
print(count)   