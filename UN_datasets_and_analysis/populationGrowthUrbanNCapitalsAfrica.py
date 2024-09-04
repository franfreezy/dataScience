import csv

#path to files
countrycsv='africancounties.csv'
datasetcsv='populationGrowthUrbanandCapitals.csv'

#readcsv
with open(countrycsv, newline='') as csvfile,open(datasetcsv, newline='') as csvfile2:
    reader1 = csv.reader(csvfile)
    reader2 = csv.reader(csvfile2)
    next(reader1) #skips the header
    next(reader2)

    for row in reader1:
        print(row[0]) 