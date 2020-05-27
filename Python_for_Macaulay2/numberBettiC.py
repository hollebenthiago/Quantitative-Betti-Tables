import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci

var = int(input("How many variables?"))
rep = int(input("How many uniformly generated ideals?"))
ring1 = str(input("What rings do you want to compare? (first)"))
ring2 = str(input("What rings do you want to compare? (second)"))
ring3 = str(input("What rings do you want to compare? (third)"))

arq1 = open('./Simulations/numBetti/'+str(var)+'vardeg'+str(rep)+'rep'+ring1,'r')
arq2 = open('./Simulations/numBetti/'+str(var)+'vardeg'+str(rep)+'rep'+ring2,'r')
arq3 = open('./Simulations/numBetti/'+str(var)+'vardeg'+str(rep)+'rep'+ring3,'r')

badyss1 = arq1.read()
badyss1 = str.split(badyss1, '\n')
for i,li in enumerate(badyss1):
    badyss1[i] = str.split(badyss1[i][1:-1], ',')
goodys1 = badyss1[:-1]
goodys1 = [[int(goodys1[j][i]) for i in range(len(goodys1[j]))] for j in range(len(goodys1))]

badyss2 = arq2.read()
badyss2 = str.split(badyss2, '\n')
for i,li in enumerate(badyss2):
    badyss2[i] = str.split(badyss2[i][1:-1], ',')
goodys2 = badyss2[:-1]
goodys2 = [[int(goodys2[j][i]) for i in range(len(goodys2[j]))] for j in range(len(goodys2))]

badyss3 = arq3.read()
badyss3 = str.split(badyss3, '\n')
for i,li in enumerate(badyss3):
    badyss3[i] = str.split(badyss3[i][1:-1], ',')
goodys3 = badyss3[:-1]
goodys3 = [[int(goodys3[j][i]) for i in range(len(goodys3[j]))] for j in range(len(goodys3))]


for deg in range(2,var):
    labels = range(2,int(sci.binom(var,deg)))

    width = 0.7
    xs = np.arange(len(goodys1[deg-2]))
    fig, ax = plt.subplots(figsize=(10,5))
    rects1 = ax.bar(xs-width/3, goodys1[deg-2], width/3, label='$\mathbb{'+ring1[0]+'}'+ring1[1:]+'$', color = 'blue')
    rects2 = ax.bar(xs , goodys2[deg-2], width/3, label='$\mathbb{'+ring2[0]+'}'+ring2[1:]+'$', color = 'black')
    rects3 = ax.bar(xs + width/3, goodys3[deg-2], width/3, label='$\mathbb{'+ring3[0]+'}'+ring3[1:]+'$', color = 'yellow')

    ax.set_ylabel('Estimated number of  possible Betti Tables ')
    ax.set_xlabel('Number of generators')
    ax.set_title('Comparing estimated number of possible Betti Tables in ' + str(var) + ' variables between equigenerated ideals of degree ' + str(deg) + 
                 '\n of ' + '$\mathbb{'+ring1[0]+'}'+ring1[1:]+'$, ' + '$\mathbb{'+ring2[0]+'}'+ring2[1:]+'$ and ' + 
                 ' $\mathbb{'+ring3[0]+'}'+ring3[1:]+'$' )
    if deg == var-1:
        plt.yticks([1])

    elif var == 4:
        plt.yticks([1,2])
        
    elif var == 5:
        if ring1 == 'Z' or ring2 == 'Z' or ring3 == 'Z':
            plt.yticks(np.arange(8))
        else:
            plt.yticks(np.arange(5))
    ax.set(xticks = np.arange(2,len(goodys1[deg-2]), var)-2, xticklabels = np.arange(2, len(goodys1[deg-2]), var))
    ax.legend()
    plt.savefig('./Simulations_results/Number_Betti_Comp/'+ring1+ring2+ring3 +'/'+ str(var)+'var_'+str(deg)+'deg_'+str(rep)+'rep_'+ring1+ring2+ring3)
