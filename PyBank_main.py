import os
import csv

# Could use the following if needed ("..", "Resources")
csvpath = os.path.join("budget_data.csv")
def PyBank():
    with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csvheader = next(csvreader)
        total_month = 0
        total_profit = 0
        monthly_profit = []
        monthly_increase = []
        profit = []
        for row in csvreader:
            #Find total month
            total_month += 1
            #Find Profit
            monthly_profit.append(row[1])
            #find total profit
            total_profit += int(row[1])
        #this is how I checked my data
        print("Financial Analysis")
        print("------------------")
        print(("Total Month: ") + str(total_month))
        print(("Total: $") + str(total_profit))
        print(("Average change: $") + str(round(average_profit_change, 2)))
        print("Greatest increase in profits: $")
        print("Greatest decrease in profits: $")

output = (
    f"\nFinancial Analysis \n"
    f"------------------\n"
    f"Total Month: {total_month} \n"
    f"Greatest increase in profits: $" + str(max(set(monthly_profit))) + "\n"
    f"Greatest decrease in profits: $" + str(min(set(monthly_profit))))
print(output)       

with open(output_file, 'w', newline="") as datafile:
    datafile.write(output)