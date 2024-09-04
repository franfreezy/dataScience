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
    
    country=[]
    
    for row in reader1:
        country.append(row[0])

    for data in reader2:
        countryname=data[1]
        if countryname in country:
            print(countryname)
        