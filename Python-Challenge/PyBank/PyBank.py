#thank you David Chao for you're wonderful help with this code.
import os, csv
from pathlib import Path

#create the path
budgetPath = os.path.join("Resources", "budget_data.csv")
analysisPath = os.path.join("Analysis", "analysisResult.txt")
totalMonth = 0
totalProfit = 0
previousProfit = 0
monthChange = 0
changeCount = 0
totalChange = 0
greatestInc = 0
greatestIncMonth = ""
greatestDec = 0
greatestDecMonth = ""



with open(budgetPath) as budgetEnd:
    csvreader = csv.reader(budgetEnd)
    header = next(csvreader)

    for row in csvreader:     
        totalMonth += 1
        totalProfit += int(row[1])
        currentProfit = int(row[1])

        if previousProfit != 0:
            monthChange = currentProfit - previousProfit
            totalChange += monthChange
            changeCount += 1

            if monthChange > greatestInc:
                greatestInc = monthChange
                greatestIncMonth = row[0]

            if monthChange < greatestDec:
                greatestDec = monthChange
                greatestDecMonth = row[0]

          
        previousProfit = currentProfit


    

output = f"""
Financial Analysis
----------------------------
Total Months: {totalMonth}
Total: ${totalProfit}
Average Change: ${totalChange / changeCount:.2f}
Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})
Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})
"""

print(output)

with open(analysisPath, "w") as resultsEnd:
    resultsEnd.write(output)