# example of encapsulation using classes and object
 
class Worker:
   
#'Common base class for all workers'
   
Count = 0

   

def __init__(self, name, salary):
      
self.name = name
     
self.salary = salary
     
 Worker.Count += 1
   
 
  
def displayCount(self):
     
print "Total Worker %d" % Worker.Count

 
 
def displayWorker(self):
      
print "Name : ", self.name,  ", Salary: ", self.salary



w1 = Worker("Ram", 2000)

w2 = Worker("Shaam", 5000)

w1.displayWorker()

w2.displayWorker()

print "Total Employee %d" % Worker.Count