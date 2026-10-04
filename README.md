# Employee Attrition Analysis

## Objective
Find out why employees leave the company and which groups are most at risk, so HR can reduce attrition.

## Dataset
IBM HR Employee Attrition dataset (Kaggle).

## Tools Used
- **SQL Server**: data analysis queries
- **Python (pandas)**: cross-checking results and finding a high-risk group
- **Power BI**: interactive dashboard

## Key Findings
- The overall attrition rate is **16.12%**.
- **Sales** has the highest attrition (20.63%), followed by Human Resources (19.05%) and Research & Development (13.84%).
- Employees who work **overtime** leave at **30.53%**, about 3x the rate of those who don't (10.44%).
- Employees who left earned less on average (**4.8K** per month) than those who stayed (**6.8K**).
- Employees with the lowest job satisfaction (level 1) have the highest attrition rate at **22.84%**, compared to 11.33% for level 4.
- The highest-risk group is **Sales employees who work overtime and have low satisfaction**, with an attrition rate of about **50%**.

## Recommendations
- Reduce overtime, starting with the Sales team.
- Review pay for roles where leavers earn much less than stayers.
- Run satisfaction surveys and act on low scores.


## Files
| File | Description |
|------|-------------|
| `SQLQuery1.sql` | SQL queries for attrition analysis |
| `attrition_analysis.py` | Python analysis using pandas |
| `Employee_Attrition_project.pbix` | Power BI dashboard |
| `Employee_Attrition_Visualisation.pdf` | Dashboard export |
