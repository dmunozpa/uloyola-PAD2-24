# Create a class called "FruitBasket"
class FruitBasket:
    def __init__(self, apples, oranges):
        # Hidden details: store the number of fruits in variables
        self.apples = apples
        self.oranges = oranges
    
    # Method to count how many fruits are in total (Abstraction)
    def count_fruits(self):
        return self.apples + self.oranges
    
    # Method to display the result
    def show_count(self):
        total_fruits = self.count_fruits()
        print(f"There are a total of {total_fruits} fruits in the basket.")
        

# Now let's use this class
my_basket = FruitBasket(apples=3, oranges=5)
my_basket.show_count()
