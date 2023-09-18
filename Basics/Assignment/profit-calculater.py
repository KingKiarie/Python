# create a file called profit-calculator.py
# Write a python program that Calculates Sales Profit

year1_sales = 14560
year2_sales = 17890

# method1
margin = year2_sales-year1_sales
print(margin)

profit1 = (margin/year1_sales)*100
print(profit1)

# method2
profit= ((year2_sales-year1_sales)/year1_sales)*100

print(profit)

