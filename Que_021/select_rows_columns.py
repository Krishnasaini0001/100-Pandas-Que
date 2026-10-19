import pandas as pd

data = {
    "Name": ["Ajo", "Jatin", "Krishna"],
    "Age": [20, 21, 22],
    "Marks": [88, 75, 97]
}

df = pd.DataFrame(data)

result = df.iloc[0:2, 0:2]

print(result)