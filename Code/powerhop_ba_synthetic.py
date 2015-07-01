#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg
import igraph
from numpy import log, log10
from scipy import stats
import random

# fout is the file with the results for your 
fout = open("syntetic_results_ba_m2_p1.txt","w")

for n in range(100):
	print str(n)+") "+"Generating network"
	net = igraph.Graph.Barabasi(n=10000,m=2,power=1,directed=False)
	diam = net.diameter(directed=False, unconn=True, weights=None)
	d=net.shortest_paths(source=None, target=None, weights=None, mode="ALL")

	print str(n)+") "+"Calculating powerhop exponent..."

	C_r = []
	r_l = []

	for r in range(2,diam+1):
		r_l.append(log10(r))
		C_r.append(0)
		for i in range(len(d)):
			C_r[r-2] = C_r[r-2]+len([j for j in d[i] if j <= r])
		C_r[r-2] = float(C_r[r-2])/(len(d)*(len(d)-1))
		if C_r[r-2] >= 0.9:
			C_r[r-2] = log10(C_r[r-2])
			break
		else:
			C_r[r-2] = log10(C_r[r-2])
	if r > 3:
		gradient, intercept, r_value, p_value, std_err = stats.linregress(r_l,C_r)
		r_real = r
		diam_real = diam
		print >> fout,n, gradient, r_value, r
		print n, gradient, r_value, r
