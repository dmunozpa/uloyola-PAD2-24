class Person:

    def __init__(self, name,age) -> None:
        self.name = name
        self.age = age
        
    #def __str__(self) -> str:
    #    output = ("Name of the Object:"+self.name+"\n")
    #    output += ("Age of the Object:"+str(self.age))
    #    return output

    def __str__(self) -> str:
        result = "Name:"+self.name+" Age:"+str(float(self.age))
        return result
    
    def __repr__(self) -> str:
        result = "Name:"+self.name+" Age:"+str(float(self.age))
        return result


obj = Person("Pepe",18)
obj1 = Person("Tomas",20)

classe = list()

classe.append(obj)
classe.append(obj1)

print(classe)
    