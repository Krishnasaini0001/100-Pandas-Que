import pandas as pd

data = [90, 85, 88]

marks = pd.Series(data, index=["Math", "Python", "DBMS"])

print(marks)