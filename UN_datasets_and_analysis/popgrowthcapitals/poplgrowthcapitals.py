#visualisation
import pandas as pd
import csv
import bar_chart_race as bcr
data='output2.csv'
df = pd.read_csv(data)

actual_popln = df.copy()
actual_popln.iloc[:, 1:]*=1000
print(actual_popln)




