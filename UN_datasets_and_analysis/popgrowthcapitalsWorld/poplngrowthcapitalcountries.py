#population changes across all capital cities in the world

#import modules
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pandas as pd

#DATA CLEANUP EXERCISE

#path to files
datasetcsv='../populationGrowthUrbanandCapitals.csv'
csv_file = "capitalcityv1.csv"

#readcsv
with open(datasetcsv, newline='') as csvfile,open(csv_file, mode='w', newline='') as file:
    reader = csv.reader(csvfile)
    writer = csv.writer(file)
    next(reader)
    writer.writerow(['Country', 'year', 'city', 'population', ])
    
    for data in reader:
        countryname = data[1]
        capitalpopln = 'Capital city population (thousands)'
        if capitalpopln in data[3]:
            writer.writerow([data[1], data[2], data[4], data[6]])

csv_file = "capitalcityv1.csv"
csv_file2 = 'output.csv'
with open(csv_file2, mode='w', newline='') as csvfile, open(csv_file, newline='') as csvfile2:
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

v1csv = 'output.csv'
v2csv='output1.csv'
with open(v2csv, mode='w', newline='') as csvfile, open(v1csv, newline='') as csvfile2:
    reader = list(csv.reader(csvfile2))
    writer = csv.writer(csvfile)               
    writer.writerow(['Country', 'year', 'city', 'population',])
    writer.writerows(reader[4:])

csvfile = 'output1.csv'
csvfile2 = 'final.csv'
csvfile3= 'output3.csv'
with open(csvfile2, mode='w', newline='') as csvfile2, open(csvfile, newline='') as csvfile,open(csvfile3, mode='w', newline='') as file:
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
        writer.writerow([city, dict05.get(city), dict10.get(city), dict15.get(city), dict18.get(city)])
    writer3 = csv.DictWriter(file, fieldnames=dictfinal.keys())
    
    writer3.writeheader()  # Write the header (keys)
    
    # Write rows (values)
    for i in range(len(next(iter(dictfinal.values())))):  # Get the length of the first list
        row = {key: dictfinal[key][i].replace(",", "") for key in dictfinal}
        writer3.writerow(row)
     
    
csv_file = "output2.csv" # final, well sorted csv

# Writing the dictionary to a CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['capital', '2005', '2010', '2015', '2018'])
    for key in list(dictfinal.keys()):
        key1=dictfinal[key][0].replace(",", "")
        key2=dictfinal[key][1].replace(",", "")
        key3=dictfinal[key][2].replace(",", "")
        key4=dictfinal[key][3].replace(",", "")


        writer.writerow([key, key1, key2, key3, key4])