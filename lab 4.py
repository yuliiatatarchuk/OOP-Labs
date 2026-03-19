import pandas as pd
import sqlite3
df = pd.read_csv("Job opportunities.csv")
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()
df.to_sql('jobs', conn, if_exists='replace', index=False)
query = " SELECT * FROM jobs LIMIT 11;"
result = pd.read_sql(query, conn)
print(result)

required = 'SELECT * FROM jobs WHERE "Required Skills" LIKE "%SQL%";'
req = pd.read_sql(required, conn)
print(req)

unique = 'SELECT DISTINCT Location, Company FROM jobs'
uni = pd.read_sql(unique,conn)
print(uni)

df['Salary Range'] = df['Salary Range'].str.replace(r'[^\d\-]', '', regex=True)
df[['MinSalary', 'MaxSalary']] = df['Salary Range'].str.split('-', expand=True)
df['MinSalary'] = pd.to_numeric(df['MinSalary'])
df['MaxSalary'] = pd.to_numeric(df['MaxSalary'])
df.to_sql('jobs', conn, if_exists='replace', index=False)
avarage_salary = 'SELECT "Experience Level", AVG((MinSalary + MaxSalary)/2) AS AvgSalary FROM jobs GROUP BY "Experience Level";'
avr = pd.read_sql(avarage_salary, conn)

num_vac = 'SELECT "Experience Level", COUNT(*) AS VacancyCount FROM jobs GROUP BY "Experience Level";'
num = pd.read_sql(num_vac, conn)
print( num, avr)
print(df['MinSalary'].min(), df['MaxSalary'].max())

ind_salary_query = 'SELECT "Industry", COUNT(*) AS VacancyCount FROM jobs WHERE "Salary Range" > 50000 GROUP BY "Industry";'
ind_salary = pd.read_sql(ind_salary_query, conn)
print(ind_salary)

ind_avg_query = 'SELECT "Industry", "Salary Range" AS IndustryAvgSalary FROM jobs GROUP BY "Industry";'
ind_avg = pd.read_sql(ind_avg_query, conn)
print(ind_avg)

loc_exp_query = 'SELECT "Location", "Experience Level", COUNT(*) AS Count FROM jobs GROUP BY "Location", "Experience Level";'
loc_exp = pd.read_sql(loc_exp_query, conn)
print(loc_exp)

ind_type_query = 'SELECT "Industry", "Job Type", COUNT(*) AS Count FROM jobs GROUP BY "Industry", "Job Type";'
ind_type = pd.read_sql(ind_type_query, conn)
print(ind_type)

loc_exp_avg_query = 'SELECT "Location", "Experience Level", "Salary Range" AS AvgSalary FROM jobs GROUP BY "Location", "Experience Level";'
loc_exp_avg = pd.read_sql(loc_exp_avg_query, conn)
print(loc_exp_avg)

top_max_query = 'SELECT "Job Title", Company, MaxSalary FROM jobs ORDER BY MaxSalary DESC LIMIT 5;'
top_max = pd.read_sql(top_max_query, conn)
print(top_max)

comp_2023_query = 'SELECT Company, COUNT(*) AS PostCount FROM jobs WHERE "Date Posted" = 2023 GROUP BY Company ORDER BY PostCount DESC LIMIT 5;'
comp_2023 = pd.read_sql(comp_2023_query, conn)
print(comp_2023)

skills_series = df['Required Skills'].str.split(',').explode().str.strip()
skills_count = skills_series.value_counts()
print(skills_count.head(10))