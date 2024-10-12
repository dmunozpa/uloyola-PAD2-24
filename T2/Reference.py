import math;

class Person:
    def __init__(self, name:str, surname:str, age:str, address:str, phone_number:str):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.phone_number = phone_number

    def copy(self):
        new = Person(self.name, self.surname, self.age, self.address, self.phone_number)
        return new

    def __del__(self):
        print("Destructor called")


    def get_name(self)->str:
        return self.name

    def set_name(self, name:str)->None:
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")

# Example usage of the Person class:
john = Person("John", "M", 30, "123 Main St", "555-123-4567")

# 1.- Copy using reference, the two variables are the same, if you change a value in one, the other is updated too.

#copy = john

# 2.- Copy using Copy method, the two variables are different objetcs, if you change a value in one, the other is NOT updated.
copy =  john.copy()

# Test code

copy.age = 12

print(john.age)

