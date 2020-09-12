from math import exp

def my_func(k):
     return 1/(1 + exp(-k))
     

#print my_func(0)

Wxh = 0.5
Whh = -1.0 
Why = -0.7 
hbias = -1.0
ybias = 0.0

x1 = 9
x2 = 4
x3 = -2


A1=9*0.5 
a2=my_func(-2*0.5 -1)

a3=4*0.5


#A1 = Whh*a1
A2 = Whh*a2

A3 = a3

A4 =   A3 
#print A4
A5 = my_func(A3 + A1 -1)
#print A5
A6 = A5*Why

print A6

print my_func(A6)

#print y




 


