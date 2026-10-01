# 🐼 Pandas Learning Journey

<div align="center">

<img src="https://pandas.pydata.org/static/img/pandas_white.svg" width="100"/>

📊 Learn Pandas • Practice 100 Questions • Build Data Skills

A structured journey from Pandas fundamentals to advanced data analysis

<br>







</div>

### 🎯 About This Repository

Welcome to my Pandas Learning Journey 🐼

This repository contains 100 practical Pandas questions with answers and Python code, organized from beginner to advanced level.

The goal is to build a strong foundation in Data Analysis, Data Cleaning, Data Manipulation, and Data Processing using Pandas.

💡 Learn → Code → Practice → Build → Improve

---

### 💻 Example
import pandas as pd

data = {
    "Name": ["Krishna", "Rahul", "Aman"],
    "Marks": [90, 85, 78]
}

df = pd.DataFrame(data)

print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nTop Student:")
print(df.loc[df["Marks"].idxmax()])
Output
      Name  Marks
0  Krishna     90
1   Rahul     85
2     Aman     78

Average Marks:
84.33333333333333

Top Student:
Name     Krishna
Marks          90

---
