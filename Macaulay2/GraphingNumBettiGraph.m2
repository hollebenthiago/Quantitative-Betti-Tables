restart
load("./RandomBetti.m2");
R = QQ;
rR = "QQ";
var = 5
rep = 15
badlists = {}
for i from 2 to var-1 do{
    badele = numBettiGraph(R,var,i,rep);
    badlists = append(badlists,badele);
    print(i)
}
badlists
goodl = {}
for i to #badlists-1 do{
     goodl = append(goodl, badlists#i);
}
goodl

file = concatenate("./Simulations/numBetti/",toString(var), "var", "deg", toString(rep), "rep", rR)
for i to #goodl-1 do{
    file << goodl#i << endl;
}
file << close;

exit()