import pandas as pd

data = {
    "Name": ["Ajo", "Jatin", "Krishna"],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

print("Student Names:")
print(df["Name"])