class Person:

    def __init__(self,name:str,id:str,age:int):
        self.name = name
        self.id = id
        self.age = age
    
    def copy(self):
        new = Person(self.name,self.id,self.age)
        return new

###############
### EXAMPLE ###
###############

john = Person("John","245995922W",20)

#########
# 1. Copy by Reference 
#########
copy = john
copy.age = 18

###
# The object John has been updated, due to the reference of copy.
print("Copy a variable by REFERENCE makes that the two variables are the SAME object")
print(f"Check John age is: [{john.age}]")
print(f"Check Copy age is: [{copy.age}]" )

#########
# 1. Copy by Copy method. 
#########

copy1 = john.copy()
copy1.age = 24

print("Copy a variable by COPY method makes that the two variables are DIFFERENT objects")
print(f"Check John age is: [{john.age}]")
print(f"Check Copy age is: [{copy1.age}]" )

#######################
# CONCLUSION: Use a copy method if you need a copy of an object, never use reference :D
#######################