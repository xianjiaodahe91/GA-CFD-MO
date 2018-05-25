# Package importation
import numpy as np
import sys
import os

################################################################################
#                                    INPUTS                                    # 
################################################################################
# Get the inputs from the terminal line
gen = float(sys.argv[1])

################################################################################
#                                   MAIN BODY                                  # 
################################################################################
# Get the values of the search space 
x1 = np.genfromtxt('./gen%i/popx%i' %(gen, gen))
x2 = np.genfromtxt('./gen%i/popy%i' %(gen, gen))

# Get the number of individuals
N = len(x1)

# Boundary conditions
U = 30 # m/s
rho = 1.225 #kg/m^3

# Loop over all individuals
for ind in range(N):
	# Get the lift, drag and area values for each individual
    D = np.genfromtxt('./gen%i/data/FITg%ii%i.txt' %(gen, gen, ind))[0] 
    L = np.genfromtxt('./gen%i/data/FITg%ii%i.txt' %(gen, gen, ind))[1] 
    # Save the values of the search space and the function value toghether in a file
    with open('./data/gen%i.txt' %gen, 'a') as file:
        file.write(",".join([str(x1[ind]),str(x2[ind]),str(-L/(0.5*rho*U**2)),str(D/(0.5*rho*U**2))]))
        file.write("\n")
        # The minus sign is due to maximization optimization