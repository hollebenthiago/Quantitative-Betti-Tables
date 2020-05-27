loadPackage("RandomIdeals", Reload => true);
loadPackage ("BoijSoederberg", Reload => true);
rI = randomIdeal;
rMI = randomMonomialIdeal;
rSFMI = randomSquareFreeMonomialIdeal;
numBetti = method();
numBetti(Sequence,Ring,ZZ,MethodFunction) := (degrees,A,repetitions,function)->(
	l := for j from 1 to repetitions list betti res function(degrees,A);
	{unique l,#(unique l)}
)
simBetti = method();
simBetti(Sequence,Ring,ZZ,MethodFunction) := (degrees,A,repetitions,function)->(
	l := for i from 1 to 10 list (
		(numBetti(degrees,A,repetitions,function))#1
	);
	max l
)
probBetti = method();
probBetti(Sequence,Ring,ZZ,MethodFunction) := (degrees,A,repetitions,function)->(
	bettitables := for i from 1 to repetitions list(
		betti res function(degrees,A)
	) do print i;
	y := tally bettitables;
	q := set bettitables;
	l := toList q;
	sample := for i to #l-1 list (l#i,y_(l#i)/repetitions)
)
numBettiGraph = method();
numBettiGraph(Ring,ZZ,ZZ,ZZ) := (A,variables,degree,repetitions)->(
	D := A[x_1..x_variables];
	maxi := binomial(variables,degree)-1;
	l := for i from 2 to maxi list unique(
	for j from 0 to repetitions list betti res rSFMI(i:degree,D));
	numm := for v from 0 to maxi-2 list #l#v;
	numm 
)

numBettiGraph2 = method();
numBettiGraph2(InexactFieldFamily,ZZ,ZZ,ZZ) := (A,variables,degree,repetitions)->(
	D := A[x_1..x_variables];
	maxi := binomial(variables,degree)-1;
	l := for i from 2 to maxi list unique(
	for j from 0 to repetitions list betti res rSFMI(i:degree,D)) do print(i);
	numm := for v from 0 to maxi-2 list #l#v;
	numm 
)




simBettiGraph = method();
simBettiGraph(Ring,ZZ,ZZ,ZZ) := (A,variables,degree,repetitions)->(	
	D = A[x_1..x_variables];
	l := for i from 1 to 10 list (
		numBettiGraph(D,variables,degree,repetitions) 
	);
	w := transpose l;
	for i from 0 to #w-1 list max w#i 
)
probBettiGraph = method();
probBettiGraph(Ring,ZZ,ZZ,ZZ) := (A,gens,degree,repetitions)->(
	bettitables := for i from 1 to repetitions list(
		betti res rSFMI(gens:degree,A)
	);
	y := tally bettitables;
	q := set bettitables;
	l := toList q;
	sample := for i to #l-1 list (l#i,y_(l#i)/repetitions)
)
randomPureBetti = method();
randomPureBetti(Sequence,Ring,ZZ,MethodFunction) := (degrees,A,repetitions,function)->(
	l := for i from 1 to repetitions list(
		isPure betti res function(degrees,A)
	);
	tally l
)

