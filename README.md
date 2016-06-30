# (Transit) Clairvoyance
## Predicting multiple-planet systems for TESS

In 2017, TESS (Transiting Exoplanet Survey Satellite) will launch, marking a transition from the wide-apertured, long-staring capabilities of Kepler to the sweeping gaze of a new mission able to capture much more of the sky, at the expense of resolution and the chances of longer-period planet follow-up.

Transit Clairvoyance uses Artificial Neural Networks (ANNs) to predict the most likely short period transiters to have additional transiters, thereby doubling the discovery yield of a mock transit follow-up survey. The training and cross-validation were done by splitting the Kepler exoplanet data archive (http://exoplanetarchive.ipac.caltech.edu/, accessed May 17, 2016) and the features selected for an initial 2-feature ANN were the planetary radius and orbital period, while a binary inner multiplicity flag (ie. 0 for no planet with orbital period P < 13.7 days in the system; 1 otherwise) was added for a 3-feature ANN that we eventually combined with the 2-feature into a hybrid. From the 2- and 3-feature ANNs, class probabilities were generated to describe how likely a system was to have exoplanets with P > 13.7. For a more detailed description of how these probabilities were generated, see Kipping & Lam 2016. 

The 2- and 3-feature ANN results are displayed in the correspondingly named tables. In both, the columns are, in order:
- Log10( Radius [Earth radii] )
- Log10( Period of maximum sized planets )
- Probability of system having an outer transiter (0-1)

##Hybrid ANN

[A look at the hybrid architecture.](HybridANN.png)


