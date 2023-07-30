import os
import csv

#set csv path
bank_csv=os.path.join('.','Resources','budget_data.csv')

#set variables 
budget_data = []

#scan csv file
with open(bank_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    #skip first row
    next(csvreader)

    #Loop through the file and store in a dictionary 
    for row in csvreader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})
    
#Calculate the total months
total_months = len(budget_data)

#Loop through to calculate the changes between months 
change_months = budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"]=budget_data[i]["amount"] - change_months
    previous_amount = budget_data[i]["amount"]

#Calculate total amount 
total_amount = sum(row['amount']for row in budget_data)

#Calculate the average of amount changes
