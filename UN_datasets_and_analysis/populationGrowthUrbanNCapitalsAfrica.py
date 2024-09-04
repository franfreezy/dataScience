#import modules
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pandas as pd

#DATA CLEANUP EXERCISE

#path to files
countrycsv='africancounties.csv'
datasetcsv='populationGrowthUrbanandCapitals.csv'

#readcsv
with open(countrycsv, newline='') as csvfile,open(datasetcsv, newline='') as csvfile2:
    reader1 = csv.reader(csvfile)
    reader2 = csv.reader(csvfile2)
    next(reader1) #skips the header
    next(reader2)
    
    country=[]
    
    for row in reader1:
        country.append(row[0])

    for data in reader2:
        countryname=data[1]
        requireddata=[data[1],data[2],data[4],data[6]]
        capitalpopln='Capital city population (thousands)'
        
        
        if countryname in country:
            if capitalpopln in data[3]:

                print(requireddata) # conversion of the data into a dataframe
    

#DATAVISUALISATION
np.random.seed(42) #ensure visualized data is the same all the time
city_bars = 54 # number of bars
city_frames = 20 #rate at which they are scanned, the more, the slower.

