import csv
import os

print("Financial Analysis\n")
print("----------------------------------\n")

month_count = 0
profit_loss_overtime = 0
pl_time = 0
max_profit = 0
max_loss = 0
last_pl = 0
avg_change = []


csvpath = os.path.join('Resources', 'budget_data.csv') 
# csvpath = "Resources/budget_data.csv"

# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #print(csvreader) #where it is located

    csv_header = next(csvreader) #skips first row
    #print(f"CSV header {csv_header}")

    for row in csvreader:
        month_count = month_count + 1 #counts every row
        pl_time = int(row[1]) #get profit/loss from csv
        profit_loss_overtime = profit_loss_overtime + pl_time #adding all profits/losses

        current_pl = int(row[1]) #set current 
        pl_difference = current_pl - last_pl #current - previous

        if (pl_difference > max_profit): 
            max_profit = current_pl - last_pl
            max_month_name = row[0]

           # print(max_month_name)

        elif (pl_difference < max_loss):
            max_loss = current_pl - last_pl
            min_month_name = row[0]

           # print(min_month_name)

        last_pl = current_pl #set previous to current
        avg_change.append(pl_difference) #creates list of pl changes
    
    avg_change.pop(0)
    avg_avg_change = sum(avg_change) / len(avg_change)
    
    print(f"Total months: {month_count}\n")
    print(f"Total: ${profit_loss_overtime}\n")
    print(f"Average Change: $ {round(avg_avg_change, 2)}\n")
    print(f"Greatest Increase in Profits: {max_month_name} (${max_profit})\n")
    print(f"Greatest Decrease in Profits: {min_month_name} (${max_loss})\n")

list_write = ['Financial Analysis',
              '----------------------------------',
              'Total months: ' + str(month_count),
              "Total: $" + str(profit_loss_overtime),
              'Average Change: $' + str(round(avg_avg_change, 2)),
              'Greatest Increase in Profits: '+ max_month_name + " ($" + str(max_profit) +")",
              'Greatest Decrease in Profits: ' + min_month_name + "($" + str(max_loss)+ ")" ]

with open('analysis/exported_data.txt', 'w') as f:
     for line in list_write:
         f.write(line)
         f.write('\n')
         f.write('\n')