class Person:
    
    ## Contructor por defecto
    def __init__(self):

        self.name = ''
        self.surname = ''
        self.age = 0
        self.address = ''
        self.phone_number = 9999999
    
    def __init__(self,name:str, surname:str, age:int):
        
        self.name = name
        self.surname = surname
        self.age = age

        self.address = ''
        self.phone_number = 999999
    
############################
############################

#persona1 = Person()
#persona1.name = "Maria"#
#persona1.age = 14

persona2 = Person("Pepe","Rodriguez",15)

print(persona2)

persona2.address = 'Calle Falsa Nº123'
persona2.phone_number = 965643

print(persona2)

