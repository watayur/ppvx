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






args = sys.argv # [SR, DR w/ DT, OD, max_combo, title(optional)]

sr = float(args[1].replace('"', ''))
sr_dt = float(args[2].replace('"', ''))
od = float(args[3].replace('"', ''))
max_combo = int(args[4].replace('"', ''))
if len(args) == 6:
    title = args[5].replace('"', '')
else:
    title = ""

print("\nSR={:5.2f}, SR w/ DT={:5.2f}, OD={:5.2f}, max_combo={}".format(sr, sr_dt, od, max_combo))
print(' NM     HD     HR     HDHR   FL     DT     HDDT   HRDT   HDHRDT EZDT   EZHDDT')
con = ['FC 100%', 'FC 99%', 'FC 98%', 'FC 97%', 'FC 96%', '1xMiss halfxCOMBO 99%']
acc = [100., 99., 98., 97., 96., 99.]
# NM,HD,HR,HDHR,FL,DT,HDDT,HRDT,HDHRDT,EZDT,EZHDDT
# 100%,99%,98%,97%,96%,99% 1xMISS halfxCOMBO

for i in range(6):

    for j in range(11):
        if j == 0:
            mods = [0, 0, 0, 0, 0, 0, 0]
        elif j == 1:
            mods = [1, 0, 0, 0, 0, 0, 0]
        elif j == 2:
            mods = [0, 1, 0, 0, 0, 0, 0]
        elif j == 3:
            mods = [1, 1, 0, 0, 0, 0, 0]
        elif j == 4:
            mods = [0, 0, 0, 1, 0, 0, 0]
        elif j == 5:
            mods = [0, 0, 0, 0, 1, 0, 0]
        elif j == 6:
            mods = [1, 0, 0, 0, 1, 0, 0]
        elif j == 7:
            mods = [0, 1, 0, 0, 1, 0, 0]
        elif j == 8:
            mods = [1, 1, 0, 0, 1, 0, 0]
        elif j == 9:
            mods = [0, 0, 1, 0, 1, 0, 0]
        elif j == 10:
            mods = [1, 0, 1, 0, 1, 0, 0]

        pp = calc_pp(sr if j <= 4 else sr_dt, od, int(max_combo / 2) if i == 5 else max_combo, 1 if i == 5 else 0, acc[i], mods)
        print("{:>7.1f}".format(pp), end='')

    print("  {}".format(con[i]))

print()

'''
196.3pp
681.1pp
452.7pp
593.6pp
572.5pp
585.7pp
267.8pp
604.6pp
532.6pp
547.1pp
588.4pp
338.1pp
549.7pp
477.3pp
606.3pp
486.8pp
707.0pp
625.3pp
627.1pp
541.4pp
'''