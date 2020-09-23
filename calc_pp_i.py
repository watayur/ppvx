# 300_range: [49.5 - int(ceil(OD * 3))]
# OD6+HR (23.5 ms), OD5+DT (23 ms) as a threshold
# 最大コンボ数依存
# SR1 SS→10pp, SR6 SS→300pp

import sys
import math
import numpy as np

# mods = [HD, HR, EZ, FL, DT, HT, NF]
def calc_pp(sr, od, max_combo, misses, acc, mods):
    #strain
    strain = pow(sr / 10, 3)
    strain *= (1 - (misses / 70))
    strain *= min(pow(2500, 0.11), pow(max_combo, 0.11))
    strain *= 1.5

    if mods[0] == 1:
        strain *= 1.1
    if mods[1] == 1:
        strain *= 1.1   
    if mods[2] == 1:
        strain *= 0.9
    if mods[3] == 1:
        strain *= 1.05 + (0.01 * min(pow(2500, 0.1), pow(max_combo, 0.1)))


    #accuracy
    if mods[1] == 1:
        od = min(10, od * 1.4)
    elif mods[2] == 1:
        od *= 0.5
    
    accuracy = 49.5 - int(math.ceil(od * 3))

    if mods[4] == 1:
        accuracy /= 1.5
    if mods[5] == 1:
        accuracy /= 0.75

    
    accuracy = 1 / (pow(accuracy, 5) / 10) + 0.00001

    accuracy *= pow(acc / 100, 30)
    accuracy *= min(pow(2500, 0.1), pow(max_combo, 0.1))

    accuracy *= 15000

    #print("strain = {:>12.6f}".format(strain))
    #print("acuracy = {:>12.6f}".format(accuracy))

    pp = pow(strain + accuracy, 1.25) * 300

    if mods[6] == 1:
        return pp * 0.9
    return pp






args = sys.argv # [SR, OD, max_combo, misses, acc, mods(0 or 1)]

sr = float(args[1].replace('"', ''))
od = float(args[2].replace('"', ''))
max_combo = int(args[3].replace('"', ''))
misses = int(args[4].replace('"', ''))
acc = float(args[5].replace('"', ''))
hd = float(args[6].replace('"', ''))
hr = float(args[7].replace('"', ''))
ez = float(args[8].replace('"', ''))
fl = float(args[9].replace('"', ''))
dt = float(args[10].replace('"', ''))
ht = float(args[11].replace('"', ''))
nf = float(args[12].replace('"', ''))

print('{:>6.1f}'.format(calc_pp(sr, od, max_combo, misses, acc, [hd, hr, ez, fl, dt, ht, nf])))


#for i in range(201):
    #print('{:>4.1f}* : {:>6.1f}'.format(i/10, calc_pp(i/10, 6, 1000, 0, 100, [0,0,0,0,0,0,0])))