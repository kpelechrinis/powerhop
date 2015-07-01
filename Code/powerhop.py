#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
from numpy import log10
import igraph
from scipy import stats

print "Reading network...with diameter"
if '.txt' in sys.argv[1]:
	net = igraph.Graph.Read_Edgelist(sys.argv[1],directed=False)
else:
	if '.gml' in sys.argv[1]:
		net = igraph.Graph.Read_GML(sys.argv[1])
	else:
		if '.net' in sys.argv[1]:
			net = igraph.Graph.Read_Pajek(sys.argv[1])
		if '.xml' in sys.argv[1]:
			net = igraph.Graph.Read_GraphML(sys.argv[1],index=0)
		if '.ncol' in sys.argv[1]:
			net = igraph.Graph.Read_Ncol(sys.argv[1],weights=False,directed=False)

print net.vcount()
if net.is_connected():
	diam = net.diameter(directed=False, unconn=True, weights=None)
	print diam
	print "Calculating shortest paths..."
	d=net.shortest_paths(source=None, target=None, weights=None, mode="ALL")
else:
	print "Calculating LCC..."
	clus = net.clusters()
	gian = clus.giant()
	print gian.vcount()
	d=gian.shortest_paths(source=None, target = None, weights = None, mode="ALL")
	diam = max(max(d))
	print diam

print "Calculating powerhop exponent..."

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
		print "Effective diameter:", r
		break
	else:
		C_r[r-2] = log10(C_r[r-2])
	
gradient, intercept, r_value, p_value, std_err = stats.linregress(r_l,C_r)
print gradient, intercept, r_value


plt.plot(r_l,C_r,"ro")
plt.xlabel('log(r)', fontsize=18)
plt.ylabel('log(C(r))', fontsize=16)
plt.show()

