import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Krishna"],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

print("Row with index label 1:")
print(df.loc[1])