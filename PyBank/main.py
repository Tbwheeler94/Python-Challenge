import os
import csv

budget_data_csv = os.path.join(".." , "PyBank" , "budgetdatadownload.csv")

# Open and read csv
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip headers
    header = next(csvreader)

    # Read through each row of data after the header
    for row in csvreader:
        
        print("Financial Analysis")
        print("-------------------------")
        
        row_count = sum(1 for row in csvreader) + 1
        print("Total Months: " + str(row_count))
        row_count = 0
    
    #create array
    #add values in row 2 to array
    #sum values in array
    
        profit = []
        for row in csvreader:
            if int(row[1]) > 0:
                profit_value = row[1]
                profit.append(profit_value)
                print(profit)

        # Convert row to float and compare to grams of fiber
        # if int(row[1]) > 5:
            #print(row[1])
