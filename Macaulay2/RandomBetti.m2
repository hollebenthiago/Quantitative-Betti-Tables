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

sizeBettiGraph = method();
sizeBettiGraph(Graph) := (G)->(
	I := edgeIdeal G;
	projdim := pdim coker gens I;
	reg := regularity coker gens I;
	{projdim, reg}
)

numSizeBettiGraph = method();
numSizeBettiGraph(Ring, ZZ, ZZ, Boolean) := (A, variables, repetitions, connected)->(
	mini := variables - 1;
	maxi := binomial(variables, 2) - 1;
	R := A[x_1..x_variables];
	sizes := {};
	for i from mini to maxi do {
		sizeList := {};
		print i;
		for j to repetitions do {
			G := randomGraph(R, i);
			if ((isConnected G and isolatedVertices G == {}) or not connected) then {
				I := edgeIdeal G;
				sizeList = append(sizeList, sizeBettiGraph(G));
			};

			if (j % 100 == 0) then (print j);
		};
		sizes = append(sizes, #(unique sizeList));
		print(i, #(unique sizeList), sizes);
	};
	sizes
)

frequencySizeBettiConnected = method();
frequencySizeBettiConnected(Ring, ZZ, ZZ, ZZ) := (A, variables, e, repetitions)->(
	l := {};
	R := QQ[x_1..x_variables];
	for i from 1 to repetitions do {
		G := randomGraph(R, e);	
		if (isConnected G and isolatedVertices G == {}) then {
			I := edgeIdeal G;
			l = append(l, sizeBettiGraph(G));
		};
		if (i % 100 == 0) then (print i);
	};
	tally l
)

frequencySizeBetti = method();
frequencySizeBetti(Ring, ZZ, ZZ, ZZ) := (A, variables, e, repetitions)->(

	l := {};
	R := QQ[x_1..x_variables];
	for i from 1 to repetitions do {
		G := randomGraph(R, e);	
		I := edgeIdeal G;
		l = append(l, sizeBettiGraph(G));

		if (i % 100 == 0) then (print i);
	};
	tally l
)
