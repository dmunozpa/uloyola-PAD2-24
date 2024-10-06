class Person:
    
    ## Contructor por defecto
    def __init__(self):

        self.name = ''
        self.surname = ''
        self.age = 0
        self.address = ''
        self.phone_number = 9999999
    
    ## Contructor con parametros, name, surname, age
    def __init__(self,name:str, surname:str, age:int):
        
        self.name = name
        self.surname = surname
        self.age = age

        self.address = ''
        self.phone_number = 999999
    
    ## Creación del metodo print
    def printScreen(self):

        print("This is the objetct :",self)
        print("[ Name: ",self.name,"]")
        print("[ Surname: ",self.surname,"]")        
        print("[ Age: ",self.age,"]")        
        print("[ Adresss: ",self.address,"]")    

        ## Otra forma de resepresnetar el metodo print
        print(self.surname," ",self.name,",",self.age)    


############################
############################

#persona1 = Person()
#persona1.name = "Maria"#
#persona1.age = 14

persona2 = Person("Pepe","Rodriguez",15)

persona2.address = 'Calle Falsa Nº123'
persona2.phone_number = 965643

persona2.printScreen()
