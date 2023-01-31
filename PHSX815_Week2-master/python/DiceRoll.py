# This code simulates a dice roll that has say 4 sides. A new method has been added to the Random class which generates random numbers according to a categorical distribution. Code was adapted for these purposes from a tutorial on categorical distributions found here: https://www.youtube.com/watch?v=MYHxW-MIld0
# The sides of the dice reads as follows: {0,1,2,3}

#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from Random import Random

# main function for our Dice roll Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)
    
    # default seed
    seed = 5555
    
    # default number of rolls
    n_samples = 10
    
    # default single dice roll probability for hypothesis 0
    p0 = 0.25

    # default single dice roll probability for hypothesis 1
    p1 = 0.25
    
    # default single dice roll probability for hypothesis 2
    p2 = 0.25
    
    # default single dice roll probability for hypothesis 4
    p3 = 0.25

    haveH0 = False
    haveH1 = False
    haveH2 = False
    haveH3 = False
    
    if '-Nroll' in sys.argv:
        p = sys.argv.index('-Nroll')
        Nr = int(sys.argv[p+1])
        if Nr > 0:
            n_samples = Nr
    if '-prob0' in sys.argv:
        p = sys.argv.index('-prob0')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p0 = ptemp
    if '-prob1' in sys.argv:
        p = sys.argv.index('-prob1')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p1 = ptemp
    if '-prob2' in sys.argv:
        p = sys.argv.index('-prob2')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p2 = ptemp
    if '-prob3' in sys.argv:
        p = sys.argv.index('-prob3')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p3 = ptemp
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
    if '-input2' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile2 = sys.argv[p+1]
        haveH2 = True
    if '-input3' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile3 = sys.argv[p+1]
        haveH3 = True
    #if '-h' in sys.argv or '--help' in sys.argv or not haveH0:
        #print ("Usage: %s [options]" % sys.argv[0])
        #print ("  options:")
        #print ("   --help(-h)          print options")
        #print ("   -input0 [filename]  name of file for H0 data")
        #print ("   -input1 [filename]  name of file for H1 data")
        #print ("   -input2 [filename]  name of file for H2 data")
        #print ("   -input3 [filename]  name of file for H3 data")
        #print ("   -prob0 [number]     probability of 1 for single toss for H0")
        #print ("   -prob1 [number]     probability of 1 for single toss for H1")
        #print ("   -prob2 [number]     probability of 1 for single toss for H2")
        #print ("   -prob3 [number]     probability of 1 for single toss for H3")
        #print ("   -Nroll [number]     number of rolls")
        #print
        #sys.exit(1)
        
    # gather probabilities into an array
    thetas = [p0, p1, p2, p3] 
    print(thetas)
    
    # class instance of Random class 
    random = Random(seed)
    
    # Calling for the sampling to be done using the categorical distribution
    arr = random.dist_categorical(thetas, n_samples)
    print(arr)
    
    # Adapting code from Week 1 work below to take this data that has now been randomly sampled according to a categorical distribution
    
    # create histogram of our data
    n, bins, patches = plt.hist(arr, bins=50, density=True, color='lightblue', ec='C0', orientation='vertical', alpha=0.75)

    # plot formating options
    title = 'Categorical Random Sampling for: ' + str(n_samples) + " 4-sided Dice Rolls"
    plt.xlabel('x', color='C0', fontsize=12)
    plt.ylabel('Probability', color='C0', fontsize=12)
    plt.title(title, color='C0', fontsize=15)
    plt.grid(True)

    # show figure (program only ends once closed
    plt.show()