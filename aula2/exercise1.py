'''

#=============================
#Function without parameter.

#declaration

def display():
    print("I'm studing functions")

display()        #<-- calling

#===========================================
#Function that have parameter without retorn value

def multiplication(value1, value2):
    print("Product: ", value1 * value2)

multiplication(2,3)

#==========================================
#Function that return a value:

def multiplication2(value1, value2):

    return value1 * value2

print("pruct2: ", multiplication2(2,5))


#==========================================
#Function that return more than one value:

def operation(number1,number2):

    return number1*number2, number1 + number2, number1 - number2

product, total, rest = operation(4,2)

print("Product: ", product)
print("Total: ", total)
print("Rest: ", rest)


#Function that return more than one value:

def operation(number1,number2):

    return number1 * number2, number1 + number2, number1 - number2

product, total, rest = operation(4,2)

print("Product: ", product)
print("Total: ", total)
print("Rest: ", rest)

#=======================================
#Return more than one value using tuple:

tuple = ()
list = ["Product: ", "Total: ", "Rest: "]
i = 0

def operation(number1, number2):
    return number1 * number2, number1 + number2, number1 - number2

tuple = operation(10, 3)

while i < len(tuple):

    print(list[i], tuple[i])
    i+=1

'''