import pandas as pd

df = pd.read_csv('data/WA_Fn-UseC_-HR-Employee-Attrition (1).csv')
print(df.head())

total = len(df)
left = (df['Attrition'] == 'Yes').sum()
rate = left / total * 100

#Overall Attrition Rate 
print(f"Total employees: {total}")
print(f"Employees who left: {left}")
print(f"Attrition rate: {rate:.1f}%")

#Attrition Rate by Department
dept_attrition = df.groupby('Department')['Attrition'].apply(lambda x: (x == 'Yes').mean() * 100).round(1)
print("\nAttrition rate by Department:")
print(dept_attrition.sort_values(ascending=False))

#Attrition by OverTime
overtime_attrition = df.groupby('OverTime')['Attrition'].apply(lambda x: (x == 'Yes').mean() * 100).round(1)
print("\nAttrition rate by OverTime:")
print(overtime_attrition)

#Average Monthly Income by Attrition
income_by_attrition = df.groupby('Attrition')['MonthlyIncome'].mean().round(0)
print("\nAverage Monthly Income by Attrition:")
print(income_by_attrition)

#Attrition by Job Satisfaction
job_satisfaction_attrition= df.groupby('JobSatisfaction')['Attrition'].apply(lambda x:(x=='Yes').mean() *100).round(1)
print("\nAttrition rate by Job Satisfaction:")
print(job_satisfaction_attrition.sort_values(ascending=False))

# Combined risk group: Sales + Overtime + Low Satisfaction (level 1 or 2)
high_risk = df[
    (df['Department'] == 'Sales') &
    (df['OverTime'] == 'Yes') &
    (df['JobSatisfaction'] <= 2)
]

high_risk_rate = (high_risk['Attrition'] == 'Yes').mean() * 100

print(f"\nHigh-risk group size: {len(high_risk)} employees")
print(f"High-risk group attrition rate: {high_risk_rate:.1f}%")