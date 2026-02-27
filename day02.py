sales_data=[1200,3500,3400,7800,2100,9000]

high_value_sales=[]

for sale in sales_data:
    if sale>5000:
        high_value_sales.append(sale)

print(f"all sales", sales_data)
print("high value sales(filtered) ",high_value_sales)