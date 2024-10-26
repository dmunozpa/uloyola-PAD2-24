from abc import ABC, abstractmethod

class Animal(ABC):


    ###############
    # NOTICE: 2 atributes privates and sex by default will be set as MALE.
    ###############
    def __init__(self,name:str,sex:str = 'MALE') -> None:
        self.__name = name
        self.__sex = sex

    ###############
    # Properies to set Name and Sex.
    ###############
    @property
    def name(self):
        return self.__name
    
    @property
    def sex(self):
        return self.__sex
    

    ###############
    # Overloading over str and repr
    ###############
    def __str__(self) -> str:
        return f"Name: {self.name}, Sex: {self.sex}"
    
    def __repr__(self) -> str:
        return f"Name: {self.name}, Sex: {self.sex}"
    
    ###############
    # Sleep method, all subclases will have it by default, NO NEED TO IMPLEMENTED
    ###############
    def sleep(self):
        print(f"({self.name}) ZzZzZzZ")

    ###############
    # Eat method, all subclases will HAVE TO IMPLEMENT
    ###############
    @abstractmethod
    def eat(self, food:str):
        pass

class Bird(Animal):

    def eat(self, food: str):
        '''
        Out bird eat whatever we give them
        '''
        print(f"({self.name}) Hmmm, Thank you! for the {food} :-) ")

    def wash_yourself(self):
        print(f"({self.name}) I'm cleaning my feathers ")

    def fly(self):
        print(f"({self.name}) I'm flying ")

#####################
### TEST CODE #######

piopio = Bird("PioPio")
piapia = Bird("PiaPia","FEMALE")

print(piopio)
print(piapia)

piopio.eat("Piece of bread")
piapia.eat("Some sunflower's seeds")

piopio.wash_yourself()
piapia.wash_yourself()

piopio.fly()
piapia.fly()
