import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci

var = int(input("How many variables?"))
rep = int(input("How many randomly generated ideals?"))
ring = input("Over which ring?")
arq = open('./Simulations/numBetti/'+str(var)+'vardeg'+str(rep)+'rep'+ring,'r')
yss = []
badyss = arq.read()
badyss = str.split(badyss, '\n')
for i,li in enumerate(badyss):
    badyss[i] = str.split(badyss[i][1:-1], ',')
goodys = badyss[:-1]
goodys = [[int(goodys[j][i]) for i in range(len(goodys[j]))] for j in range(len(goodys))]
print(goodys)

plt.figure(figsize=(15,5))
plt.title('Estimated number of possible Betti tables of equigenerated squarefree monomial ideals in ' + str(var) + ' variables over $\mathbb{'+ring[0]+'}' + ring[1:] + '$')
for i,y in enumerate(goodys):
    plt.plot(range(2,int(sci.binom(var,i+2))), y, '--.', label = 'Degree ' + str(i+2))
plt.ylabel('Number of possible Betti tables')
plt.xlabel('Number of generators of the ideals')
plt.xticks(range(2,int(sci.binom(var,int(var//2))),var))
if var == 4:
    plt.yticks([1,2])
elif var == 5 and (ring == "Q" or ring == "R" or ring == "C" or  len(ring) > 1):
    plt.yticks([1,2,3,4,5])

plt.legend()
plt.savefig('./Simulation_results/Number_Betti_Tables ' + ring + '/'+str(var)+ '_var_'+'deg_'+str(rep)+'_'+ ring)
plt.show()
