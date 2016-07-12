from hybrid_ann import *
import sys
from sys import argv

#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

script, N_inner, R, P = argv
N_inner = int(N_inner)
R = float(R)
P = float(P)
P_outer = output(N_inner, R, P)
print "Clairvoyance predicts a %f percent probability of additional transiting planets with P > 13.7 days." % (P_outer)