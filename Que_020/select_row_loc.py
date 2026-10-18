import pandas as pd

data = {
    "Name": ["Ajo","Krishna", "Jatin"],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

print("Row with index label 1:")
print(df.loc[1])