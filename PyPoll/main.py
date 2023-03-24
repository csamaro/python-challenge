import csv
import os

print("Election Results\n")
print("-------------------------\n")

#create variables for data to be stored and initialize them to 0
voter_counts = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0
cv_percent = 0.0
dv_percent = 0.0
rv_percent = 0.0


csvpath = os.path.join('Resources', 'election_data.csv') 

# open election_data and read it in 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    
    #print(csvreader) #where it is located

    csv_header = next(csvreader) #skips first row
    #print(f"CSV header {csv_header}")

    for row in csvreader:
        voter_counts = voter_counts + 1 #counting all votes
        #checking each vote, updating counter for each candidate
        if(row[2] == "Charles Casper Stockham"):
            charles_votes = charles_votes + 1
        elif(row[2] == "Diana DeGette"):
            diana_votes = diana_votes + 1
        elif(row[2] == "Raymon Anthony Doane"):
            raymon_votes = raymon_votes + 1
        else: 
            print("Lost votes") #checks to see if we have any garbage data

#now determine who won the election
if (charles_votes >= diana_votes) and (charles_votes >= raymon_votes):
    winner = "Charles Casper Stockham"
elif (diana_votes >= charles_votes) and (diana_votes >= raymon_votes):
    winner = "Diana DeGette"
elif (raymon_votes >= charles_votes) and (raymon_votes >= diana_votes):
    winner = "Raymon Anthony Doane"
else:
    winner = "It's A Tie :o"

#calculate vote percentage of each candidate
cv_percent = (charles_votes / voter_counts)*100
dv_percent = (diana_votes / voter_counts)*100
rv_percent = (raymon_votes / voter_counts)*100

print(f"Total Votes: {voter_counts}\n")
print("-------------------------\n")
print(f"Charles Casper Stockham: {round(cv_percent, 3)}% ({charles_votes})\n")
print(f"Diana DeGette: {round(dv_percent, 3)}% ({diana_votes})\n")
print(f"Raymon Anthony Doane: {round(rv_percent, 3)}% ({raymon_votes})\n")
print("-------------------------\n")
print(f"Winner: {winner}")
print("-------------------------\n")

#now creating variable to write to a txt file
list_write = ['Election Results',
              "-------------------------",
              "Total Votes: " + str(voter_counts), 
              "-------------------------",
              "Charles Casper Stockham: "+ str(round(cv_percent, 3)) +"% (" + str(charles_votes)+")",
              "Diana DeGette: "+ str(round(dv_percent, 3)) +"% (" + str(diana_votes) + ")",
              "Raymon Anthony Doane: "+ str(round(rv_percent, 3)) + "% ("+ str(raymon_votes) +")",
              "-------------------------",
              "Winner: "+ str(winner),
              "-------------------------"]
#print(list_write)

#writing to txt file / creating one if there is none in analysis folder
with open('analysis/exported_data.txt', 'w') as f:
     for line in list_write:
         f.write(line)
         f.write('\n')
         f.write('\n')