import pandas as pd

marks = pd.Series([90, 85, 88], index=["Math", "Python", "DBMS"])

print(marks["Python"])