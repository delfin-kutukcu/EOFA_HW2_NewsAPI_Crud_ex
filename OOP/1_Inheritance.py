"""
1_inheritance.py

This file demonstrates the concept of inheritance in Python.
It shows how a child class can inherit properties and methods from a parent class.
"""

class Animal:
    """
    Base class for all animals. Defines common properties and behaviors.
    """
    def __init__(self, name, foot_num):
        """
        Constructor method for the Animal class.
        
        :param name: Name of the animal
        :param foot_num: Number of feet the animal has
        """
        self.name = name
        self.foot_num = foot_num    
    
    def make_sound(self):
        """
        Represents the sound the animal makes.
        
        :return: Sound of the animal (str)
        """
        return "Animal is making a noise."
    
    def foot_num_is(self):
        """
        Returns the number of feet the animal has.
        
        :return: Number of feet (int)
        """
        return self.foot_num


class Dog(Animal):
    """
    Dog class, inherits from the Animal class.
    """
    def __init__(self, name):
        """
        Constructor method for the Dog class.
        
        :param name: Name of the dog
        """
        super().__init__(name, foot_num=4)
    
    def make_sound(self):
        """
        Represents the sound a dog makes.
        
        :return: Sound of the dog (str)
        """
        return "Woof woof!"


class Cat(Animal):
    """
    Cat class, inherits from the Animal class.
    """
    def __init__(self, name):
        """
        Constructor method for the Cat class.
        
        :param name: Name of the cat
        """
        super().__init__(name, foot_num=4)
    
    def make_sound(self):
        """
        Represents the sound a cat makes.
        
        :return: Sound of the cat (str)
        """
        return "Meow meow!"


class Bird(Animal):
    """
    Bird class, inherits from the Animal class.
    """
    def __init__(self, name):
        """
        Constructor method for the Bird class.
        
        :param name: Name of the bird
        """
        super().__init__(name, foot_num=2)
    
    def make_sound(self):
        """
        Represents the sound a bird makes.
        
        :return: Sound of the bird (str)
        """
        return "Chirp chirp!"


# Usage
dog = Dog('Rocky')
cat = Cat('Fluffy')
bird = Bird('Blue')
pegasus_animal = Animal('Pegasus', 4)

print(f'{dog.name} : {dog.make_sound()}')
print(f'{dog.name} foot number: {dog.foot_num_is()}')
print(f'{cat.name} : {cat.make_sound()}')
print(f'{cat.name} foot number: {cat.foot_num_is()}')
print(f'{bird.name} : {bird.make_sound()}')
print(f'{bird.name} foot number: {bird.foot_num_is()}')
print(f'{pegasus_animal.name} : {pegasus_animal.make_sound()}')
print(f'{pegasus_animal.name} foot number: {pegasus_animal.foot_num_is()}')