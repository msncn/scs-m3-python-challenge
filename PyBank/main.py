# Read the CSV for PyBank
import os
import csv

# PyBank file path
py_bank = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_net = 0
month_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]


# Read PyBank csv file
with open(py_bank,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    print(f"PyBank CSV Header: {csv_header}")
    
    previous_row = next(csvreader)
    previous_profit = int(previous_row[1])
    total_months += 1
    total_net += int(previous_row[1])
       
    for row in csvreader:
        
        # The total number of months
        total_months += 1
        
        # The net total amount of "Profit/Losses" over the entire period
        total_net += int(row[1])
        
        # The changes in "Profit/Losses" over the entire period and then the average of the changes
        current_profit = int(row[1])
        current_change = current_profit - previous_profit
        
        month_change.append(current_change)
        previous_profit = int(row[1])
    
        average_change = sum(month_change)/ (total_months-1)

        # The greatest increase & decrease in profits (date and amount) over the entire period
        
        if current_change > greatest_increase[1]:
            
            greatest_increase[0] = row[0]
            greatest_increase[1] = current_change
            

        if current_change < greatest_decrease[1]:
          
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = current_change
                  
       
# Print the analysis
print("------------------------------")
print("Financial Analysis")
print("------------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average change: ${round(average_change,2)}")
print(f"Greatest Inccrease in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Deccrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})") 

# Export it into a txt file to the "analysis" folder
py_bank_analysis = os.path.join("analysis","budget_analysis.txt")

with open(py_bank_analysis, "w") as textfile:
    textfile.write("Financial Analysis")
    textfile.write('\n')
    textfile.write("------------------------------") 
    textfile.write('\n')
    textfile.write(f"Total months: {total_months}")
    textfile.write('\n')
    textfile.write(f"Total: ${total_net}")
    textfile.write('\n')
    textfile.write(f"Average change: ${round(average_change,2)}")
    textfile.write('\n')
    textfile.write(f"Greatest Inccrease in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    textfile.write('\n')
    textfile.write(f"Greatest Deccrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
