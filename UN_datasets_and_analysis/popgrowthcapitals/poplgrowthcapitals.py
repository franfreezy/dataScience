#visualisation
import pandas as pd
import csv
import bar_chart_race as bcr
data='output2.csv'
df = pd.read_csv(data)

actual_popln = df.copy()
actual_popln.iloc[:, 1:]*=1000


#in columns
data='output3.csv'
df = pd.read_csv(data)
actual_popln2 = df.copy()
actual_popln2 *= 1000
df = actual_popln2

new_column_data = ['2005', '2010', '2015', '2018']
df.insert(0, 'Year', new_column_data)
df = df.set_index('Year')

bcr.bar_chart_race(
    df=df,
    filename='bar_chart_race.mp4',  
    title='African Capital cities population growth', 
    figsize=(15, 10),  
    cmap='dark12',  
    n_bars=53,  
    period_length=1200,  
    label_bars=True, 
    sort='desc'  
)


