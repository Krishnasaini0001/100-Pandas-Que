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


```python
import pandas as pd

data = {
    "Name": ["Krishna", "Jatin", "Harshendra"],
    "Marks": [90, 75, 88]
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

```
---

### 🧠 Learning Method

Every question follows this simple process:

❓ Question
     │
     ▼
💡 Concept
     │
     ▼
📝 Answer
     │
     ▼
💻 Python Code
     │
     ▼
🧪 Practice
     │
     ▼
🚀 GitHub Commit

This makes the repository useful not only for learning but also for revision and interview preparation.

---

📌 Why Pandas?

Pandas is one of the most important Python libraries for working with structured data.

It is widely used for:

📥 Data Collection
      ↓
🧹 Data Cleaning
      ↓
🔄 Data Transformation
      ↓
📊 Data Analysis
      ↓
📈 Visualization
      ↓
🤖 Machine Learning
---

Pandas Learning Journey

🟢 Q01 ━━━━━━━━━━━━━━━━━━━ Q25
   Fundamentals

🟡 Q26 ━━━━━━━━━━━━━━━━━━━ Q50
   Data Cleaning

🟠 Q51 ━━━━━━━━━━━━━━━━━━━ Q75
   Data Manipulation

🔴 Q76 ━━━━━━━━━━━━━━━━━━━ Q100

   Advanced Pandas

---

Pandas-Learning-Journey/
│
├── Day_001/
│   └── pandas_import.py
│
├── Day_002/
│   └── pandas_version.py
│
├── Day_003/
│   └── create_series.py
│
├── Day_004/
│   └── custom_index.py
│
├── Day_005/
│   └── create_dataframe.py
│
├── ...
│
├── Day_025/
│   └── rename_column.py
│
├── Day_026/
│   └── filter_rows.py
│
├── ...
│
├── Day_050/
│   └── text_search.py
│
├── Day_051/
│   └── calculate_mean.py
│
├── ...
│
├── Day_075/
│   └── percentage_change.py
│
├── Day_076/
│   └── read_csv.py
│
├── ...
│
├── Day_100/
│   └── pandas_workflow.py
│
└── README.md
🤖 Machine Learning
