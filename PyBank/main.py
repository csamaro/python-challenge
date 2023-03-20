import csv
import os

print("Financial Analysis")
print("----------------------------------")

month_count = 0
profit_loss_overtime = 0.0
max_profit = 0
max_loss = 0
pl_time = 0
month_max = []
month_min = []

csvpath = os.path.join('Resources', 'budget_data.csv') 
# csvpath = "Resources/budget_data.csv"

# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #print(csvreader) #where it is located

    csv_header = next(csvreader) #skips first row
    print(f"CSV header {csv_header}")

    for row in csvreader:
        month_count = month_count + 1 #counts every row
        pl_time = int(row[1]) #get profit/loss from csv
        profit_loss_overtime = profit_loss_overtime + pl_time #adding all profits/losses
        if pl_time > max_profit:
            max_profit = pl_time #sets max profit
            month_max[0] = row[0] #sets month/day of max profit
        if pl_time < max_loss:
            max_loss = pl_time #sets max loss
            month_min[0] = row[0] #sets month/day of max loss

    
    print(month_count)
    print(profit_loss_overtime)
    print(max_profit)
    print(max_loss)
    print(f"{month_max}")
    print(f"{month_min}")