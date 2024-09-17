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