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
    delta1 = 0
    delta2 = 0
    delta_line1 = 0
    delta_line2 = 0
    loop1 = 0
    loop2 = 0
    
    for row in csvreader:
        month = row[0]
        loss = row[1]
        months.append(month)
        losses.append(loss)
        
    m_count = len(months)
    
for loop1 in range (m_count):
    total = total + int(losses[loop1])
                        
for loop2 in range (m_count-1):
    a_change = a_change +(float(losses[loop2+1]) - float(losses[loop2]))
    
    m_change = (float(losses[loop2+1]) - float(losses[loop2]))
    if m_change > delta1:
        delta1 = m_change
        delta_line1 = loop2
    else:
        delta1=delta1
        
    if m_change < delta2:
        delta2 = m_change
        delta_line2 = loop2
    else:
        delta2 = delta2
