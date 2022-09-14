#! /usr/bin/python3
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
df=pd.read_excel("/home/jshuler/Documents/First.xlsx", "Sheet1")


var = df.groupby('BMI').Sales.sum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlabel('BMI')
ax1.set_ylabel('Sum of Sales')
ax1.set_title("BMI wise Sum of Sales")
var.plot(kind ='line')