#Wap to display a person name age address
Name = input("Enter the name : ")
Age = int(input("Enter the age: "))
Address = input("Enter the address: ")
print(Name)
print(Age)
print(Address)

########################################################

import pandas as pd
import matplotlib.pyplot as plt
product_return = pd.read_csv("https://raw.githubusercontent.com/Invact-Abhay/DOE/refs/heads/main/ComplaintsTable.csv")
product_return
product_return.head()

total_complaints = product_return.groupby("ProductCategory")["ComplaintCount"].sum()
total_complaints

sorted_complaints = total_complaints.sort_values(ascending=False)
sorted_complaints

cumulative_sum = sorted_complaints.cumsum()
cumulative_sum

cumulative_percentage = round(cumulative_sum/sorted_complaints.sum()*100,2)
cumulative_percentage

fig, ax1 = plt.subplots()
sorted_complaints.plot(kind='bar',color='C0',ax = ax1)
ax1.set_ylabel('Returns')
ax2 = ax1.twinx()
cumulative_percentage.plot(kind='line',color='C1',ax=ax2,marker='D')
ax2.set_ylabel('cumulative_percentage%')
plt.title('Pareto Analysis of Product Complaints')

product_return.head()

Top4 = product_return.query('ProductCategory in["Kitchenware","Bedding","Jewelry","Books","Beauty Products"]')
Top4

sorted_complaints1 = Top4.groupby("ComplaintReason")["ComplaintCount"].sum().sort_values(ascending=False)
sorted_complaints1
