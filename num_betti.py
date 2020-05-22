import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
#os.system('M2 m2teste.m2')

R  = input('Base ring (QQ, ZZ, or ZZ/q for the finite field F_q): ')
n = int(input('Number of variables: '))
rep = int(input('Number of repetitions: '))
rR = R.replace('/','_')
print(rR)
f = open('num_betti.m2', 'w+')
f.write('load("./Macaulay2/RandomBetti.m2"); \n')
f.write(f'R = %s; \n' %(R))
f.write(f'rR = \"%s\"; \n' %(rR))
f.write(f'var = %s; \n' %(n))
f.write(f'rep = %s; \n' %(rep))
f.write('badlists = {}; \n')
f.write('for i from 2 to var-1 do { \n')
f.write('   badele = numBettiGraph(R, var, i, rep); \n')
f.write('   badlists = append(badlists, badele); \n')
f.write('print(i)} \n')
f.write('goodl = {} \n')
f.write('for i to #badlists-1 do { \n')
f.write('   goodl = append(goodl, badlists#i); \n')
f.write('} \n')
f.write("file = concatenate(\"./Simulations/numBetti/\", toString(var), \"var\", \"deg\", toString(rep), \"rep\", rR) \n")
f.write('for i to #goodl-1 do{ \n')
f.write('   file << goodl#i << endl; \n')
f.write('} \n')
f.write('file << close; \n')
f.write('exit()')
f.close()

os.system('M2 num_betti.m2')

arq = open('./Simulations/numBetti/'+str(n)+'vardeg'+str(rep)+'rep'+rR,'r')
yss = []
badyss = arq.read()
badyss = str.split(badyss, '\n')
for i,li in enumerate(badyss):
    badyss[i] = str.split(badyss[i][1:-1], ',')
goodys = badyss[:-1]
goodys = [[int(goodys[j][i]) for i in range(len(goodys[j]))] for j in range(len(goodys))]
print(goodys)

plt.figure(figsize=(15,5))
if len(rR) == 2:
    plt.title('Estimated number of possible Betti tables of equigenerated squarefree monomial ideals in ' + str(n) + ' variables over $\mathbb{'+ rR[0]+'}$')
elif len(rR) > 2:
    plt.title('Estimated number of possible Betti tables of equigenerated squarefree monomial ideals in ' + str(n) + ' variables over $\mathbb{'+ rR[0]+'}' + rR[1:] + '$')
for i,y in enumerate(goodys):
    plt.plot(range(2,int(sci.binom(n,i+2))), y, '--.', label = 'Degree ' + str(i+2))
plt.ylabel('Number of possible Betti tables')
plt.xlabel('Number of generators of the ideals')
plt.xticks(range(2,int(sci.binom(n,int(n//2))),n))
if n == 4:
    plt.yticks([1,2])

plt.legend()
plt.savefig('./Simulations_results/Number_Betti_Tables_' + rR + '/'+str(n)+ '_var_'+'deg_'+str(rep)+'_'+ rR)
plt.show()

    
