# Week 1 Practice Excercise

# Import and Inspect | DataFrame | Pandas | Python |:
# Problem 1:-

import pandas as pd
car=pd.read_csv('MPG.csv')

# Problem 2:-

car

# Problem 3:-

car.head(10)

# Problem 4:-

car.tail()

# Problem 5:-

pd.options.display.max_rows=400
car

# Problem 6:-

car.isna().sum()

# Problem 7:-

car=car.dropna()
car.isna().sum()

# Problem 8:-

car.describe()

# Problem 9:-

car.info()

# Problem 10:-

car.shape


# Analysing Columns | DataFrame | Pandas | Python |:
# Problem 1:-

mpg=pd.read_csv('MPG.csv')
mpg

# Problem 2:-

car=mpg.copy()

# Problem 3:-

mpg.drop('cylinders',axis=1)
mpg.columns
car.columns

# Problem 4:-

car.info()
car.describe()

# Problem 5:-

car[['cylinders','origin']].value_counts()

# Problem 6:-

car[['origin']].value_counts() 
car['origin'].unique()
car['origin'].nunique()

# Problem 7:-

car.sort_values('displacement')

# Problem 8:-

car.sort_values('displacement',ascending=False)

# Problem 9:-

car.sort_values(['displacement','weight'],ascending=False)

# Problem 10:-

car.describe(include='all')

# Problem 11:-

car.T


# Indexing and Slicing | DataFrame | Pandas | Python | 
# Problem 1:-

titanic=pd.read_csv('Titanic.csv')

# Problem 2:-

titanic.info()

# Problem 3:-

titanic.columns

# Problem 4:-

titanic.name
type(titanic.name)

# Problem 7:-

titanic['name']
name=titanic['name']
name
type(name)
name.shape

# Problem 6:-

name=titanic[['name']]
name
type(name)
name.shape

# Problem 7:-

titanic.iloc[100,:]

# Problem 8:-

titanic.loc[100,:]

# Problem 9:-

titanic.iloc[:,[2,8]]

# Problem 10:-

titanic.loc[:,['name','fare']]

# Problem 11:-


titanic.loc[[50,25,15],['pclass','fare','age']]
titanic.iloc[[50,25,15],[0,8,4]]

# Problem 12:-

titanic.loc[10:25, ['pclass','fare','age']]
titanic.iloc[10:26, [0,8,4]]

# Problem 13:-

titanic.loc[10:15, 'pclass':'age']
titanic.iloc[10:16, 0:5]

# Problem 14:-

titanic[titanic['age']>=35]

# Problem 15:-

titanic.loc[(titanic['age']>=35), 'pclass':'age']

# Problem 16:-

titanic.loc[(titanic['age']>=35)&(titanic['sex']=='female')]


# Calculated Columns | DataFrame | Pandas | Python |
# Problem 1:-

tips=pd.read_csv('Tips.csv')

# Problem 2:-

tips.head()

# Problem 3:-

tips['tip']/tips['total_bill']*100

# Problem 4:-

tip_percentage=tips['tip']/tips['total_bill']*100
tip_percentage

# Problem 5:-

tips['tip_percentage']=tips['tip']/tips['total_bill']*100
tips.head()

# Problem 6:-

tips['tip_percentage']=tips['tip_percentage'].round(1)
tips.head()

# Problem 7:-

tips=tips.drop(['smoker'], axis = 1)
tips.head()

# Problem 8:-

tips.set_index('tip')
tips.head()

# Problem 9:-

tips=tips.set_index('tip')
tips.head()

# Problem 10:-

tips=tips.reset_index()
tips.head()
