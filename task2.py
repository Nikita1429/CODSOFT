def add(P1,P2):      
   return P1+P2  
def subtract(P1,P2):     
   return P1-P2   
def multiply(P1,P2): 
   return P1*P2   
def divide(P1,P2):       
   return P1/P2    
#    
print ("Please select the operation.")    
print ("a.Add")    
print ("b.Subtract")    
print ("c.Multiply")    
print ("d.Divide")    
    
choice = input("Please enter choice (a/ b/ c/ d): ")    
    
P1 = int(input ("Enter the first number:"))    
P2 = int(input ("Enter the second number:"))    
    
if choice == 'a':    
   print (P1, " + ", P2, " = ", add(P1, P2))    
    
elif choice == 'b':    
   print (P1, " - ", P2, " = ", subtract(P1, P2))    
    
elif choice == 'c':    
   print (P1, " * ", P2, " = ", multiply(P1, P2))    
elif choice == 'd':    
   print (P1, " / ", P2, " = ", divide(P1, 2))    
else:    
   print("Invalid input")    