import os
import csv
import sys

# Path to collect budget data from the Resources folder
budgetdataCSV = os.path.join('.', 'Resources', 'budget_data.csv')


# Read in the CSV file
with open(budgetdataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Set empty lists to gather profit/loss and month data
    total_list = []
    month_list = []
    monthly_change = []
    
    # Loop through the data
    for row in csvreader:
        
        total_list.append(int(row[1]))
        month_list.append(row[0])
    
    # Loop through profit/loss list to find difference change
    for i in range(1,len(total_list)):
        change = total_list[i] - total_list[i-1]
        monthly_change.append(change)
    
    # Find the index positions of the greatest increase/decrease
    max_change_index = monthly_change.index(max(monthly_change))
    min_change_index = monthly_change.index(min(monthly_change))

# Print out results to terminal    
print("Financial Analysis")
print("----------------------------------")
print("")
print("----------------------------------")
print(f"Total Months: {len(month_list)}")
print(f"Total: ${sum(total_list)}")
print(f"Average Change: ${round(sum(monthly_change) / float(len(monthly_change)),2)}")
print(f"Greatest Increase in Profits: {month_list[max_change_index]} (${max(monthly_change)})")
print(f"Greatest Decrease in Profits: {month_list[min_change_index]} (${min(monthly_change)})")

# Print to Result.txt file
sys.stdout = open('results.txt','wt')
print("Financial Analysis")
print("----------------------------------")
print("")
print("----------------------------------")
print(f"Total Months: {len(month_list)}")
print(f"Total: ${sum(total_list)}")
print(f"Average Change: ${round(sum(monthly_change) / float(len(monthly_change)),2)}")
print(f"Greatest Increase in Profits: {month_list[max_change_index]} (${max(monthly_change)})")
print(f"Greatest Decrease in Profits: {month_list[min_change_index]} (${min(monthly_change)})")
sys.stdout.close




