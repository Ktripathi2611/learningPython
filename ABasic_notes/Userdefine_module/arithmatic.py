''' 
a simple arithmatic file 
 '''

def add(*add):
    return sum(add)

def sqrt(num):
    return num ** 0.5#square root

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

# use of __name__ is to check if the file is run as a script or imported as a module 

a=10
b=20
if __name__ == "__main__":# this line is used to check if the file is run as a script or imported as a module  means if the file is run as a script then it will run the code inside the if block
    print(add(a,b))
    print(sqrt(a))
    print(square(a))
    print(cube(a))
