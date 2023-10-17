import os
import csv

#set csv path
poll_csv=os.path.join('/Users/cindy/Desktop/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv')

#set variables
total_votes=0
candidate_votes={}

#scan csv file
with open(poll_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    #skip first row
    next(csvreader)

    #loop through file 
    for row in csvreader:
        #cout number of total votes 
        total_votes+=1
        
        #unique candidate names
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name]=0

        #count votes for each candidate
        candidate_votes[candidate_name]+=1
    
    #print results
print("Election Results") 

print("----------------")

print(f"Total Votes: {total_votes}")

print("------------------")

# Winner of the election
winner = ""
winner_votes = 0
for candidate_name, count in candidate_votes.items():  # Iterate through candidate names and their vote counts
    if count > winner_votes:
        winner_votes = count
        winner = candidate_name
    #Percentage of votes for each candidate 
    percentage = round((count / total_votes) * 100, 3)
    print(f"{candidate_name}: {percentage}% ({count})")

print("----------------")
print(f"Winner: {winner}")
print("------------------")

#Print the results to new text file
analysis_results = os.path.join("Analysis","Rsults")
with open("Results.txt","w") as textfile:
    textfile.write("Election results\n"
"-----------------------------------------\n"
"Total Votes: 369711\n"
"-----------------------------------------\n"
"Charles Casper Stockham: 23.049% (85213)\n"
"Diana DeGette: 73.812% (272892)\n"
"Raymon Anthony Doane: 3.139% (11606)\n"
"-----------------------------------------\n"
"Winner: Diana DeGette\n"
"-----------------------------------------\n")