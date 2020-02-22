import os
import csv

revenue_values = []
revenue_difference = []
dates = []
profit_loss = 0
row_count = 0

budget_data_csv = os.path.join(".." , "PyBank" , "budgetdatadownload.csv")

# Open and read csv
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip headers
    header = next(csvreader)

    # Read through each row of data after the header
    for row in csvreader:

        #Profit/Loss counter
        profit_loss = profit_loss + int(row[1])

        #Creates a list of revenue values as integers
        revenue_values.append(float(row[1]))

        #Creates a list of dates
        dates.append(row[0])

    for unit in range(1, len(revenue_values)):
        
        revenue_difference.append(revenue_values[unit] - revenue_values[unit - 1])

    average_revenue_difference = round(sum(revenue_difference) / len(revenue_difference), 2)

    greatest_increase_profits = round(max(revenue_difference))
    greatest_decrease_profits = round(min(revenue_difference))

    greatest_increase_index = revenue_difference.index(greatest_increase_profits) + 1
    greatest_decrease_index = revenue_difference.index(greatest_decrease_profits) + 1

print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(len(revenue_values)))
print("Profit/Loss: $" + str(profit_loss))
print("Average Change: $" + str(average_revenue_difference))
print(f'Greatest Increase in Profits: {dates[int(greatest_increase_index)]} (${greatest_increase_profits})')
print(f'Greatest Increase in Profits: {dates[int(greatest_decrease_index)]} (${greatest_decrease_profits})')

textfile= open("output.txt","w+")
textfile.write("Financial Analysis" + "\n")
textfile.write("-------------------------" + "\n")
textfile.write("Total Months: " + str(len(revenue_values)) + "\n")
textfile.write("Profit/Loss: $" + str(profit_loss) + "\n")
textfile.write("Average Change: $" + str(average_revenue_difference) + "\n")
textfile.write(f'Greatest Increase in Profits: {dates[int(greatest_increase_index)]} (${greatest_increase_profits})' + "\n")
textfile.write(f'Greatest Increase in Profits: {dates[int(greatest_decrease_index)]} (${greatest_decrease_profits})' + "\n")
textfile.close()