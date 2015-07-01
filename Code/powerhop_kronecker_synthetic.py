#!/usr/bin/env python

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg
import igraph
from numpy import log, log10
from scipy import stats
import random

fout = open("syntetic_results_kronecker_04.txt","w")
for n in range(100):
	print str(n)+") "+"Generating network...with diameter"
	# Here you define the seed matrix
	seed = 2*(0.4+(0.1*random.random()))
	mat ="0 "+str(0.5*seed)+" "+str(0.5*seed)+" "+str(0.5*seed)+" "+";"+str(0.5*seed)+" "+"0 "+str(0.5*seed)+" "+str(0.5*seed)+" "+";"+str(0.5*seed)+" "+str(0.5*seed)+" "+"0 "+str(0.5*seed)+" "+";"+" "+str(0.5*seed)+" "+str(0.5*seed)+" "+str(0.5*seed)+" "+"0 " 
	# Here we call the kronecker graph generator - we are using the snap library that can be found on github: https://github.com/snap-stanford/snap/tree/master/examples/krongen
	os.system("/Users/kpele/Documents/GitHub/snap/examples/krongen/krongen -o:/Users/kpele/Dropbox/fractaldim-PlosOne/Fractal-dimension-nets/kronecker_graph.txt -m:\""+str(mat)+"\" -i:6")
	# here we need to remove the first 4 lines of the output file of the kronecker graph generated since it includes general information and otherwise will not form an appropriate input for igraph
	no_lines = sum(1 for line in open('kronecker_graph.txt'))
	os.system("tail -"+str(no_lines-4)+" kronecker_graph.txt > kronecker_graph_net.txt")
	net = igraph.Graph.Read_Edgelist("kronecker_graph_net.txt",directed=False)
	if net.is_connected():
		diam = net.diameter(directed=False, unconn=True, weights=None)
		nv = net.vcount()
		print diam
		print str(n)+") "+"Calculating shortest paths..."
		d=net.shortest_paths(source=None, target=None, weights=None, mode="ALL")
	else:
		print "Calculating LCC..."
		clus = net.clusters()
		gian = clus.giant()
		nv = gian.vcount()
		print gian.vcount()
		d=gian.shortest_paths(source=None, target = None, weights = None, mode="ALL")
		diam = max(max(d))
		print diam 
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
		print >> fout,n, gradient, r_value, r, str(0.5*seed),nv
		print n, gradient, r_value, r
		os.system("rm kronecker_graph.txt")
		os.system("rm kronecker_graph_net.txt")
