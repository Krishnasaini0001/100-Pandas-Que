import pandas as pd

data = {
    "Name": ["Krishna", "Jatin", "Ajo"],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

print("First Row:")
print(df.iloc[0])