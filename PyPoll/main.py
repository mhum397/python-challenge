import os
import csv
import sys

# Path to collect budget data from the Resources folder
electiondataCSV = os.path.join('.', 'Resources', 'election_data.csv')


# Read in the CSV file
with open(electiondataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Set empty lists to gather voting and candidate data
    votes = []
    candidate_list = []
    
    # Loop through the data
    for row in csvreader:
        
        votes.append(row[0])
        candidate_list.append(row[2])
    
    # Calculate total votes and count occurences in list
    total_votes = len(votes)
    khan_count = candidate_list.count('Khan')
    correy_count = candidate_list.count('Correy')
    li_count = candidate_list.count('Li')
    otooley_count = candidate_list.count("O'Tooley")

    if khan_count > correy_count and khan_count > li_count and khan_count > otooley_count:

        winner = "Khan"
    
    elif correy_count > khan_count and correy_count > li_count and correy_count > otooley_count:

        winner = "Correy"

    elif li_count > khan_count and li_count > correy_count and li_count > otooley_count:

        winner = "Li"

    elif otooley_count > khan_count and otooley_count > correy_count and otooley_count > li_count:

        winner = "O'Tooley"  

# Print out results to terminal    
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
print(f"Khan: {round((khan_count / total_votes * 100),3)}% ({khan_count})")
print(f"Correy: {round((correy_count / total_votes * 100),3)}% ({correy_count})")
print(f"Li: {round((li_count / total_votes * 100),3)}% ({li_count})")
print(f"O'Tooley: {round((otooley_count / total_votes * 100),3)}% ({otooley_count})")
print("----------------------------------")
print(f"Winner: {winner}")
print("----------------------------------")

# Print to Result.txt file
sys.stdout = open('election_results.txt','wt')
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
print(f"Khan: {round((khan_count / total_votes * 100),3)}% ({khan_count})")
print(f"Correy: {round((correy_count / total_votes * 100),3)}% ({correy_count})")
print(f"Li: {round((li_count / total_votes * 100),3)}% ({li_count})")
print(f"O'Tooley: {round((otooley_count / total_votes * 100),3)}% ({otooley_count})")
print("----------------------------------")
print(f"Winner: {winner}")
print("----------------------------------")
sys.stdout.close
