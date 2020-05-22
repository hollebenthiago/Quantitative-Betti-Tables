restart
load("./RandomBetti.m2");
rR = "Z_2"; -- ring 1
sS = "Z_3"; -- ring 2
var = 7 -- number of variables
deg = 2 -- degree of the generators
R = ZZ/2[x_1..x_var]
S = ZZ/3[x_1..x_var]
rep = 5 -- number of calculations, careful: it may take a long time
llr = for i from 2 to binomial(var,deg)-1 list probBettiGraph(R,i,deg,rep);
print("first ring done")
lr = {}
for i to #llr -1 do {
    qi = for k to #llr#i -1 list (toString llr#i#k#0, toString llr#i#k#1_RR);
    lr = append(lr,qi);	
}

lls = for i from 2 to binomial(var, deg)-1 list probBettiGraph(S,i,deg,rep);
print("second ring done")
ls = {}
for i to #lls-1 do {
    qi = for k to #lls#i -1 list (toString lls#i#k#0, toString lls#i#k#1_RR);
    ls = append(ls, qi)
}
file = concatenate("./Simulations/probBetti/",toString(var), "var",toString(deg), "degprob", toString(rep), "rep",rR,sS)
for i to #lr-1 do{
    for j to #lr#i-1 do{
    	file << lr#i#j#0 << endl;
    	file << lr#i#j#1 << endl;
    };
    file << "!" << endl;   
}
file << "?" << endl;
for i to #ls-1 do{
    for j to #ls#i-1 do{
    	file <<  ls#i#j#0 << endl;
    	file <<  ls#i#j#1 << endl;
    };
    file << "!" << endl;
}
file << close

"ring generators degree repetitions"
