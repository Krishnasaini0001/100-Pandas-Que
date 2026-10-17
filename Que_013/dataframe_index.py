import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Krishna"],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

print("DataFrame Index:")
print(df.index)