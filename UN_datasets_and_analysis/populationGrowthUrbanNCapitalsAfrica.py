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
    dict18 = {}
    dict05 = {}
    dict15={}
    for row in reader1:
        country.append(row[0])

    for data in reader2:
        countryname=data[1]
        requireddata=[data[1],data[2],data[4],data[6]]
        capitalpopln='Capital city population (thousands)'
        
        
        if countryname in country:
            if capitalpopln in data[3]:
                if (requireddata[1]) == '2015':  # conversion of the data into a dataframe
                    dict15[requireddata[2]] = requireddata[3]
                elif (requireddata[1]) == '2005':
                    dict05[requireddata[2]] = requireddata[3]
                elif (requireddata[1]) == '2018':
                    dict18[requireddata[2]] = requireddata[3]
print(dict18)   
print(dict05)
print(dict15)


#DATAVISUALISATION
np.random.seed(42) #ensure visualized data is the same all the time
city_bars = 54 # number of bars
city_frames = 20 #rate at which they are scanned, the more, the slower.


