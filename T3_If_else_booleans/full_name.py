name = len(input('Insert your full name: '))


if name > 0:
    
    if name < 4:
        print('You have entered less than 4 character. Please make sure you have entered your name and surname')
    elif name > 25:
        print('You have entered more than 25 characters. Please make sure that you have only entered your full name')
    else:
        print('Thank you for entering your full name.')
        
else:
    print('You have not entered anything! Please enter your full name.')
    