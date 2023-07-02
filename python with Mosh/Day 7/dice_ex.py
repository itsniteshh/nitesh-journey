import random


class Dice:
    
    def roll(self):
        
        final = []
        
        for i in range(2):
            values = random.randint(1, 6)
            final.append(values)
        
        return tuple(final)
    

dic_value = Dice()
print(dic_value.roll())

