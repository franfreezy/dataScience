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
csv_file = "capitalcityv1.csv"
#readcsv
with open(countrycsv, newline='') as csvfile,open(datasetcsv, newline='') as csvfile2,open(csv_file, mode='w', newline='') as file:
    reader1 = csv.reader(csvfile)
    reader2 = csv.reader(csvfile2)
    writer = csv.writer(file)
    next(reader1) #skips the header
    next(reader2)
    writer.writerow(['Country', 'year', 'city', 'population', ])
    country=[]
    

    for row in reader1:
        country.append(row[0])

    for data in reader2:
        countryname = data[1]
        capitalpopln='Capital city population (thousands)'
      
        if countryname in country:
            
            if data[4] !='':
                
                if capitalpopln in data[3]:
                    writer.writerow([data[1], data[2], data[4], data[6]])
#version 1 csv generated
v1csv = 'capitalcityv1.csv'
v2csv='output.csv'
with open(v2csv, mode='w', newline='') as csvfile, open(v1csv, newline='') as csvfile2:
    reader=csv.reader(csvfile2)
    writer = csv.writer(csvfile)
    required_years = ['2005', '2010', '2015', '2018']              
     # Write the header
    data_by_country = {}

    for row in reader:
        country, year, city, population = row
        if country not in data_by_country:
            data_by_country[country] = {}
        data_by_country[country][year] = (city, population)
        for country in data_by_country:
            for year in required_years:
                if year not in data_by_country[country]:
                    # Fill missing data with placeholders
                    data_by_country[country][year] = (city, 0)

    for country, years_data in data_by_country.items():
        for year in required_years:
            city, population = years_data[year]
            writer.writerow([country, year, city, population])
    
#refine the output with the blanks filled up                    
                
    
       
               


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


