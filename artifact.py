import math
import numpy as np

CD = [7.8, 7.0, 6.2, 5.4]
CR = [3.9, 3.5, 3.1, 2.7]
ATK = [5.8, 5.2, 4.7, 4.1]
EM = [23, 21, 19, 16]
ER = [6.5, 5.8, 5.2, 4.5]
HP = [5.8, 5.2, 4.7, 4.1]
DEF = [7.3, 6.6, 5.8, 5.1]
FLAT_ATK = [19, 18, 16, 14]
FLAT_HP = [299, 269, 239, 209]
FLAT_DEF = [23, 21, 19, 16]

def calculate(input, stat):
    if input:
        input = float(input)
        div = input / max(stat)
        med = input / int(math.ceil(div))
            
        def find_nearest(array, value):
            array = np.asarray(array)
            idx = (np.abs(array - value)).argmin()
            return array[idx]

        output = []
        while div > 1:
            output.append(find_nearest(stat, med))
            input = input - find_nearest(stat, med)
            div = div - 1
        while input >= min(stat):
            output.append(find_nearest(stat, input))
            input = input - find_nearest(stat, input)

        output.sort(reverse=True)
        print(output)

print('Welcome to GI Artifact Number Calculator! (Enter to skip)')
while True:
    print('==========================================================')
    calculate(input("Input Crit DMG: "), CD)
    calculate(input("Input Crit Rate: "), CR)
    calculate(input("Input ATK Percentage: "), ATK)
    calculate(input("Input Energy Recharge: "), ER)
    calculate(input("Input Elemental Mastery: "), EM)
    calculate(input("Input HP Percentage: "), HP)
    calculate(input("Input DEF Percentage: "), DEF)
    calculate(input("Input ATK: "), FLAT_ATK)
    calculate(input("Input HP: "), FLAT_HP)
    calculate(input("Input DEF: "), FLAT_DEF)
    print('==========================================================')
    input('Press any key to recalculate...')