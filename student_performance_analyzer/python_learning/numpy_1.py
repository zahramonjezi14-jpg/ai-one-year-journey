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


# using numpy**********************************

# scores=df[subjects].to_numpy()

scores=df[["math","python","english"]].to_numpy()

print("************")
    
print(scores)
print("mean all score", np.mean(scores))
print("mean every lesson", np.mean(scores,axis=0))
print("mean every student", np.mean(scores,axis=1))

# نمرات بزرگتر از 16
print(scores[scores>=16])

print(scores>16)


print(scores*2)

s=np.arange(1,17)
print(s.reshape(2,8))

x=np.array([14,34,25,12])
print(x.mean())