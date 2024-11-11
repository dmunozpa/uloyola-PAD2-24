import random

class Dice:
    def __init__(self,sides=6) -> None:
        self.sides = sides

    def roll(self)->int:
        return random.randint(1,self.sides)

def simulate_rolling_two_dice(num_rolls:int):
    dice1 = Dice()
    dice2 = Dice()

    for _ in range(num_rolls):
        roll1 = dice1.roll()
        roll2 = dice2.roll()
        print(f"Simulation {_} result: {roll1+roll2}")

# Simulate rolling two dice five times each
simulate_rolling_two_dice(5) 
