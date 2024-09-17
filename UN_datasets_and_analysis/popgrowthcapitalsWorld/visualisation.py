import pandas as pd
import csv
import bar_chart_race as bcr

#in columns
data='output3.csv'
df = pd.read_csv(data)
actual_popln2 = df.copy()
actual_popln2 *= 1000
df = actual_popln2

new_column_data = ['2005', '2010', '2015', '2018']
df.insert(0, 'Year', new_column_data)
df = df.set_index('Year')

df1 = df.iloc[:, :15]
df2 = df.iloc[:,15:30]
df3 = df.iloc[:,30:50]
df4 = df.iloc[:, 50:70]
df5 = df.iloc[:, 70:90]
df6 = df.iloc[:,90:110]
df7 = df.iloc[:,110:130]
df8 = df.iloc[:, 130:150]
df9 = df.iloc[:, 150:170]
df10 = df.iloc[:,170:190]
df11 = df.iloc[:,190:210]
df12 = df.iloc[:, 210:230]

dfs = [df1, df2, df3, df4,df5,df6,df7,df8,df9,df10,df11,df12]

# Loop over the list and generate bar chart races
for i, df_part in enumerate(dfs, start=1):
    filename = f'bar_chart_race_{i}.mp4'  
    bcr.bar_chart_race(
        df=df_part,
        filename=filename,  
        title='Capital cities population growth', 
        figsize=(15, 10),  
        cmap='dark12',  
        n_bars=len(df_part.columns),   
        period_length=3000,  
        label_bars=True, 
        sort='desc'  
    )
    