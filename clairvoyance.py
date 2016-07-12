from hybrid_ann import *
import argparse

parser = argparse.ArgumentParser(description='Predicts probability of outer companion transiter in system.')
parser.add_argument('-n','--n_inner', type=int, help='Number of planets in system with P < 13.7 days', required=True)
parser.add_argument('-r','--radius', type=float, help='Planet radius', required=True)	
parser.add_argument('-p','--period', type=float, help='Orbital period', required=True) 

args = vars(parser.parse_args())
N_inner = args['n_inner']
R = args['radius']
P = args['period']
P_outer = output(N_inner, R, P)
print "Clairvoyance predicts a %f percent probability of additional transiting planets with P > 13.7 days." % (P_outer) 