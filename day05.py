import pandas as pd
import matplotlib.pyplot as plt

sales_data={
    'Day': ['Mon','Tue','Wed','Thu','Fri'],
    'Sales':[12000,15000,9000,None,18000]
}

df=pd.DataFrame(sales_data)

print("_Missing values check_")
print(df.isnull().sum())

mean_sales=df['Sales'].mean()
df['Sales']=df['Sales'].fillna(mean_sales)

print("\n_After Filling missing values_")
print(df)

plt.bar(df['Day'],df['Sales'],color='skyblue')
plt.xlabel('Day of the week')
plt.ylabel('Sales amount')
plt.title('Weekly sales performance (cleaned data)')
plt.show()