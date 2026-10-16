import pandas as pd

data = {
    "Name": ["krsna", "hrv"],
    "Age": [20, 21],
    "Marks": [80, 90]
}

df = pd.DataFrame(data)

print("Column Names:")
print(df.columns.tolist())