import math

print('Welcome to the calculator! Which operation will you be performing today?')
print('Investment - Calculate the amount of interest you will earn on your investment')
print('Bond       - Calculate the amount you will have to pay on home loan')

operation = input('Please, type the operation which you want to perform: ').lower()


#This code is a simple calculator that performs two operations: investment and bond calculations. 
#For investment, it calculates the total amount earned after a given number of years at a given interest rate, using either simple or compound interest. 
#For bonds, it calculates the final monthly repayment for a home loan based on the present value of the house, the interest rate, and the number of months over which the loan will be repaid. The user is prompted to choose which operation to perform and to input the necessary values for the calculation. 
#If an invalid operation is entered, an error message is displayed.


if operation != 'investment' and operation !='bond':
    print('Error, please introduce a valid operation')
else: 
    if operation == 'investment':
        amount = int(input('Introduce the amount of money to deposit: '))
        interest_rate = int(input('Introduce the interest rate, digit only: '))
        years_investing = int(input('Years planned to invest: '))
        
        interest = input('Simple or Compound?: ').lower()
        
        
        if interest == 'simple':
            total_amount = amount * (1 + interest_rate*years_investing)
        elif interest == 'compound':      
            total_amount = amount * math.pow((1 + interest_rate), years_investing)
        else:
            print('Introduce the correct type of interest!')
        
        print(f'The total amount you will receive investing at {interest} interest will be $ {total_amount}')
    
    else:
        if operation == 'bond':
            value_of_house = int(input('Introduce the present value of the house: $'))
            
            interest_rate = int(input('Introduce the interest rate, digit only: '))
            i = (interest_rate/100)/12
            
            months = int(input('Introduce the number of months to repay the bond: '))
            
            bond_repayment = (i * value_of_house) / (1 - (1 + i)**(-months))
            
            print(f'The final monthly repayment for the loan is: $ {bond_repayment:2f}')
        else:
            print('Introduce the correct details to execute the operation!')
           
# By: Edwar Benavente 