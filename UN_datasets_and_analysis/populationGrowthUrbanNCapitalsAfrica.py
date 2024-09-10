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
csv_file = "popgrowthcapitals/capitalcityv1.csv"
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
v1csv = 'popgrowthcapitals/capitalcityv1.csv'
v2csv='popgrowthcapitals/output.csv'
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
v1csv = 'popgrowthcapitals/output.csv'
v2csv='popgrowthcapitals/output1.csv'
with open(v2csv, mode='w', newline='') as csvfile, open(v1csv, newline='') as csvfile2:
    reader = list(csv.reader(csvfile2))
    writer = csv.writer(csvfile)               
    writer.writerow(['Country', 'year', 'city', 'population',])
    writer.writerows(reader[4:])
       
#### making the data meaningful               
csvfile = 'popgrowthcapitals/output1.csv'
csvfile2='popgrowthcapitals/final.csv'
with open(csvfile2, mode='w', newline='') as csvfile2, open(csvfile, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    writer = csv.writer(csvfile2)
    writer.writerow(['capital', '2005', '2010', '2015', '2018'])
    dict05 = {}
    dict10 = {}
    dict15 = {}
    dict18 = {}
    dictfinal = {}
    rows = list(reader)
    hashlist=list()
    for row in rows:
        country = row[0]
        city = row[2]
        population = row[3]

        if row[1] == '2005':
            dict05[row[2]] = row[3]
        elif row[1] == '2010':
            dict10[row[2]] = row[3]
        elif row[1] == '2015':
            dict15[row[2]] = row[3]
        elif row[1] == '2018':
            dict18[row[2]]=row[3]
    
    for row in rows:
        country = row[0]
        city = row[2]
        
        
        dictfinal[city] = [dict05.get(city), dict10.get(city),dict15.get(city), dict18.get(city)]
        writer.writerow([city, dict05.get(city), dict10.get(city),dict15.get(city), dict18.get(city)])
     
    
csv_file = "output2.csv" # final, well sorted csv

# Writing the dictionary to a CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['capital', '2005', '2010', '2015', '2018'])
    for key in list(dictfinal.keys()):
        writer.writerow([key, dictfinal[key][0], dictfinal[key][1], dictfinal[key][2], dictfinal[key][3]])

 
#DATAVISUALISATION
np.random.seed(42) #ensure visualized data is the same all the time
city_bars = 54 # number of bars
city_frames = 20 #rate at which they are scanned, the more, the slower.


