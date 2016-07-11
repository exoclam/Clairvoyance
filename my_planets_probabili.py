# type python my_planets_probabili.py on your command line to estimate how likely your planet
# has another planet in its system with orbital period greater than 13.7 days
from hybrid_ann import *
from sys import argv

#script, user_name = argv
prompt = '> '

#print "Hi %s, I'm the %s script." % (user_name, script)
print "How many transiting planets detected with P < 13.7 days?"
N_inner = int(raw_input(prompt))

print "Radius, in Earth radii, of planet 1?"
R = float(raw_input(prompt))

print "Period, in days, of planet 1?"
P = float(raw_input(prompt))

print ""
P_outer = output(N_inner, R, P)
print "Clairvoyance predicts a %f percent probability of additional transiting planets with P < 13.7 days." % (P_outer)