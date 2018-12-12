import os
import csv

# Path to collect budget data from the Resources folder
budgetdataCSV = os.path.join('.', 'Resources', 'budget_data.csv')


# Read in the CSV file
with open(budgetdataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    total_list = []
    month_list = []
    monthly_change = []
    total_change = []

    # Loop through the data
    for row in csvreader:
        
        total_list.append(int(row[1]))
        month_list.append(row[0])
    
    for i in range(1,len(total_list)):
        change = total_list[i] - total_list[i-1]
        monthly_change.append(change)
    
print(f"Total Months: {len(month_list)}")
print(f"Total: ${sum(total_list)}")
print(f"Average Change: ${round(sum(monthly_change) / float(len(monthly_change)),2)}")

