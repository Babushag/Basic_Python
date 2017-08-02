nterms = input("How many terms? ")
n1terms=int(nterms)
n1 = 0
n2 = 1
count = 0
print("Fibonacci sequence upto",nterms,":")
for i in range(12):
     count=n1+n2
     n2=n1
     n1=count
     print(count,end=" ")
