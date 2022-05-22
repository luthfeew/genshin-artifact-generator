import math
import numpy as np
from collections import Counter
from js import window, document

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
input_artifact = Element("artifact")
input_part = Element("part")
input_main_stat = Element("main_stat")
input_level = Element("level")
input_star = Element("star")

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
ARTIFACT_SET = {
    75004: "Gladiator's Finale",
    77004: "Wanderer's Troupe",
    81004: "Noblesse Oblige",
    82004: "Bloodstained Chivalry",
    88004: "Archaic Petra",
    89004: "Retracing Bolide",
    73004: "Lavawalker",
    80004: "Crimson Witch of Flames",
    72004: "Thundersoother",
    79004: "Thundering Fury",
    93004: "Shimenawa's Reminiscence",
    94004: "Emblem of Severed Fate",
    71004: "Blizzard Strayer",
    90004: "Heart of Depth",
    91004: "Tenacity of the Millelith",
    92004: "Pale Flame",
    95004: "Husk of Opulent Dreams",
    96004: "Ocean-Hued Clam",
    97004: "Vermillion Hereafter",
    98004: "Echoes of an Offering",
    74004: "Maiden Beloved",
    76004: "Viridescent Venerer",
    55004: "Berserker",
    57004: "Instructor",
    59004: "The Exile",
    83004: "Prayers for Illumination",
    84004: "Prayers for Destiny",
    85004: "Prayers for Wisdom",
    86004: "Prayers to Springtime",
    58004: "Gambler",
    62004: "Scholar",
    53004: "Defender's Will",
    51004: "Resolution of Sojourner",
    52004: "Brave Heart",
    56004: "Martial Artist",
    54004: "Tiny Miracle",
    61004: "Lucky Dog",
    60004: "Adventurer",
    63004: "Traveling Doctor",
}
ARTIFACT_PART = {
    40: "Flower of Life",
    20: "Plume of Death",
    50: "Sands of Eon",
    10: "Goblet of Eonothem",
    30: "Circlet of Logos",
}
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

for x, y in ARTIFACT_SET.items():
    option = window.document.createElement("option")
    option.value = x
    option.text = y
    input_artifact.element.appendChild(option)

for x, y in ARTIFACT_PART.items():
    option = window.document.createElement("option")
    option.value = x
    option.text = y
    input_part.element.appendChild(option)

for x, y in MAIN_STAT.items():
    option = window.document.createElement("option")
    option.value = x
    option.text = y
    input_main_stat.element.appendChild(option)


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

    if int(input_artifact.value) == 0 or int(input_part.value) == 0:
        hasil.element.value = "Invalid Artifact! (Please select [artifact] and [part])"
        return
    if len(all_arrays) > 4 or len(all_arrays) == 0 or int(input_main_stat.value) == 0:
        hasil.element.value = "Invalid Artifact! (Please select a [main stat] and [max 4 sub stats])"
        return
    if int(input_level.value) < 1 or int(input_level.value) > 20 or int(input_star.value) < 3 or int(input_star.value) > 5:
        hasil.element.value = "Invalid Artifact! (Please select [level between 1-20] and [star between 3-5])"
        return

    flat_list = []
    for sublist in all_arrays:
        for item in sublist:
            flat_list.append(item)

    count = dict(Counter(flat_list))
    cmd = '/gart '
    cmd += str(int(input_artifact.value) + int(input_part.value) +
               (int(input_star.value) * 100)) + ' '
    cmd += str(input_main_stat.value) + ' '
    for key, value in count.items():
        if value > 1:
            cmd += (str(key) + ',' + str(value) + ' ')
        else:
            cmd += (str(key) + ' ')
    cmd += str(int(input_level.value) + 1)
    hasil.element.value = cmd


def reset():
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


def reset_sub(*args, **kwargs):
    reset()


def reset_all(*args, **kwargs):
    input_artifact.element.selectedIndex = 0
    input_part.element.selectedIndex = 0
    input_main_stat.element.selectedIndex = 0
    input_level.element.value = 20
    input_star.element.value = 5
    reset()


def copy(*args, **kwargs):
    hasil.element.select()
    document.execCommand('copy')
