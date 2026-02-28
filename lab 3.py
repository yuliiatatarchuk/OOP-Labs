import pandas as pd

df = pd.read_csv("Job opportunities.csv")
print(df.head(5))
print(df.tail(5))
rows, columns = df.shape
print(f'Кількість рядків: {rows}, Кількість стовпців: {columns}')
memory_bytes = df.memory_usage(deep=True).sum()
memory_megabytes = memory_bytes / (1024 ** 2)
print(f'{memory_megabytes:.2f} MB пам\'яті')
df.isnull().sum()
print(df.isnull().sum())
print(df.info())
filtered_data = df[(df['Industry'] == 'Cloud Computing') ]
filtered_data1 = df[(df['Experience Level'] == 'Senior') ]
filtered_data2 = df[(df['Job Type'] == 'Full-Time') & (df['Location'] == 'London ')]
print(filtered_data)
print(filtered_data1)
print(filtered_data2)

sorted_df = df.sort_values(by='Salary Range', ascending=False)
df["Salary"] = df["Salary Range"].str.extract(r'£(\d+,?\d*)')
df["Salary"] = df["Salary"].str.replace(',', '').astype(int)
columns= ["Salary Range", "Job Title"]
print(sorted_df[columns].head(5))

industry_stats = df.groupby("Industry")["Salary"].agg(['count', 'mean'])
industry_stats.columns = ['Кількість вакансій', 'Середня зарплата']
largest_salary = df["Salary Range"].idxmax()
print(industry_stats)
print(df.loc[largest_salary, ["Industry","Salary Range"]])

def category(salary):
    if salary < 40000:
        return "Low"
    if  40001 <= salary <= 70000:
        return "Medium"
    if salary > 70000:
        return 'High'
df['Salary Category'] = df['Salary'].apply(category)
print(df[['Salary Range', 'Salary Category']].head())

df['Date Posted'] = pd.to_datetime(df['Date Posted'])
df['Year'] = df['Date Posted'].dt.year
year_analysis = df.groupby('Year').agg({'Job Title': 'count'})
year_analysis.columns = ['Number']
active_years = year_analysis.sort_values(by='Number', ascending=False)
print(active_years)