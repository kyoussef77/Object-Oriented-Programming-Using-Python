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


    class Computer:
    
        def __init__(self):
            self.__maxprice = 900
    
        def sell(self):
            print("Selling Price: {}".format(self.__maxprice))
    
        def setMaxPrice(self, price):
            self.__maxprice = price
    
    c = Computer()
    c.sell()
    
    # change the price
    c.__maxprice = 1000
    c.sell()
    
    # using setter function
    c.setMaxPrice(1000)
    c.sell()


When we run this program, the output will be:

    Selling Price: 900
    Selling Price: 900
    Selling Price: 1000
    
 In the above program, we defined a class Computer. We use __init__() method to store the maximum selling price of computer.
  We tried to modify the price. However, we can’t change it because Python treats the __maxprice as private attributes.
   To change the value, we used a setter function i.e setMaxPrice() which takes price as parameter.