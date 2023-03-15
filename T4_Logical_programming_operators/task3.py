"""
Objective: program that determines the award a person competing in a
triathlon will receive. Considering time (minutes) of three events: triathlon
swimming and cycling. 
- Calculate and siplay the total time taken
- The award is given if time for a total of 100 minutes. 
"""

triathlon = float(input('Introduce the time of triathlon: '))
swim = float(input('Introduce the time of swimming: '))
run = float(input('Introduce the time of running: '))

total_time = triathlon + swim + run
print('The total time of the thriathlon for this participant is: ', total_time, ' minutes.')

if total_time <= 100:
        print('The participant receives the award: Provincial Colours')
elif total_time <= 105 and total_time > 100:
        print('The participant receives the award: Provincial Half Colours') 
elif total_time <= 110 and total_time > 105:
        print('The participant receives the award: Provincial Scroll')    
else:
        print('We are sorry, the participant did not qualify for an award!') 