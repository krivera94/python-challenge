import csv 

with open("budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    months = []
    losses = []
    
    total = 0
    a_change = 0
    m_change = 0
    m_count = 0
    d1 = 0
    d2 = 0
    dl1 = 0
    dl2 = 0
    l1 = 0
    l2 = 0
    
    for row in csvreader:
        month = row[0]
        loss = row[1]
        months.append(month)
        losses.append(loss)
        
    m_count = len(months)
    
for l1 in range (m_count):
    total = total + int(losses[l1])
                        
for l2 in range (m_count-1):
    a_change = a_change +(float(losses[l2+1]) - float(losses[l2]))
    
    m_change = (float(losses[l2+1]) - float(losses[l2]))
    if m_change > d1:
        d1 = m_change
        dl1 = l2
    else:
        d1=d1
        
    if m_change < d2:
        d2 = m_change
        dl2 = l2
    else:
        d2 = d2
        
analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total Amount Ps/Ls: ${total}\n\
Average Changes: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[dl1+1]} (${int(d1)})\n\
Greatest Decrease in Profits: {months[dl2+1]} (${int(d2)})\n'

print(analysis)
