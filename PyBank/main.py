import csv
import os
def average(num):
  ave = float(sum(num)/len(num))
  return ave
totalmonth = 0
netamount = 0
monthchange = []
monthmax = []
monthmin = []
change = 0.0
currentvalue = 0
averagechange = 0.0
maxchange = 0
minchange = 0
budget_csv = os.path.join("budget_data.csv")
with open (budget_csv, newline = "") as csvfile:
    csvreader= csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        totalmonth =  totalmonth +1
        netamount = netamount + int(row[1])
        change = (int(row[1])- currentvalue)
        
        #maxprofit = str(monthchange[averagechange.index(max(averagechange))])
        #minprofit = str(monthchange[averagechange.index(min(averagechange))])

        if currentvalue != 0:
            monthchange.append(change)
           
        currentvalue = int(row[1])
    
    maxmonth = max(monthchange)
    minmonth = min(monthchange)

print (str(totalmonth))
print (str(netamount))


averagechange = round(average(monthchange),2)
print (str(averagechange))
print (str(maxmonth))
print (str(minmonth))