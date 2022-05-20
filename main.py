import math
import numpy as np
from collections import Counter

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

CD_CMD = [501224, 501223, 501222, 501221]
CR_CMD = [501204, 501203, 501202, 501201]
ATK_CMD = [501064, 501063, 501062, 501061]
EM_CMD = [501244, 501243, 501242, 501241]
ER_CMD = [501234, 501233, 501232, 501231]
HP_CMD = [501034, 501033, 501032, 501031]
DEF_CMD = [501094, 501093, 501092, 501091]
FLAT_ATK_CMD = [501054, 501053, 501052, 501051]
FLAT_HP_CMD = [501024, 501023, 501022, 501021]
FLAT_DEF_CMD = [501084, 501083, 501082, 501081]

all_arrays = []


def calculate(input, stat, cmd):
    if input:
        input = float(input)
        div = input / max(stat)
        med = input / int(math.ceil(div))

        def find_nearest(array, value):
            array = np.asarray(array)
            idx = (np.abs(array - value)).argmin()
            return array[idx]

        def find_command(array, value):
            array = np.asarray(array)
            idx = (np.abs(array - value)).argmin()
            return cmd[idx]

        output = []
        while div > 1:
            output.append(find_command(stat, med))
            input = input - find_nearest(stat, med)
            div = div - 1
        while input >= min(stat):
            output.append(find_command(stat, input))
            input = input - find_nearest(stat, input)

        output.sort(reverse=True)
        all_arrays.append(output)
        print(output)


print('Welcome to GI Artifact Number Calculator! (Enter to skip)')
while True:
    print('==========================================================')
    calculate(input("Input Crit DMG: "), CD, CD_CMD)
    calculate(input("Input Crit Rate: "), CR, CR_CMD)
    calculate(input("Input ATK Percentage: "), ATK, ATK_CMD)
    calculate(input("Input Energy Recharge: "), ER, ER_CMD)
    calculate(input("Input Elemental Mastery: "), EM, EM_CMD)
    calculate(input("Input HP Percentage: "), HP, HP_CMD)
    calculate(input("Input DEF Percentage: "), DEF, DEF_CMD)
    calculate(input("Input ATK: "), FLAT_ATK, FLAT_ATK_CMD)
    calculate(input("Input HP: "), FLAT_HP, FLAT_HP_CMD)
    calculate(input("Input DEF: "), FLAT_DEF, FLAT_DEF_CMD)
    print('==========================================================')
    flat_list = []
    for sublist in all_arrays:
        for item in sublist:
            flat_list.append(item)

    count = dict(Counter(flat_list))
    cmd = ''
    for key, value in count.items():
        if value > 1:
            cmd += (str(key) + ',' + str(value) + ' ')
        else:
            cmd += (str(key) + ' ')
    print(cmd)
    print('==========================================================')
    input('Press any key to recalculate...')
