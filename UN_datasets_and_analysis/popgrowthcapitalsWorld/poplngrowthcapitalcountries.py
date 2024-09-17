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

