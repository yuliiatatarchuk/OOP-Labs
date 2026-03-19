import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Job opportunities.csv')
df["Avarage Salary"] = df["Salary Range"].str.extract(r'£(\d+,?\d*)')
df["Avarage Salary"] = df["Avarage Salary"].str.replace(',', '').astype(int)

plt.figure(figsize=(10, 6))
sns.barplot(x='Experience Level', y='Avarage Salary', data=df, palette='viridis', hue = 'Experience Level',legend=False)
plt.title('Залежність зарплати від досвіду')
plt.xlabel('Досвід')
plt.ylabel('Середня зарплата($)')
plt.show()

plt.figure(figsize=(12, 6))
plt.xticks(rotation=45, ha='right')
sns.boxplot(x='Industry', y='Avarage Salary', data=df, palette='Set2', hue = 'Experience Level',legend=False)
plt.title('Розподіл зарплат за галузямии')
plt.xlabel('Industry')
plt.ylabel('Avarage Salary')
plt.show()

pivot_table = pd.crosstab(df['Experience Level'], df['Industry'])
corr_matrix = pivot_table.corr()
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap='viridis', linewidths=0.5)
plt.title('Кореляція між Experience Level та Industry')
plt.show()

df['Year'] = df['Date Posted'].apply(lambda x: int(x.split('/')[0]))
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Year', y='Avarage Salary', hue='Experience Level', data=df, palette='deep', alpha=0.7)
plt.title('Залежність між зарплатою та роком публікації вакансій')
plt.xlabel('Year')
plt.ylabel('Avarage Salary')
plt.legend(title='', bbox_to_anchor=(1, 1), loc='upper left')
plt.show()

sns.pairplot(df[['Experience Level', 'Year', 'Avarage Salary' ]], diag_kind='kde', palette='bright')
plt.suptitle('Парні графіки для Experience Level, Year та Avarage Salary', y=1.02)
plt.show()

