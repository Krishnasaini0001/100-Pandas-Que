import pandas as pd

data = {
    "Name": ["Krishna", "hrv", "Aman","Sourabh", "vaibhav", "Ajo" , "jatin", "op", "Sahil"],
    "Age": [21, 22, 20, 23, 24, 25, 26, 27, 28],
    "Marks": [85, 90, 78, 88, 92, 75, 80, 85, 90]
}

df = pd.DataFrame(data)

print(df.tail(3))# a tail print a bottom 3 rows 