from abc import ABC, abstractmethod

##############
# DEFINITION OF THE INTERFACE
##############
class Pet(ABC):

    @abstractmethod
    def play(self,toy:str):
        pass

    @abstractmethod
    def kiss(slef):
        pass

##############
# DEFINITION OF A CLASS OF THE INHERITANCE
##############
class Animal(ABC):

    def __init__(self,name:str,sex:str = 'MALE') -> None:
        self.__name = name
        self.__sex = sex

    @property
    def name(self):
        return self.__name
    
    @property
    def sex(self):
        return self.__sex
    
    def __str__(self) -> str:
        return f"Name: {self.name}, Sex: {self.sex}"
    
    def __repr__(self) -> str:
        return f"Name: {self.name}, Sex: {self.sex}"
    
    def sleep(self):
        print(f"({self.name}) ZzZzZzZ")

    @abstractmethod
    def eat(self, food:str):
        pass

##########
# OBJECT DOG
##########
class Dog(Animal, Pet):

    def __init__(self, name: str, size = 'SIZE', sex: str = 'MALE') -> None:
        super().__init__(name, sex)
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self,value):
        self.__size = value

    def eat(self, food: str):
        print(f"({self.name}) Hmmm, Thank you! for the {food} :-) ")

    def play(self,toy:str):
        print(f"({self.name}) I'm playing with {toy} ")

    def kiss(self):
        print(f"({self.name}) Muahh ;D ")


#####################
### TEST CODE #######

doggy = Dog("Doggy")
print(doggy)

doggy.eat("bone")
doggy.kiss()

