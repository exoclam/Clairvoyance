from hybrid_ann import *
import argparse

parser = argparse.ArgumentParser(description='Predicts probability of outer companion transiter in system.')
parser.add_argument('-n','--n_inner', type=int, help='Number of planets in system with P < 13.7 days', required=True)
# add_arguments for up to three inner transiters
for i in range(1,4):
	parser.add_argument('-r%d' % i,'--radius%d' % i, type=float, help='Planet radius')	
	parser.add_argument('-p%d' % i,'--period%d' % i, type=float, help='Orbital period') 

args = vars(parser.parse_args())
N_inner = args['n_inner']
R = []
P = []
# find max R of inner transiter(s)
for i in range(1,4):
	R.append(args['radius%d' % i])
Rmax = max(R)

# get ID of transiter with maximum radius
k = R.index(max(R))

# find P of inner transiter with max R
for i in range(1,4):
	P.append(args['period%d' % i])
P_Rmax = P[k]
P_outer = output(N_inner, Rmax, P_Rmax)
print "Clairvoyance predicts a %f percent probability of additional transiting planets with P > 13.7 days." % (P_outer) 