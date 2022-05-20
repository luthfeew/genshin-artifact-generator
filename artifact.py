import math
import numpy as np
from collections import Counter

uid = Element("uid")
hasil = Element("output")
input_cr = Element("inputCR")
input_cd = Element("inputCD")
input_flat_hp = Element("inputFlatHP")
input_hp = Element("inputHP")
input_flat_atk = Element("inputFlatATK")
input_atk = Element("inputATK")
input_flat_def = Element("inputFlatDEF")
input_def = Element("inputDEF")
input_er = Element("inputER")
input_em = Element("inputEM")
input_level = Element("level")

CR = [3.9, 3.5, 3.1, 2.7]
CD = [7.8, 7.0, 6.2, 5.4]
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
MAIN_STAT = {
    10001: "HP",
    10002: "HP Percentage",
    10003: "ATK",
    10004: "ATK Percentage",
    10005: "DEF",
    10006: "DEF Percentage",
    10007: "Energy Recharge",
    10008: "Elemental Mastery",
    13007: "Crit Rate",
    13008: "Crit Damage",
    12009: "Healing Bonus",
    15008: "Pyro DMG Bonus",
    15009: "Electro DMG Bonus",
    15010: "Cryo DMG Bonus",
    15011: "Hydro DMG Bonus",
    15012: "Anemo DMG Bonus",
    15013: "Geo DMG Bonus",
    15014: "Dendro DMG Bonus",
    15015: "Physical DMG Bonus",
}


def calculate(*args, **kwargs):
    all_arrays = []

    def calc(input, stat, cmd):
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

    calc(input_cr.value, CR, CR_CMD)
    calc(input_cd.value, CD, CD_CMD)
    calc(input_flat_hp.value, FLAT_HP, FLAT_HP_CMD)
    calc(input_hp.value, HP, HP_CMD)
    calc(input_flat_atk.value, FLAT_ATK, FLAT_ATK_CMD)
    calc(input_atk.value, ATK, ATK_CMD)
    calc(input_flat_def.value, FLAT_DEF, FLAT_DEF_CMD)
    calc(input_def.value, DEF, DEF_CMD)
    calc(input_er.value, ER, ER_CMD)
    calc(input_em.value, EM, EM_CMD)
    flat_list = []
    for sublist in all_arrays:
        for item in sublist:
            flat_list.append(item)

    count = dict(Counter(flat_list))
    cmd = '/gart xxxxx xxxxx '
    for key, value in count.items():
        if value > 1:
            cmd += (str(key) + ',' + str(value) + ' ')
        else:
            cmd += (str(key) + ' ')

    lvl = int(input_level.value) + 1
    cmd += str(lvl)
    hasil.write(cmd)


def clear(*args, **kwargs):
    input_cr.clear()
    input_cd.clear()
    input_flat_hp.clear()
    input_hp.clear()
    input_flat_atk.clear()
    input_atk.clear()
    input_flat_def.clear()
    input_def.clear()
    input_er.clear()
    input_em.clear()
    hasil.clear()
