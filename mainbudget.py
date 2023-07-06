# We need to read in all of the rows (looping through all of the rows - Day 2, Activity 8)
import os, csv

total_profit_losses = 0
total_months = 0

sum_profit_losses = 0

greatest_increase = 0
greatest_increase_month = ""

greatest_decrease = 999999999999
greatest_decrease_month = ""

csvpath = os.path.join('Resources', 'budget_data.csv')


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
# In the for loop, we need to get the profit/losses

        profit_losses = int(row[1])

        total_profit_losses = total_profit_losses + profit_losses
        total_months = total_months + 1

        if total_months > 1:
            change = profit_losses - last_profit_losses

            sum_profit_losses = sum_profit_losses + change

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]

        last_profit_losses = int(row[1])


# After the loop, print out our summary stuff to the screen
output_text=(
f'Financial Analysis\n'
f'----------------------\n'
f'Total Months:   {str(total_months)}\n'
f'Total: ${ str(total_profit_losses)}\n'
f'Average Change: ${ round(sum_profit_losses / (total_months - 1),2)}\n'
f'Greatest Increase in Profits:{greatest_increase_month}(${ str(greatest_increase) })\n'
f'Greatest Decrease in Profits:{greatest_decrease_month}(${ str(greatest_decrease) })'
)
print(output_text)

# Also, remember to write out the summary stuff to a file
# Use Day 2, activity 10: write_txt_file.py as an example

Output_path = os.path.join('Analysis', 'budget_text.txt')


# Method 2: Improved Reading using CSV module

with open(Output_path,"w") as output_file:
    output_file.write(output_text)
