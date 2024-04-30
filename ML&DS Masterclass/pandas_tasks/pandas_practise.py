import numpy as np
import pandas as pd

myindex = ['USA', 'CHINA', 'JAPAN']
mydata = [1772, 3123, 2233]

myser = pd.Series(data=mydata, index=myindex)
print(myser)
print()

ages = {'john': 12, 'johny': 52}
print(pd.Series(ages))

# =====
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100, 'China': 500, 'India': 210, 'USA': 260}


# Dataframe -> x Series (index + col_name) - it's a column of data but with name

# index, column -> row, col
# info() -> ...
# df.columns, df.index -> list of ...
# df.head(x) -> x first rows ... / tail
# df.describe -> info (+mean, std, min, max ...)
# df['name_of_col'] -> col
# df[index] -> row # u can use ',' here to recieve x ...
# np.round(df['col_name'] + df['col_name2'],2) -> ...
# df.set_index('col_name') -> id of rows
# df.reset_index() -> rollback ^
# grab single row -> df.iloc[index] (u can use slices)
# grab single row -> df.loc['index'] u can use ','
# df = df.drop('row/col', axis=0) -> pernament axis=> (0rows,1columns) *indx

# conditional filtering
# df[df.["Pop"] > 50] -> single arg
# df[(df.["Pop"] > 50) & (df.['sex'] == 'Male')] -> multiple ( | as or )
# options = ["Sat", "Sun", "Fri"] -> df[df['day].isin(options)] -> multiple

# apply() -> apply any custom function of every row in a Series
def last_four(nr):
    return str(nr)[-4:]


# df.['CC Number'].apply(last_four) -> Series of what method applied
# df.['CC Number'].apply(lambda data: str(data)[-4:] -> Series of what method applied

# multiple args

def quality(total_bill, tip):
    if tip % total_bill > 0.25:
        return "generous"
    else:
        return "other"


# df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']),axis=1),
# vectorize(func) -> not numpy aware // float as input and output

# timeit -> setup + statements -> timeit.timeit(...)

# df.sort_values('col_name', ascending=False) lub ['col1','col2']
# df['col_name'].max() / idxmax()
# df.iloc[170]
# df.corr() -> ?
# df['sex'].value_counts() -> count of appearanceces
# df['sex'].unique() / nunique() -> unique 'keywords'
# df['col'].replace('Female', 'F') / (['Female', 'Male], [...])
# mymap = {'Female': 'F', 'Male':'M'}
# df['sex'].map(mymap)
# df.duplicated() -> true / false
# df.drop_duplicates() -> del dupl rows
# df.between(10,20,inclusive=True) / df[df.between(10,20,inclusive=True)]
# df.nlargest(10, 'tip')
# sample(5) -> sample 5 diff random rows / sample(frac=0.1) -> 10% of rows

# missing data
print(pd.NA)
print(pd.NA == pd.NA)  # FALSE
print(pd.NA is pd.NA)  # TRUE

df = pd.read_csv("../data/movie_scores.csv")
print(df)

print(df.isnull())
print()
print(df[df['pre_movie_score'].notnull()])

# DROP DATA
print(df.dropna())  # del any row with any missing values
print(df.dropna(thresh=1))  # at least thresh = x not null values
print(df.dropna(axis=1))  # drop columns missing any val
print(df.dropna(subset=['last_name']))  # checking null in exact col

# FILL
print(df.fillna('NEW VALUE!'))
# df['pre_movie_score'] = df['pre_movie_score'].fillna(0)
# print(df)

print(
    df['pre_movie_score'].fillna(df['pre_movie_score'].mean()))  # fill with avg

# interpolate

df = pd.read_csv('../data/mpg.csv')
print(df)

# group by
# df = df.groupby(['model_year']).mean() ->???
# print(df)
# df.loc[[70,92]] -> data with years 70, 82
# df.xs(key=70, level='model_year')
# better use of cross-section (xs): df.xs(key=70, level='cylinders')
# df[df[cylinders].isin([6,8])].groupby(['model_year', 'cylinders']).mean()
# df.swaplevel()
# df.agg(['std','mean'])
# df.agg({'mpg':['max', 'mean'], 'weight':['mean','std']})

# combining DataFrame's
# pd.concat([df1, df2],axis=1) -> will consider col names
# (df.index = []) - indx reset =range(len(df))

# inner merge
# pd.merge(registrations, logins, how='inner', on='name')
# left / right
# pd.merge(right=registrations, left=logins, how='left/right', on='name')
# outer - both

# text methods (for String data)
names = pd.Series(['andrzej', 'rodrygo'])
print(names.str.isdigit())
print()

tech_fin = pd.Series(['COS, PO, PRZECINKU', 'ZNOWU,COS, TEN'])
print(tech_fin.str.split(',', expand=True))
# strip() -> delte whitespaces / +replace to org data
# messy_data.apply(cleanup) / cleanup(method for cleaning data)

# time methods for date and time data
from datetime import datetime

# pd.to_datetime(...)  # dayfirst=True -> EU format
# use datetime docs to apply proper format of date
# pd.to_datetime(..., format='%d--%b--%Y')

# sales = pd.read_csv('../data/sales.csv', parse_dates=[0])
# sales = sales.set_index('DATE')
# sales.resample(rule='A').mean()  # rule -> panda docs

# IO tools
# read_csv('filename.csv', header=null, index_col=0)
# df.to_csv('filename2.csv', index=False)

# tables = pd.read_html(url) /or as file if FWall problem

# xlrd / openpyxl -> working on Excel files
# pd.read_excel('...', sheet_name='name_of_sheet')
# pd.read_excel('...', sheet_name=None) -> returns dict of sheets
# pd.ExcelFile('filename.xlsx')

# SQL DB
# - driver lib needed to your db
#  sqlalchemy - conn with db

# Pivot tables
dff = pd.read_csv('../data/Sales_Funnel_CRM.csv')
print(dff)

licences = dff[['Company', 'Product', 'Licenses']]
print(licences)
piv1 = pd.pivot(licences, index='Company', columns='Product', values='Licenses')

print(pd.pivot_table(licences, index='Company', aggfunc='sum',
                     values=['Licenses', 'Sale Price'],
                     fill_value=0, margins=True))  # aggfunc = [np.mean, np.sum]
# total 
print(dff.groupby('Company').sum())
