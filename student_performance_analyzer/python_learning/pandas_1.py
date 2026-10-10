from pathlib import Path
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent


DATA_FILE= BASE_DIR / "data" /"students.csv"
REPORT_DIR= BASE_DIR / "reports"
REPORT_FILE=BASE_DIR/"data"/"student_report.csv"

df=pd.read_csv(DATA_FILE)
subjects_all=df.columns.to_list()

print(subjects_all)
subjects=["math","python", "english"]
# میانگین
df["average"]=df[subjects].mean(axis=1)
print("average",df["average"])
# میانگین
df["avg"]=(df["math"]+df["python"]+df["english"])/3
print("avg",df["avg"])
# بزرگترین
highest=df.loc[df["average"].idxmax()]
minest=df.loc[df["average"].idxmin()]
# بزرگترین معدل
print(highest)
print("***********")
# کوچکترین معدل
print(minest)
# نمره ریاضی گمترین معدل
print(minest["math"])


# میانگین ریاضی
avg_math=df["math"].mean()

# بزرگترین نمره ریاضی
max_math=df["math"].max()
# بزرگترین نمره ریاضیname 

print("بزرگترین نمره ریاضیname",df.loc[df["math"].idxmax(),"name"])

# چاپ کردن سطز دوم
print(" چاپ کردن name سطز دوم",df.loc[1,"name"])
print(" چاپ کردن سطز دوم",df.iloc[1])

