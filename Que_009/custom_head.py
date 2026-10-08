import pandas as pd

data = {
    "Name": ["Krishna", "hrv", "Aman","Sourabh", "vaibhav", "Ajo" , "jatin", "op", "Sahil" ,"deepak"],
    "Age": [21, 22, 20, 23, 24, 25, 26, 27, 28, 29],
    "Marks": [85, 90, 78, 88, 92, 75, 80, 85, 90, 95]
}

df = pd.DataFrame(data)

print(df.head(3))# a head print a top 3 rows 