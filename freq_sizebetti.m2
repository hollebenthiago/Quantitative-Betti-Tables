load("./Macaulay2/RandomBetti.m2"); 
R = QQ; 
rR = "QQ"; 
var = 9; 
e = 35; 
rep = 100000; 
l = frequencySizeBettiConnected(QQ, var, e, rep); 
elementsl = unique elements l; 
file = "./Simulations/frequencySizeBetti/y9var35edges100000repQQ" 
for i to #elementsl - 1 do { 
   file << elementsl#i; 
   file << " "; 
   file << l#(elementsl#i); 
   file << "|"; 
}; 
file << close; 
exit();