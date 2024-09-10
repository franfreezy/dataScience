#visualisation
import pandas as pd
import csv
data='output2.csv'
df = pd.read_csv(data)

actual_popln = df.copy()
actual_popln.iloc[:, 1:]*=1000
print(actual_popln)
