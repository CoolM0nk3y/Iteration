print("This will find the average of the numbers enterd. Type in -1 to stop the program")

enterd = int(input("Please enter a number: "))

numbersent = 1

total = 1

while enterd != -1 :
    enterd = int(input("Please enter a number: "))
    total = enterd + total
    numbersent = numbersent + 1
else :
    print("the average of the values you enterd is {0}". format(total / numbersent))
    
    
