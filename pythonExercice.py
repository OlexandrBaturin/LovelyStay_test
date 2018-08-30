# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime

data = pd.read_json('E:/LovelyStay/reviews.json', orient='records')
data.head()

#1.1. Start by having a look at the dataset and check for missing values. What can you do about missing values? 
#You can specify more than one approach. This is a subjective question, write your reasoning below. 
#Feel free to include in your answer any code with exploratory analysis that guided you.
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


#1.2. Compute the min, max and mean of the overall rating, per product. Ignore missing values
data.groupby("asin")["overall"].min()
data.groupby("asin")["overall"].max()
data.groupby("asin")["overall"].mean()

data.groupby("asin")["overall"].mean().plot.hist()

#1.3. Now substitute the missing values in overall rating with their (global) mean value. 
#Recompute the mean overall rating per product.
data["overall"].fillna(data["overall"].mean(), inplace=True)
data.groupby("asin")["overall"].mean().plot.hist()

#1.4. Comment the results.
"""
After substituting missing values, the shape of the histogram is quite similar to the previous. 
Global mean value remains the same. 
"""

#2. How many products are in the dataset? And reviewers?
data.groupby("asin").size()
#or
data.asin.nunique()
#database have 129 different products.

data.groupby("reviewerID").size()
#or
data.reviewerID.nunique()
#database have 1131 different reviewers

#3. Which product has the highest number of reviewers?
data.groupby("asin")["reviewerID"].count().idxmax()
#Product with ID 'B000JMLBHU' has the highest number of reviewers

#4.1 Which reviewer did the highest number of reviews? Which product did he like the least?
data.groupby("reviewerID")["overall"].count().idxmax()
# reviewer with ID 'A320TMDV6KCFU' did the highest number of reviews

data[data["reviewerID"] == "A320TMDV6KCFU"].sort_values("overall")
#he like the least a product with ID 'B0012W11BM' 

#4.2 How many reviewers did more than 5 reviews?
# data.groupby("reviewerID")["overall"].count() > 5
# I wasn't able to finish this align

#5. For the product 'B000GFK7L6', which what are the names of the reviewers that rated it 1.0?
data[(data["asin"] == "B000GFK7L6") & (data["overall"] == 1)]["reviewerName"]
# Amazon Customer "EmanEkaf", Amazoner "reader, thinker, doer" and Douglas Banks 
#rated with 1.0 the product with ID 'B000GFK7L6'

#6. Date and string manipulation

#6.1 Create a new colum named days_since_review with the number of days that have passed since the review was made.
data = data.assign(days_since_review = pd.Series(pd.to_datetime(str(datetime.now().date())) - pd.to_datetime(data["reviewTime"])).values)

#6.2 The helpfulness of a review is currently defined as an array [number of helpfull reviews/ total number of reviews]. 
#Create a new column helpful_bool, where the review is either helpful (True) or not (False). 

#7. Advanced analysis: Suppose this dataset was only a sample of a larger one, and you were asked the following: *

#a) Group the products by their review text. 

#b) Use this data to recommend (or advise against) new articles to a user. 

#c) Build a system to detect fake reviews. 

#* Describe how you would first approach the task. Be specific about the kind of preprocessing you would apply. 
#Feel free to play around, but no code is needed here.

