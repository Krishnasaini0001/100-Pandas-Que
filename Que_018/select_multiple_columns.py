import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Krishna"],
    "Age": [20, 21, 22],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

result = df[["Name", "Marks"]]

print(result)