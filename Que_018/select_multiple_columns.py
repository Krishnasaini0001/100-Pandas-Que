import pandas as pd

data = {
    "Name": ["Ajo", "Jatin", "Krishna"],
    "Age": [20, 21, 22],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

result = df[["Name", "Marks"]]

print(result)