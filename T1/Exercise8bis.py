##Dice simulator: Write a program that simulates the roll of two dice and calculates the sum of
##the values obtained.

import random

def roll_two_dice():
    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    return dice1,dice2

def main():
 
    dice1, dice2 = roll_two_dice()
    print(f"Sum total: ",dice1+dice2)
    
if __name__ == "__main__":
    main()