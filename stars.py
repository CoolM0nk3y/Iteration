
amount = int(input("Please enter the amount of lines : "))

per_line = int(input("Please enter how many you want per line: ")) 
string = "*"
for a in range(1, amount + 1):
    print("{0}".format(string * per_line))
                   
