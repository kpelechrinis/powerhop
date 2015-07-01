# powerhop

This repository includes data and code from our study: E. Papalexakis, B. Hooi, K. Pelechrinis and C. Faloutsos, "Power-hop: A Pervasive Observation for Real Complex Networks"

/Data

* power.gml has the power grid network used
* The Gowalla social network used can be found here: https://snap.stanford.edu/data/loc-gowalla.html 
* as20000102.txt has the AS network used
* CA-GrQc.txt and ca-HepTh.txt have the collaborations networks used
* The Facebook social network used can be found here: http://socialnetworks.mpi-sws.org/data-wosn2009.html
* moreno_propro.txt has the metabolic (protein-to-protein interactions) network
* The Yahoo! web graph cannot be made available due to our agreement with Yahoo! However, Yahoo! is providing data access to eligible parties through application on webscope: http://webscope.sandbox.yahoo.com
* The two urban networks were collected by as and can be found in: NYC_net.ncol and SF_net.ncol.  Every line has the format: |node 1|node 2|physical distance between the nodes| The last information was not used in our analysis.  The IDs of the nodes correspond to the actual IDs of the venues on Foursquare
	-- If you use the urban networks please provide the appropriate citation to our work: E. Papalexakis, B. Hooi, K. Pelechrinis and C. Faloutsos, "Power-hop: A Pervasive Observation for Real Complex Networks" --

/Code

* powerhop.py: This script is the one used to obtain the power hop exponent of the real datasets.  The only input it requires is the name of the file that has the network to be examined
* powerhop_ba_synthetic.py: This script was used to obtain the power hop exponent of the synthetic dataset with the BA model.  More details are provided as comments in the script
* powerhop_kronecker_synthetic.py: This script was used to obtain the power hop exponent of the synthetic dataset with the Kronecker model.  We used the kronecker generator from SNAP (https://github.com/snap-stanford/snap/tree/master/examples/krongen) and more details are provided as comments in the script
	-- If you use any of these codes/scripts please provide the appropriate citation to our work: E. Papalexakis, B. Hooi, K. Pelechrinis and C. Faloutsos, "Power-hop: A Pervasive Observation for Real Complex Networks" --
