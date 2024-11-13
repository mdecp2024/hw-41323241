'''
Under ideal conditions a certain bacteria population is known to double every three hours.  
Suppose that there are initially 100 bacteria. When will the population first reach 50,000 ? 
'''
import math

# Given values
P0 = 100  # initial population
P_target = 50000  # target population
T = 3  # doubling time in hours

# Calculate the time when population reaches P_target
t = T * math.log(P_target / P0, 2)

print(f"The population will first reach {P_target} after {t:.2f} hours.")

