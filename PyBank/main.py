import os
import csv

# Assign variables
revenue_values = []
revenue_difference = []
dates = []
profit_loss = 0
row_count = 0

# Assign variable to file pathway to desired data
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

    #Loop through values in revenue_values array beginning at second value
    for unit in range(1, len(revenue_values)):
        
        # subtract previous unit in array from current unit
        # create array of these differences named revenue_difference
        revenue_difference.append(revenue_values[unit] - revenue_values[unit - 1])

    #divide sum of revenue differences by total number of units in the array to find the average change
    #round this number to the nearest 2 decimal places
    average_revenue_difference = round(sum(revenue_difference) / len(revenue_difference), 2)

    # assign variables to max and min revenue difference values 
    greatest_increase_profits = round(max(revenue_difference))
    greatest_decrease_profits = round(min(revenue_difference))

    # find index values of the max and min revenue difference - 1
    # this number will be used to find the respective date value in the dates array
    greatest_increase_index = revenue_difference.index(greatest_increase_profits) + 1
    greatest_decrease_index = revenue_difference.index(greatest_decrease_profits) + 1

#Print all results
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(len(revenue_values)))
print("Profit/Loss: $" + str(profit_loss))
print("Average Change: $" + str(average_revenue_difference))
print(f'Greatest Increase in Profits: {dates[int(greatest_increase_index)]} (${greatest_increase_profits})')
print(f'Greatest Increase in Profits: {dates[int(greatest_decrease_index)]} (${greatest_decrease_profits})')

#Write output to text file
textfile= open("output.txt","w+")
textfile.write("Financial Analysis" + "\n")
textfile.write("-------------------------" + "\n")
textfile.write("Total Months: " + str(len(revenue_values)) + "\n")
textfile.write("Profit/Loss: $" + str(profit_loss) + "\n")
textfile.write("Average Change: $" + str(average_revenue_difference) + "\n")
textfile.write(f'Greatest Increase in Profits: {dates[int(greatest_increase_index)]} (${greatest_increase_profits})' + "\n")
textfile.write(f'Greatest Increase in Profits: {dates[int(greatest_decrease_index)]} (${greatest_decrease_profits})' + "\n")
textfile.close()