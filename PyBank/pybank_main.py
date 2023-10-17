import os
import csv

# Set csv path
bank_csv = os.path.join('/Users/cindy/Desktop/Bootcamp/python-challenge/PyBank/Resources/budget_data.csv')

# Set variables
budget_data = []

# Scan csv file
with open(bank_csv) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')

    # Loop through the file and store in a dictionary
    for row in csvreader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]), "change": 0})

# Calculate the total months
total_months = len(budget_data)

# Loop through to calculate the changes between months
change_months = budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"] = budget_data[i]["amount"] - change_months
    change_months = budget_data[i]["amount"]

# Calculate total amount
total_amount = sum(row['amount'] for row in budget_data)

# Calculate the average of amount changes
total_change = sum(row['change'] for row in budget_data)
average_change = round(total_change / (total_months - 1), 2)

# Calculate the greatest increase and decrease from the changes
increase = max(budget_data, key=lambda x: x['change'])
month_increase = increase["month"]
change_increase = increase["change"]

decrease = min(budget_data, key=lambda x: x['change'])
month_decrease = decrease["month"]
change_decrease = decrease["change"]

# Print
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_amount}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {month_increase} (${change_increase})')
print(f'Greatest Decrease in Profits: {month_decrease} (${change_decrease})')

# Export results to a text file
bank_file = os.path.join("/Users/cindy/Desktop/Bootcamp/python-challenge/PyBank/Resources/Results")
with open("Results.txt", "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_amount}\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {month_increase} (${change_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {month_decrease} (${change_decrease})\n")
