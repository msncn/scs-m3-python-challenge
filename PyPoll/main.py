# Read the CSV for PyPoll
import os
import csv

# PyPoll file path
py_poll = os.path.join("Resources", "election_data.csv")

total_votes = -1

# Read PyPoll csv file
with open(py_poll,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    print(f"PyBank CSV Header: {csv_header}")
    
    # data = list(csvreader) (this is an alternative to calculate the # of votes)
    # total_votes = len(data)

    charles_count = diana_count = raymon_count = 0
    charles_percent = diana_percent = raymon_percent = 0
    total_votes += 1
    
    for row in csvreader:
        
        # total # of votes
        total_votes += 1

        # # of votes for each candidates 
        if row[2] == "Charles Casper Stockham":
            charles_count += 1
        elif row[2] == "Diana DeGette":
            diana_count += 1
        elif row[2] == "Raymon Anthony Doane":
            raymon_count += 1

    
    # % of votes each candidate won
    charles_percent = round((charles_count / total_votes)* 100, 3)
    diana_percent = round((diana_count / total_votes)* 100, 3)
    raymon_percent = round((raymon_count / total_votes)* 100, 3)

    # find the winner
    voteresults = {"Charles Casper Stockham": charles_count,
                   "Diana DeGette": diana_count,
                   "Raymon Anthony Doane": raymon_count}
    winner = max(voteresults,key=voteresults.get)

# Print the analysis
print("------------------------------")
print("Election Results")
print("------------------------------")
print(f"Total Votes: {total_votes}")
print(f"Charles Casper Stockham: {charles_percent}% ({charles_count})")
print(f"Diana DeGette: {diana_percent}% ({diana_count})")
print(f"Raymon Anthony Doane: {raymon_percent}% ({raymon_count})")
print(f"Winner: {winner}")

# Export it into a txt file to the "analysis" folder
py_poll_analysis = os.path.join("analysis","election_analysis.txt")

with open(py_poll_analysis, "w") as textfile:
    textfile.write("Election Results")
    textfile.write('\n')
    textfile.write("------------------------------")
    textfile.write('\n')
    textfile.write(f"Total Votes: {total_votes}")
    textfile.write('\n')
    textfile.write(f"Charles Casper Stockham: {charles_percent}% ({charles_count})")
    textfile.write('\n')
    textfile.write(f"Diana DeGette: {diana_percent}% ({diana_count})")
    textfile.write('\n')
    textfile.write(f"Raymon Anthony Doane: {raymon_percent}% ({raymon_count})")
    textfile.write('\n')
    textfile.write("------------------------------")
    textfile.write('\n')
    textfile.write(f"Winner: {winner}")
    textfile.write('\n')
    textfile.write("------------------------------")
