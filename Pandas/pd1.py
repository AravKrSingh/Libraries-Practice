#PANDAS : USED FOR CLEANING EXPLORING AND ANALYISING DATA
#PANDAS HAVE TWO DATA STRUCTURES : DATAFRAMES AND SERIES
#SERIES ARE IN 1D AND DDATAFRAME ARE 2D
#DATAFRAME HAS THREE COMPONENTS-DATA,ROW AND COLUMN
import pandas as pd
data = {
    "NAME" : ["ARAV","ARSH","ASHISH","SACHIN"],
    "AGE" :["21","20","32","26"],
    "SALARY":["5L","3L","2L","1L"]
    }
print(data)
#Creating a dataframe
df1=pd.DataFrame(data)
print(df1)
#getting data from excel or csv
#pd.read_cscv()
#pd.read_excel

print(df1.describe())#Give statistical data like count , mean ,std,min , max, 25%,50%,75%
print(data.isnull())#-->To get no. of null data


