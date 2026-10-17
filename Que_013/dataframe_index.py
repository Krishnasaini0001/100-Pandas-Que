import pandas as pd

data = {
    "Name": ["Ajo", "Jatin", "Krsna"],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

print("DataFrame Index:")
print(df.index)