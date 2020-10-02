defense = int(input('Enter your character''s defense: '))

if defense > 0:
    defense_1 = defense * 1
    final = defense_1
if defense > 15:
    defense_2 = (defense - 15) * 0.75 + 15
    final = defense_2
if defense > 30:
    defense_3 = (defense - 30) * 0.5 + 26.25
    final = defense_3
if defense > 45:
    defense_4 = (defense - 45) * 0.25 + 33.75
    final = defense_4
else:
        print('\nNot a valid defense number')
    
print(final)
