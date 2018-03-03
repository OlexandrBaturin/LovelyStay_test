# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime

data = pd.read_json('E:/LovelyStay/reviews.json', orient='records')
data.head()

#1.1
data.info()
data.isnull().sum()

#Number of rows with missing values.
sum(data.apply(lambda x: sum(x.isnull().values), axis = 1)>0) 

"""
We have 11 missing values in overall column and 2 missing values in reviewerName.
As we have only 13 observations in total of 1386 with missing values, the first approach could be to remove this rows. 
"""
sum(data.groupby("asin")["overall"].mean().isnull())

"""
We can substitute the missing values in overall rating with their mean value per product.
However, after that, one missing value will remain.
Or we can substitute the missing values in overall rating with their (global) mean value as requested in the next exercice.
"""

"""
Another approach is to substitute for median value instead of the mean. 
Median is a more robust statistical value than the mean.
"""


#1.2
data.groupby("asin")["overall"].min()
data.groupby("asin")["overall"].max()
data.groupby("asin")["overall"].mean()

data.groupby("asin")["overall"].mean().plot.hist()

#1.3
data["overall"].fillna(data["overall"].mean(), inplace=True)
data.groupby("asin")["overall"].mean().plot.hist()

#1.4
"""
After substituting missing values, the shape of the histogram is quite similar to the previous. 
Global mean value remains the same. 
"""

#2
data.groupby("asin").size()
#or
data.asin.nunique()
#database have 129 different products.

data.groupby("reviewerID").size()
#or
data.reviewerID.nunique()
#database have 1131 different reviewers

#3
data.groupby("asin")["reviewerID"].count().idxmax()
#Product with ID 'B000JMLBHU' has the highest number of reviewers

#4.1
data.groupby("reviewerID")["overall"].count().idxmax()
# reviewer with ID 'A320TMDV6KCFU' did the highest number of reviews

data[data["reviewerID"] == "A320TMDV6KCFU"].sort_values("overall")
#he like the least a product with ID 'B0012W11BM' 

#4.2
# data.groupby("reviewerID")["overall"].count() > 5
# I wasn't able to finish this align

#5
data[(data["asin"] == "B000GFK7L6") & (data["overall"] == 1)]["reviewerName"]
# Amazon Customer "EmanEkaf", Amazoner "reader, thinker, doer" and Douglas Banks 
#rated with 1.0 the product with ID 'B000GFK7L6'


#6.1
data = data.assign(days_since_review = pd.Series(pd.to_datetime(str(datetime.now().date())) - pd.to_datetime(data["reviewTime"])).values)
































