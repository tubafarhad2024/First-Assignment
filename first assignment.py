# 1. What is OOP?
'''
Object-Oriented Programming (OOP) is a way to organize code by using objects. 
Each object holds data (attributes) and functions (methods) that work with that data. 
This structure helps us represent real-life things, making the code easier to manage, reuse, and understand.

Example: Think of a car. A car object can have attributes like color and model, 
and methods like drive and honk.
'''

class Car:
    # 2. What is a Class?
    '''
    A class is a template for creating objects. It defines the properties and behaviors 
    that the objects created from it will have.
    '''

    def _init_(self, color, model):
        # 4. What is a Constructor?
        '''
        A constructor is a special method that initializes a new object from a class. 
        It sets up the initial values for the object’s attributes.
        '''
        self.color = color
        self.model = model

    def honk(self):
        ''' 
        This method simulates the car honking.
        '''
        print("Beep! Beep!")

# Creating an instance of the Car class
myCar = Car("red", "Toyota")
# Calling the honk() method on the instance
myCar.honk()

# 3. What is an Object?
'''
An object is a specific instance of a class. 
It has its own set of data and can perform actions defined by the class. 
For instance, if "Dog" is a class, then "myDog" is an object of that class.
'''

# 5. What is Inheritance?
'''
Inheritance allows one class to inherit properties and methods from another class. 
This helps to create a hierarchy of classes where a child class can extend 
the functionality of a parent class.
'''

class SportsCar(Car):
    def _init_(self, color, model, speed):
        super()._init_(color, model)
        self.speed = speed

    def display(self):
        ''' 
        This method displays the car's color, model, and speed.
        '''
        print(f"{self.color} {self.model} goes {self.speed} mph!")

# Creating an instance of the SportsCar class
mySportsCar = SportsCar("blue", "Ferrari", 200)
# Calling the display() method on the instance
mySportsCar.display()

# 6. What is the self keyword?
'''
The self keyword is used in class methods to refer to the current instance of the class. 
It helps access attributes and methods of that object.
'''

# 7. What is Concatenation?
'''
Concatenation is the process of combining two or more strings into one single string. 
In Python, this is typically done using the + operator.
Example: 
If we have two strings, "Hello" and "World", we can concatenate them as follows:
'''
greeting = "Hello" + " " + "World"
print(greeting)  # Output: Hello World

# 8. What is NumPy?
'''
NumPy is a library in Python used for numerical computing. 
It provides support for arrays and matrices, along with mathematical functions 
to operate on these data structures.
Example: Creating an array using NumPy.
'''
import numpy as np

# Creating a NumPy array
array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", array)

# 9. What is File Handling?
'''
File handling is the process of reading from and writing to files in Python. 
It allows us to store data persistently. 
Example: Writing data to a file.
'''

# Writing to a file
with open('example.txt', 'w') as file:
    file.write("This is a sample text.")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File Content:", content)