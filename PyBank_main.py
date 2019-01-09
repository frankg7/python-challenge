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
        starting_profit = 0
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
            #find monthly profits
            profit.append(int((row)[1]) - starting_profit)
            starting_profit = int(row[1])
        #this is how I checked my data
        print("Financial Analysis")
        print("------------------")
        print(("Total Month: ") + str(total_month))
        print(("Total: $") + str(total_profit))
        average_profit_change = total_profit / total_month
        print(("Average change: $") + str(round(average_profit_change, 2)))
        print("Greatest increase in profits: $ " + str(max(set(profit))))
        print("Greatest decrease in profits: $ " + str(min(set(profit))))

        output = (
            f"\nFinancial Analysis \n"
            f"------------------\n"
            f"Total Month: {total_month} \n"
            f"Total: $" + str(total_profit) + "\n"
            f"Average change: $" + str(round(average_profit_change, 2)) + "\n"
            f"Greatest increase in profits: $" + str(max(set(profit))) + "\n"
            f"Greatest decrease in profits: $" + str(min(set(profit)))
            )
        print(output)      
        
        output_file = ("output_file.csv")
        with open(output_file, 'w', newline="") as datafile:
            datafile.write(output)
PyBank()
