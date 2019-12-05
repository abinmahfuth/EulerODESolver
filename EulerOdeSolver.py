'''
Simplest form of ODE solving

Written by Abdulrahman Binmahfuth
5th Dec. 2019

'''
import numpy as np
import time

#Start timing
start_time = time.time()


#Function Definition, y_f = y'(t), solving for y(t)
def y_f(y):
    #Write in the form of y_f = f(y(t)) ==> y'(t) = f(y)
    y_f = 2*y
    return y_f

#initilisation:
h = 0.01 #Step size
t = 4 #Target time for iteration
t0 = 0 #Initial time
n = (t-t0)/h #Number of steps needed
y0 = 1 # Value of y(t=0) 
y = y0 # initialising

#Sovler for y:
for i in np.arange(t0,t,h):    
    y = y + h*y_f(y)

#End timing
end_time = time.time()

#Print results
print("number of iteration: ", n)
print("Target time: ", t, "s")
print("execution time ", end_time - start_time, "s")
print("Y = ", y)
