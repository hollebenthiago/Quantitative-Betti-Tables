import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
#os.system('M2 m2teste.m2')

R  = input('Base ring (QQ, ZZ, or ZZ/p for the finite field ZZ/pZZ): ')
n = int(input('Number of variables: '))
rep = int(input('Number of repetitions: '))
rR = R.replace('/','_')
isconnected = input('Look for connected graphs only? (y or n)  ')
f = open('num_sizebetti.m2', 'w+')
f.write('load("./Macaulay2/RandomBetti.m2"); \n')
f.write(f'R = %s; \n' %(R))
f.write(f'rR = \"%s\"; \n' %(rR))
f.write(f'var = %s; \n' %(n))
f.write(f'rep = %s; \n' %(rep))
if isconnected == 'y':
    f.write(f'isconnected = true;')
if isconnected == 'n':
    f.write(f'isconnected = false;')
f.write(f'l = numSizeBettiGraph(R, var, rep, isconnected) \n')
f.write(f"file = concatenate(\"./Simulations/numSizeBetti/\", %s,toString(var), \"var\", toString(rep), \"rep\", rR) \n" %(isconnected))
f.write('file << l << endl; \n')
f.write('file << close; \n')
f.write('exit()')
f.close()

os.system('M2 num_sizebetti.m2')

arq = open('./Simulations/numSizeBetti/' + isconnected +str(n)+'var'+str(rep)+'rep'+rR,'r')
yss = []
badyss = arq.read()
ys = str.split(badyss[1:-2], ',')
ys = [int(y) for y in ys] + [1]
xs = np.arange(n - 1, int(sci.binom(n,2) + 1))
plt.figure(figsize=(15,5))
title = 'Estimated number of possible sizes of Betti tables of '
if isconnected == 'y':
    title += 'connected '
if len(rR) == 2:
    plt.title( title + 'graphs in ' + str(n) + ' variables over $\mathbb{'+ rR[0]+'}$')
if len(rR) > 2:
    plt.title( title + 'graphs in ' + str(n) + ' variables over $\mathbb{'+ rR[0]+'}' + rR[2:] + '$')

plt.plot(xs, ys, '-o')

plt.ylabel('Number of possible sizes of Betti tables')
plt.xlabel('Number of edges')
plt.xticks(xs)
if n == 4:
    plt.yticks([1,2])

plt.savefig('./Simulations_results/Number_Sizes_Betti_Tables_' + rR + '/'+ isconnected +str(n)+ '_var_'+str(rep)+'_'+ rR)
plt.show()

    
