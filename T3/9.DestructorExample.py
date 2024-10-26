class RandomClass:

    def __init__(self,name:str) -> None:
        self.name = name

    #########
    # Overloading for destructor: __del__ method.
    # #######
    def __del__(self):
        print("- Yes! This object has been destroyed my the Gargabe Collector")


################
# TEST CODE ####
################

# Create a random object
toBeDetroy = RandomClass("ToBeDestroyed")

# If we assign to None, it will be removed from memory.
toBeDetroy = None

print("Check if the method has been destroyed")
