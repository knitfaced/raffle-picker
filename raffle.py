import csv
import random

entries = []
total_wedge = 0

with open('DonationsList.csv') as csv_file:
	#strip null bytes
	csv_dict = csv.DictReader(x.replace('\0', '') for x in csv_file)

	#parse the csv
	line_count = 0
	for row in csv_dict:
		name = row['Display name']
		amount = float(row['Amount'])
		entries.append({'name': name, 'amount': amount})
		total_wedge += amount

print("total_wedge: %f" %(total_wedge))

for row in entries:
	print("\tname: %s amount: %s" %(row['name'], row['amount']))

winning_number = random.randint(0, total_wedge)
print("winning_number: %f" %(winning_number))



#	current_person = ""
#	current_money = 0
#	for row in csv_dict:
#		current_money += float(row['Amount'])
#		current_person = row['Display name']