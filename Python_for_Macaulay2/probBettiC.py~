import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

var = int(input("How many variables?"))
deg = int(input("What degree?"))
rep = int(input("How many randomly generated ideals?"))
rR = input("Compare which rings (first)?")
sS = input("Compare which rings (second)?")
sizefont = int(input("Size font:"))
M = int(input("Beginning of table:"))-2
N = int(input("End of table:"))-2

rcParams['font.family'] = 'serif'
rcParams['font.size'] = sizefont

arq = open('/home/tholleben/Desktop/Álgebra/Macaulay2/probBetti/'+str(var)+'var'+str(deg)+'degprob'+str(rep)+'rep'+rR+sS,'r')



def convert(string):
    string = string[21:-1]
    l = str.split(string,', ')
    for i,L in enumerate(l):
        l[i] = str.split(L, ' => ')
    for i,L in enumerate(l):
        l[i][0] = str.split(L[0][1:-1], ',')[0::2]
    for i in range(len(l)):
        l[i][1] = int(l[i][1])
        l[i][0][0] = int(l[i][0][0])
        l[i][0][1] = int(l[i][0][1])
    return l

def makeTable(string):
    l = convert(string)
    m = max([l[i][0][0] for i in range(len(l))])
    n = max([l[i][0][1] for i in range(len(l))])-m
    v = np.array([l[i][0][0] for i in range(len(l))])
    w = np.array([l[i][0][1] for i in range(len(l))])
    A = np.zeros((n+6,m+1))
    for i in range(len(l)):
        j = l[i][0][0]
        k = l[i][0][1]
        A[k-j][j] = l[i][1]
    c = -1
    while all(A[-1] == np.zeros(m+1)):
        A = A[:-1]
        c -= 1
    s = '       '
    m = len(A[0])
    n = len(A)
    totalbet = [sum(l) for l in A.T]
    for i in range(m):
        if 10 <= totalbet[i] < 100 :
            s = s + ' ' + str(i) + '  '
        elif totalbet[i] >= 100:
            s = s + ' ' + str(i) + '   '
        else:
            s = s + ' ' + str(i) + ' '
    s = s + ' \n total:'
    for i,t in enumerate(totalbet):
        s = s + ' ' + str(int(t)) + ' '
    s = s + ' \n '
    for i in range(n):
        s = s + '    ' + str(int(i)) + ':'
        for j in range(m):
            if A[i][j] == 0:
                if totalbet[j] < 100:
                    if totalbet[j] < 10:
                        s = s + ' . '
                    else:
                        s = s + ' .  '
                else: 
                    if totalbet[j] < 100:
                        if totalbet[k] < 10:
                            s = s + ' . '
                        else:
                            s = s + ' . '
                    else:
                        s = s + ' .   '
            else:
                if totalbet[j] < 10 and A[i][j] < 10:
                    s = s + ' ' + str(int(A[i][j])) + ' '

                else:
                    if totalbet[j] < 10 or A[i][j] < 10:
                        s = s + ' ' + str(int(A[i][j])) + '  '
                    else:
                        if totalbet[j] < 100 and A[i][j] < 100:
                            s = s + ' ' + str(int(A[i][j])) + ' '
                        elif totalbet[j] >= 100 and A[i][j] >= 100:
                            s = s + ' ' + str(int(A[i][j])) + ' '
                        else:
                            s = s + ' ' + str(int(A[i][j])) + '  '
        s = s + ' \n '
    
    return s

badyss = arq.read()
badyss = str.split(badyss,'\n?\n')
byss1 = str.split(badyss[0], '\n!\n')
byss2 = str.split(badyss[1],'\n!\n')[:-1]
byss1 = [str.split(yss1, '\n') for yss1 in byss1]
byss1[-1] = byss1[-1][:-1]
byss2 = [str.split(yss2, '\n') for yss2 in byss2]

tables1 = [[makeTable(v) for v in ys1[::2]] for ys1 in byss1]
probs1 = [ys1[1::2] for ys1 in byss1]
m1 = [y1.index(max(y1)) for y1 in probs1]
tables2 = [[makeTable(v) for v in ys2[::2]] for ys2 in byss2]
probs2 = [ys2[1::2] for ys2 in byss2]
m2 = [y2.index(max(y2)) for y2 in probs2]

B = [[v[m1[i+M]] for i,v in enumerate(tables1[M:N]) ], [v[m2[i+M]] for i,v in enumerate(tables2[M:N])]]

rings = ['$\mathbb{'+rR+'}[x_1...x_'+str(var)+']$', '$\mathbb{'+sS+'}[x_1...x_'+str(var)+']$']
gens = [str(i+M+2)+' generators, frequencies: \n' + rings[0] + ' - ' + str(float(probs1[i+M][m1[i+M]])) +  ' \n'+ rings[1] + ' - ' + str(float(probs2[i+M][m2[i+M]])) for i in range(len(tables1[M:N]))]

m = len(rings)
n = len(gens)
xx = int(input("Size of table (x axis):"))
yy = int(input("Size of table (y axis):"))
plt.figure(figsize=(n+xx,m+yy))
for krow, row in enumerate(B):
    plt.text(5, 10*krow + 15, rings[krow],
             horizontalalignment='center',
             verticalalignment='center')
    for kcol, num in enumerate(row):
        if krow == 0:
            plt.text(10*kcol + 15, 5, gens[kcol],
                     horizontalalignment='center',
                     verticalalignment='center')
        plt.text(10*kcol + 15, 10*krow + 15, num,
                 horizontalalignment='center',
                 verticalalignment='center')
plt.title('Tables with higher frequency')
plt.axis([0, 10*(n + 1), 10*(m + 1), 0])
plt.xticks(np.linspace(0, 10*(n + 1), n + 2), [])
plt.yticks(np.linspace(0, 10*(m + 1), m + 2), [])
plt.grid(linestyle="solid")
plt.savefig("/home/tholleben/Desktop/experiments/Prob Betti Tables/"+str(var) + "_var_" + str(deg) + "_deg_"+str(rep)+"_rep_prob_"+str(M+2)+"_beg_"+str(N+2)+"_end_"+ rR + sS + ".png" , dpi=300)
plt.show()
