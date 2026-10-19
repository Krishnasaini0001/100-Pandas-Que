import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Krishna"],
    "Age": [20, 21, 22],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

result = df.iloc[0:2, 0:2]

print(result)