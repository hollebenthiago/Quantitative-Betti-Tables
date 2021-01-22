load("./Macaulay2/RandomBetti.m2"); 
R = QQ; 
rR = "QQ"; 
var = 8; 
rep = 80000; 
isconnected = true;l = numSizeBettiGraph(R, var, rep, isconnected) 
file = concatenate("./Simulations/numSizeBetti/", y,toString(var), "var", toString(rep), "rep", rR) 
file << l << endl; 
file << close; 
exit()