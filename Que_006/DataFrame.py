import pandas as pd

data = {
    "Name": ["Krishna", "Rahul", "Aman"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)