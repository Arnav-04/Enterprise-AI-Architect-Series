import pandas as pd

#making a dataframe from dictionary
dcit1={
    "name": ["arnav", "arnie6", "arnab", "arniee"],
    "city": ["noida", "noidda", "delhi", "web"],
    "salary": [35000, 45000, 93000,101000]
}

#converting the above dictionary to Pandas DataFrame and Pandas series- lets see
df_dataframe=pd.DataFrame(dcit1)
print(df_dataframe)
print(type(df_dataframe))

df_series=pd.Series(dcit1)
print(df_series)
print(type(df_series))