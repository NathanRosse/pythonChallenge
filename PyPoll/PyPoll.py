import os, csv
from pathlib import Path

pollPath = os.path.join("Resources", "election_data.csv")
analysisPath = os.path.join("Resources", "analysisResult.txt")

totalVotes = 0
#do i have to create a dict for candidates?
totalCandidates = 0
candidateVotes = 0
charlesVotes = 0
dianaVotes = 0
raymonVotes = 0
candidate1 = "Charles Casper Stockham"
candidate2 = "Diana DeGette"
candidate3 = "Raymon Anthony Doane"


with open(pollPath) as pollEnd:
    csvreader = csv.reader(pollEnd)
    header = next(csvreader)

    for row in csvreader:
        totalVotes += 1
        if row[2] == candidate1:
            charlesVotes += 1
        if row[2] == candidate2:
            dianaVotes += 1
        if row[2] == candidate3:
            raymonVotes += 1


charlesPercent = (charlesVotes / totalVotes) * 100
dianaPercent = (dianaVotes / totalVotes) * 100
raymonPercent = (raymonVotes / totalVotes) * 100
        

winner = max(charlesPercent, dianaPercent, raymonPercent)
if winner == charlesPercent:
    winner = candidate1
if winner == dianaPercent:
    winner = candidate2
if winner == raymonPercent:
    winner = candidate3


output = f"""
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
Charles Casper Stockham: {charlesPercent:.3f}% ({charlesVotes})
Diana DeGette: {dianaPercent:.3f}% ({dianaVotes})
Raymon Anthony Doane: {raymonPercent:.3f}% ({raymonVotes})
-------------------------
Winner: {winner}
-------------------------
"""

print(output)

with open(analysisPath, "w") as resultsEnd:
    resultsEnd.write(output)
