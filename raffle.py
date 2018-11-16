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

#for row in entries:
#	print("\tname: %s amount: %s" %(row['name'], row['amount']))

winning_number = random.randint(0, total_wedge)
print("winning_number: %i" %(winning_number))

current_person = entries[0]['name']
win_lower_threshold = 0
for row in entries:
	win_upper_threshold = win_lower_threshold + row['amount']
	print("\tname: %s win_lower_threshold: %i" %(row['name'], win_lower_threshold))
	print("\tname: %s win_upper_threshold: %i" %(row['name'], win_upper_threshold))
	if (win_lower_threshold <= winning_number and winning_number < win_upper_threshold):
		print("%s won!" %(row['name']))
		break		
	win_lower_threshold += row['amount']
	current_person = row['name']
