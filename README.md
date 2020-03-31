# Quantitative-Betti-Tables
Some simulations on the properties of Betti Tables of equigenerated squarefree monomial ideals over a polynomial ring.

The goal of this repository is to run some experiments on the quantitative information of betti tables of a given class of ideals over a polynomial ring. The base ring is almost always a field (unless it's the ring of integers). We say an Ideal I is an equigenerated squarefree monomial ideal if I is generated by squarefree monomials all of the same degree d.

The experiments calculate the betti tables of a given number of randomly generated equigenerated squarefree monomial ideals over a given polynomial ring.

The graphs in the repository are from some experiments that were done, namely:

- What is the most likely Betti Table of equigenerated squarefree monomial ideals if we fix the number of generators, the degree of generators and the base ring? What is its frequency?
- How many different Betti Table are there if we fix the base ring, the number of generators and the degree of such generators?
- If we change the base ring, how different are the results of the question above?


The graphs were made using matplotlib (Python) and the Betti tables were calculated using Macaulay2, including some packages (EdgeIdeals, BoijSoederberg and RandomIdeals)

To dos:

- Change the paths
- Run more experiments
