total = 0
count = 0

try:
    number = int(input("Enter a number, press -1 to exit: "))
    while number != -1:
        count += 1
        total += number
        number = int(input("Enter a number, press -1 to exit: "))
    print(total/count)
    
except ValueError:
    print('Please insert the correct numbers!')
    
    
