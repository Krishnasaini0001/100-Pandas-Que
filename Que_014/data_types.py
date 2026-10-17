import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Krishna"],
    "Age": [20, 21, 22],
    "Marks": [80.5, 85.0, 90.5]
}

df = pd.DataFrame(data)

print("Column Data Types:")
print(df.dtypes)