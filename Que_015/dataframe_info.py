import pandas as pd

data = {
    "Name": ["Hrv", "op", "Krsna"],
    "Age": [20, 21, 22],
    "Marks": [80, 85, 90]
}

df = pd.DataFrame(data)

df.info()