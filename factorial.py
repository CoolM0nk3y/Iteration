#Oscar Stanley
#05-11-2014
#develpment task 1
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
   print("Your number has to be above 0 ")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of {0}".format(factorial))

             
             
             
    
