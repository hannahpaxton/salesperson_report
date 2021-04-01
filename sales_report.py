"""Generate sales report showing total melons each salesperson sold."""

#Ideally, instead of maintaining two lists that depend on the index of one another refering to the same sales data, this should be saved in a dictionary! 
salespeople = [] #create an open list to keep track of salespeople in file (will append to list from loop)
melons_sold = [] #create an open list to keep track of melons sold in file (will append to list from loop)

f = open('sales-report.txt') #open the sales report
for line in f: #initiate loop - look at file line by line
    line = line.rstrip() #strip whitespace from the end of the line
    entries = line.split('|') #split the line on the '|' character, creating 3 separate item for salesperson, total, and number of melons

    salesperson = entries[0] #save the first item in entries to a variable called salesperson
    melons = int(entries[2]) #save the third item in entries as an integer in a variable called melon

    if salesperson in salespeople: #create a coniditional that checks if salesperson has been added to the list of salespeople
        position = salespeople.index(salesperson) #if they have, get the index where the name is saved in the salesperson list and save it to the variable position

        melons_sold[position] += melons #use the position variable to add the number of melons we saved in the melons variable to the same position that salesperson is found at in the salespeople list
    else: #if salesperson is not found in the salespeople list
        salespeople.append(salesperson) #the name saved in salesperson is appended to the salespeople list
        melons_sold.append(melons) #the value saved in melons is appeneded to the melons_sold list


for i in range(len(salespeople)): #initiate loop - look at each item in the salespeople list individually
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #print an f statement that displays "Name of salesperson at given index sold the number of melons at the matching index"



