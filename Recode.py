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
