'''
#Parameters Default.

def display(value1 = 2, value2 = 20):
    print("Value 1: ", value1)
    print("Value 2: ", value2)

#Calling the function.

display(222)

#========================================

#args

def number(*args):

    for value in args:
        print(value)

number(1,2,3)

#======================================
#functions as parameters

def mult(n1,n2):
    return n1*n2

def expo(v1,v2):
    return pow(v1,v2)

def display(a, b, func):
    print(func(a,b))

display(4,3, mult)
display(4,3, pow)

#===============================
#recive a list as parameter
'''

def display_list(list):
    return list

list_month = ["January", "February", "March", "April", "May"]

months = [display_list(list_month)]

for i in months:

    print(i)