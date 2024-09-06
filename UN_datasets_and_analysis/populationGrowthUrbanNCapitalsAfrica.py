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
    dict15 = {}
    dict10 = {}

    for row in reader1:
        country.append(row[0])

    for data in reader2:
        countryname = data[1]
        
        requireddata = [data[1], data[2], data[4], data[6]]
        capitalpopln='Capital city population (thousands)'
        
        
        if countryname in country:
          
            if capitalpopln in data[3]:
                print(countryname,data[2])
            keys=list(dict18.keys())
            
            if (requireddata[1]) == '2015':
                pass
        else:
            pass       
    
           
                


csv_file = "output.csv"

# Open the file in write mode
#with open(csv_file, mode='w', newline='') as file:
#    writer = csv.writer(file)
#    
#   
#    writer.writerow(['City', '2005', '2010', '2015', '2018',])
#    
#   
#    for (key1, value1), (key2, value2), (key3, value3), (key4, value4) in zip(dict05.items(), dict10.items(), dict15.items(), dict18.items()):
#        writer.writerow([key1, value1,key2,  value2,key3, value3,key4,value4])
 
#DATAVISUALISATION
np.random.seed(42) #ensure visualized data is the same all the time
city_bars = 54 # number of bars
city_frames = 20 #rate at which they are scanned, the more, the slower.


