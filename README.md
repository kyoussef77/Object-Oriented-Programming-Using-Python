# Object Oriented Programming Using Python
The four principles of object-oriented programming are encapsulation, abstraction, inheritance, and polymorphism.
This document explains how Python implements each object oriented principle by using example code and a description.

##Encapsulation
Encapsulation is achieved when each object keeps its state private, inside a class. 
Other objects don’t have direct access to this state. 
Instead, they can only call a list of public functions — called methods.

So, the object manages its own state via methods — and no other class can touch it unless explicitly allowed. 
If you want to communicate with the object, you should use the methods provided. 
But (by default), you can’t change the state.

    
    # ENCAPSULATION
    class  Multiplication:
        @staticmethod
        def product(multiplier,multiplicand=None):
            if (isinstance(multiplier,list)):
                return Multiplication.productList(multiplier)
            return multiplier * multiplicand
    
        @staticmethod
        def productList (valueList):
            result = 1
            for element in valueList:
                result = Multiplication.product(result, element)
            return result

   
   
##Abstraction
Abstraction can be thought of as a natural extension of encapsulation.
In object-oriented design, programs are often extremely large. And separate objects communicate with each other a lot.
 So maintaining a large codebase like this for years — with changes along the way — is difficult.
Applying abstraction means that each object should only expose a high-level mechanism for using it.

This mechanism should hide internal implementation details. It should only reveal operations relevant for the other objects.



    # ABSTRACTION
    
    from MathOperations.Addition import Addition;
    from MathOperations.Multiplication import Multiplication;
    
    class Calculator:
        Result = 0
        
        def __init__(self):
            pass
        def Sum(self, a, b):
            self.Result = Addition.sum(a, b)
            return self.Result
    
        def Product(self, a, b):
            self.Result = Multiplication.product(a, b)
            return self.Result

## Inheritance
Inheritance is the process by which one class takes on the attributes and methods of another.
 Newly formed classes are called child classes, and the classes that child classes are derived from are
  called parent classes.

It’s important to note that child classes override or extend the functionality (e.g., attributes and behaviors)
of parent classes. In other words, child classes inherit all of the parent’s attributes and behaviors but can 
also specify different behavior to follow. The most basic type of class is an object, which generally all other
classes inherit as their parent.

    # INHERITANCE
    from Calculator.calculator import Calculator
    from MathOperations.mean import Mean
    
    class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean(data)
        return self.Result

## Polymorphism
Polymorphism is an ability (in OOP) to use common interface for multiple form (data types).
 Polymorphism means having the same interface/attributes in different
classes.

 Polymorphism is the characteristic of being able to assign
a different meaning or usage in different contexts.
 A not-so-clear/clean example is, different classes can have
 the same function name.
 
    class Parrot:
    
        def fly(self):
            print("Parrot can fly")
        
        def swim(self):
            print("Parrot can't swim")
    
    class Penguin:
    
        def fly(self):
            print("Penguin can't fly")
        
        def swim(self):
            print("Penguin can swim")
    
    # common interface
    def flying_test(bird):
        bird.fly()
    
    #instantiate objects
    blu = Parrot()
    peggy = Penguin()
    
    # passing the object
    flying_test(blu)
    flying_test(peggy)
    
 In the above program, we defined two classes Parrot and Penguin. 
ach of them have common method fly() method. However, their functions are different.
To allow polymorphism, we created common interface i.e flying_test() function that can take any object.
Then, we passed the objects blu and peggy in the flying_test() function, it ran effectively.