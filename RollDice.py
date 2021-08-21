import random
class Dice:
    def roll(self):
        roll_dice = (random.randint(1,6), random.randint(1,6))
        return roll_dice


dice = Dice()
print(dice.roll())
