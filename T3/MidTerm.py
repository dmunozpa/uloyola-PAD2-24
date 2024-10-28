class Publication:
    def __init__(self, title, authors, year, status="available"):
        self.title = title
        self.authors = authors
        self.year = year
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.authors} ({self.year})"
    
    def __repr__(self):
        return f"{self.title} - {self.authors} ({self.year})"

class Book(Publication):
    def __init__(self, title, authors, year, ISBN, pages, status="available"):
        super().__init__(title, authors, year, status)
        self.ISBN = ISBN
        self.pages = pages

class Journal(Publication):
    def __init__(self, title, authors, year, edition, periodicity, status="available"):
        super().__init__(title, authors, year, status)
        self.edition = edition
        self.periodicity = periodicity

class User:
    def __init__(self, name, userID):
        self.name = name
        self.userID = userID
        self.pubs = []

    def lend_pub(self, publication):
        if publication.status == "available" and len(self.pubs) < self.max_pubs:
            publication.status = "borrowed"
            self.pubs.append(publication)
            print(f"The Book '{publication.title}' has been lent to {self.name}.")
        else:
            if publication.status != "available":
                print(f"The Book '{publication.title}' is not available.")
            else:
                print(f"{self.name} has reached the maximum limit of borrowed items.")

    def return_pub(self, publication):
        if publication in self.pubs:
            publication.status = "available"
            self.pubs.remove(publication)
            print(f"The Book '{publication.title}' was returned by {self.name}.")
        else:
            print(f"{self.name} does not have '{publication.title}' borrowed.")

class Professor(User):
    def __init__(self, name, userID, department, employeeID, max_pubs=2):
        super().__init__(name, userID)
        self.department = department
        if(len(employeeID) is 6):
            self.employeeID = employeeID
        else:
            raise Exception(" EmployeeeID "+employeeID+" is not len 6 ")
        self.max_pubs = max_pubs

class Student(User):
    def __init__(self, name, userID, grade, studentID, max_pubs=1):
        super().__init__(name, userID)
        self.grade = grade
        self.studentID = studentID
        self.max_pubs = max_pubs

class Library:
    def __init__(self, name):
        self.name = name
        self.catalogue = []
        self.users = []

    def show_catalogue(self):
        print(f"Catalogue of the library: {self.name}")
        print("--------------------------------------------------")
        for pub in self.catalogue:
            print(pub)
        print("--------------------------------------------------")

    def add_publication(self, publication):
        self.catalogue.append(publication)

    def register_user(self, user):
        self.users.append(user)

    def lend_pub(self, user, publication):
        if user not in self.users:
            print(f"The user or publication is not registered")
        elif publication not in self.catalogue:
            print(f"The user or publication is not registered")
        else:
            user.lend_pub(publication)

    def return_pub(self, user, publication):
        if user in self.users and publication in self.catalogue:
            user.return_pub(publication)
        else:
            print("The user or publication is not registered")

#########################
###### TEST CODE ########
#########################
library = Library("Loyola Andalucía Library")

book1 = Book("Learning Python II", ["Javier Perez", "Daniel Muñoz"], 2023, "1234567890123", 300)
journal1 = Journal("Technology Journal", ["Stephen Curry", "LeBron James"], 2022, 7, "Annual")
journal2 = Journal("Medical Journal", ["Michael Jordan", "Larry Bird"], 2023, 5, "Monthly")

professor1 = Professor("Professor Tija", "123456789", "Philosophy", "123456")
student1 = Student("Ashkabos Teberio", "987654321", "DAN", "654321")
student2 = Student("Rachel Tonali", "656565656", "ADE+DAN", "454322")

library.add_publication(book1)
library.add_publication(journal1)
library.add_publication(journal2)

library.register_user(professor1)
library.register_user(student1)

library.show_catalogue()

library.lend_pub(professor1, book1)        
library.lend_pub(student1, book1)          
print(student1.pubs)                       

library.return_pub(professor1, book1)      
library.lend_pub(student1, book1)          
library.lend_pub(student1, journal2)       

print(student1.pubs)

library.lend_pub(student2, journal1)       
