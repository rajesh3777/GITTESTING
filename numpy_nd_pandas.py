import numpy as np
import pandas as pd

data = np.random.randint(10,100,(6,4))

df=pd.DataFrame(data,
                columns=["A","B","C","D"])

df["E"]=df["A"]+df["B"]
df["F"]=np.where(df["C"]>50,"High","Low")

df_sorted = df.sort_values("A",ascending=False)
df_filtered=df[df["D"]>40]

df_grouped = df.groupby("F")[["A","B","C","D"]].mean()

df2 = pd.DataFrame({
    "Name":["Raj","Kumar","Arun","Vijay","Mani"],
    "Age":[21,22,20,23,24],
    "Salary":[25000,30000,28000,35000,32000]
})

df_high_salary=df2[df2["Salary"]>28000]
df_age_sorted = df2.sort_values("Age")
df_salary_sum=df2.groupby("Age")["Salary"].sum()

df_merged = pd.merge(df,df2,
                     left_index=True,
                     right_index=True,
                     how="inner")

print("df:\n",df,"\n")
print("sort:\n",df_sorted,"\n")
print("flt:\n",df_filtered,"\n")
print("grp:\n",df_grouped,"\n")

print("emp:\n",df2,"\n")
print(">28k:\n",df_high_salary,"\n")
print("age sort:\n",df_age_sorted,"\n")
print("sum:\n",df_salary_sum,"\n")

print("mrg:\n",df_merged)
