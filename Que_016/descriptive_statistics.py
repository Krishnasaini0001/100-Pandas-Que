import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Krishna", "Rohit"],
    "Marks": [70, 80, 90, 100],
    "Age": [19, 20, 21, 22]
}

df = pd.DataFrame(data)

print("Statistical Summary:")
print(df.describe())