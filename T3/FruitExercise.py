class Fruit:

    def __init__(self, color:str) -> None:
        self.color = color
        self.prize = 0
        pass
    
    def makeJuice(self) -> str:
        return "This fruit doesnt have juice"
    
    def __str__(self) -> str:
        result = "The fruit is "+self.color+" and the cost is "+str(self.prize)
        return result
    
    def __repr__(self) -> str:
        result = "The fruit is "+self.color+" and the cost is "+str(self.prize)
        return result

class Apple(Fruit):

    def __init__(self, color:str,seeds:int ) -> None:
        super().__init__(color)
        self.seeds = seeds
    
    def makeJuice(self) -> str:
        if self.seeds > 5:
            return "The juice is super cider !!"
        else:
            return "The juice is cider"

class Pear(Fruit):

    def __init__(self, color: str, size:str) -> None:
        super().__init__(color)
        self.size = size

class Grape(Fruit):

    def __init__(self, color: str, region:str, type:str) -> None:
        super().__init__(color)
        self.region = region
        self.type = type

    def makeJuice(self) -> str:
        if self.color is 'red':
            juice = 'Tinto'
        if self.color is 'green':
            juice = 'Blanco'
        return juice
    
    def __str__(self) -> str:
        typeOfFruit = self.__class__.__name__
        result = "This is a ["+typeOfFruit+"] and is "+self.color+" and is from "+self.region
        return result
    
    def __repr__(self) -> str:
        typeOfFruit = self.__class__.__name__
        result = "This is a ["+typeOfFruit+"] and is "+self.color+" and is from "+self.region
        return result
    
    def __del__():
        print(" Object Deleted")
        

###################

goldenApple = Apple('green',4)
redApple = Apple('red',8)

cider1 = goldenApple.makeJuice()
cider2 = redApple.makeJuice()


print(cider1)
print(cider2)

#######################

myPoorPear = Pear('green','big')

pearJuice = myPoorPear.makeJuice()

print(pearJuice)

#######################

grape1 = Grape('green','Sevilla','dulce')

# For the redApple object, the method will be the father class - Fruit.
print(redApple)

# For the myPoorPear object, the method will be the father class - Fruit.
print(myPoorPear)

# For the grape1 object, the method will be him method.
print(grape1)


