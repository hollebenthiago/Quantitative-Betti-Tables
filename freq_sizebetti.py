import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci

R  = input('Base ring (QQ, ZZ, or ZZ/p for the finite field ZZ/pZZ): ')
n = int(input('Number of variables: '))
# e = int(input('Number of edges: '))
rep = int(input('Number of repetitions: '))
rR = R.replace('/','_')
isconnected = input('Look for connected graphs only? (y or n)  ')
for e in range(n-1, int(sci.binom(n,2))):
    print(e, int(sci.binom(n,2)))
    f = open('freq_sizebetti.m2', 'w+')
    f.write('load("./Macaulay2/RandomBetti.m2"); \n')
    f.write(f'R = %s; \n' %(R))
    f.write(f'rR = \"%s\"; \n' %(rR))
    f.write(f'var = %s; \n' %(n))
    f.write(f'e = %s; \n' %(e))
    f.write(f'rep = %s; \n' %(rep))
    if isconnected == 'y':
        f.write('l = frequencySizeBettiConnected(QQ, var, e, rep); \n')
    if isconnected == 'n':
        f.write('l = frequencySizeBetti(QQ, var, e, rep); \n')
    f.write('elementsl = unique elements l; \n')
    f.write('file = \"./Simulations/frequencySizeBetti/' + isconnected + str(n) + 'var' + str(e) + 'edges' + str(rep) + 'rep' + rR + '\" \n')
    f.write('for i to #elementsl - 1 do { \n')
    f.write('   file << elementsl#i; \n')
    f.write('   file << \" \"; \n')
    f.write('   file << l#(elementsl#i); \n')
    f.write('   file << "|"; \n')
    f.write('}; \n')
    f.write('file << close; \n')
    f.write('exit();')
    f.close()

    os.system('M2 freq_sizebetti.m2')

all_xs = []
all_ys = []
all_zs = []
all_totals = []

center = [0, 0]
for e in range(n-1, int(sci.binom(n,2))):
    arq = open('./Simulations/frequencySizeBetti/' + isconnected + str(n) + 'var' + str(e) + 'edges' + str(rep) + 'rep' + rR, 'r')

    badyss = arq.read()
    badyss = badyss.replace('{', '').replace('}', '').replace(',', '')
    points = str.split(badyss, '|')[:-1]
    points = [str.split(p, ' ') for p in points]
    xs = [int(p[0]) for p in points]
    ys = [int(p[1]) for p in points]
    zs = [int(p[2]) for p in points]
    new_total = sum(zs)
    
    all_xs += [xs]
    all_ys += [ys]
    all_zs += [zs]
    all_totals += [new_total]
    for x, y, z in zip(xs, ys, zs):
        center[0] += x * z
        center[1] += y * z
    
final_total = sum(all_totals)
center[0] *= 1/final_total
center[1] *= 1/final_total
# colors_needed = len(all_xs)
# cm = plt.get_cmap('gist_rainbow')

fig, ax = plt.subplots(figsize=(15,5))

# ax.set_prop_cycle('color', [cm(1.*i/colors_needed) for i in range(colors_needed)])

title = 'Coordinates of sizes of Betti tables of '
if isconnected == 'y':
    title += 'connected '
title += 'graphs on ' + str(n) + ' variables'
for x, y, z in zip(all_xs, all_ys, all_zs):
    ax.plot(x, y, 'o', color = 'tab:blue')

ax.plot(center[0], center[1], 'o', color = 'tab:green')
mx = max([max(x) for p in all_xs]) + 2
my = max([max(y) for p in all_ys]) + 2
m = max(mx, my)

ax.set_title(title)
ax.set_xlim(0, m)
ax.set_ylim(0, m)

ax.set_xlabel('Projective dimension')
ax.set_ylabel('Regularity')
ax.set_xticks(np.arange(m))
ax.set_yticks(np.arange(m))

ax.grid('on')
plt.savefig('./Simulations_results/Frequency_Sizes_Betti_Tables_' + rR + '/'+ isconnected +str(n)+ '_var_'+str(rep)+'_'+ rR)
plt.show()


