#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False
    
    if '-input1' in sys.argv:
        for i in range(1,len(sys.argv)):
            InputFile = sys.argv[i]
            haveInput = True
    
    #for i in range(1,len(sys.argv)):
     #   if sys.argv[i] == '-h' or sys.argv[i] == '--help':
      #      continue

       # InputFile = sys.argv[i]
        #haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)
    
    # Code to calculate different quantimes of the assorted arrays of outcomes
    print("times: ", times)
    print("times_avg: ", times_avg)
    
    # Quantiles of Times array
    print("times : ", times)
    print("Q1 quantile of times : ", np.quantile(times, .25))
    print("Q2 quantile of times : ", np.quantile(times, .50))
    print("Q3 quantile of times : ", np.quantile(times, .75))

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
    
    # create histogram of the times (or measurement data)
    n, bins, patches = plt.hist(times, bins=50, density=True, color='lightblue', ec='C0', orientation='vertical', alpha=0.75, label='times')
    #n, bins, patches = plt.hist(times_avg, bins=50, density=True, color='purple', ec='C0', orientation='vertical', alpha=0.75, label='times_avg')

    # plot formating options
    title = 'Cookie Heist Timer Random Sampling of ' + str(Nmeas) + ' measurements'
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title(title, fontsize=12)
    plt.grid(True)
    
    # add vertical lines to show the quantiles:
    plt.axvline(x = np.quantile(times, .25), color = 'c', label = 'Quantile 1')
    plt.axvline(x = np.quantile(times, .50), color = 'y', label = 'Quantile 2')
    plt.axvline(x = np.quantile(times, .75), color = 'm', label = 'Quantile 3')
    #plt.axvline(x = times_avg, color = 'k', label = 'times_avg')
    
    plt.legend()

    # show figure (program only continue once closed)
    plt.show()
    
    
    # create histogram of the times average (datapoints = num of experiment)
    plt.plot(times_avg, color='purple', label='times_avg')

    # plot formating options
    title = 'Cookie Heist Time Average over ' + str(len(times_avg)) + ' experiments'
    plt.xlabel('Average Time', fontsize=12)
    plt.ylabel('Probability', fontsize=12)
    plt.title(title, fontsize=15)
    plt.grid(True)
    
    plt.legend()

    # show figure (program only continue once closed)
    plt.show()

