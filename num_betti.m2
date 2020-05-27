load("./Macaulay2/RandomBetti.m2"); 
R = QQ; 
rR = "QQ"; 
var = 8; 
rep = 100000; 
badlists = {}; 
for i from 2 to var-1 do { 
   badele = numBettiGraph(R, var, i, rep); 
   badlists = append(badlists, badele); 
print(i)} 
goodl = {} 
for i to #badlists-1 do { 
   goodl = append(goodl, badlists#i); 
} 
file = concatenate("./Simulations/numBetti/", toString(var), "var", "deg", toString(rep), "rep", rR) 
for i to #goodl-1 do{ 
   file << goodl#i << endl; 
} 
file << close; 
exit()