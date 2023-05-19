import os
import csv

#set csv path
poll_csv=os.path.join('..','PyPoll','Resources','election_data.csv')

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

winner=""
winner_votes=0
for candidate_name, votes in candidate_votes.item():
    percentage=round(votes/total_votes*100,3)
    print(f"{candidate_name}: {percentage}% ({votes})")
    if votes>winner_votes:
        winner=candidate_name
        winner_votes=votes
print("----------------")
print(f"Winner: {winner}")
print("------------------")