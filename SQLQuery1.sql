CREATE DATABASE HR_Attrition;

SELECT TOP 5 * FROM Employees;

DROP TABLE Employees;

SELECT 
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(SUM(CAST(Attrition AS INT)) AS FLOAT) / COUNT(*) * 100 AS Attrition_Rate_Percent
FROM Employees;

SELECT 
    Department,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(SUM(CAST(Attrition AS INT)) AS FLOAT) / COUNT(*) * 100 AS Attrition_Rate_Percent
FROM Employees
GROUP BY Department
ORDER BY Attrition_Rate_Percent DESC;

SELECT 
    OverTime,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(SUM(CAST(Attrition AS INT)) AS FLOAT) / COUNT(*) * 100 AS Attrition_Rate_Percent
FROM Employees
GROUP BY OverTime
ORDER BY Attrition_Rate_Percent DESC;

SELECT 
    Attrition,
    COUNT(*) AS Total_Employees,
    AVG(MonthlyIncome) AS Avg_Monthly_Income
FROM Employees
GROUP BY Attrition;

SELECT 
    JobSatisfaction,
    COUNT(*) AS Total_Employees,
    SUM(CAST(Attrition AS INT)) AS Employees_Left,
    CAST(SUM(CAST(Attrition AS INT)) AS FLOAT) / COUNT(*) * 100 AS Attrition_Rate_Percent
FROM Employees
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;