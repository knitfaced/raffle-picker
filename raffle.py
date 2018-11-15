import csv

with open('DonationsList.csv') as csv_file:
	#strip null bytes
	csv_reader = csv.reader(x.replace('\0', '') for x in csv_file)

	#parse the csv
	line_count = 0
	for row in csv_reader:
		print(row)
		if line_count == 0:
			print("Column names are %s" %(row))
			line_count += 1
		else:
			print("\tname: %s email: %s" %(row[0], row[9]))
			line_count += 1
	print("Processed %s lines." %(line_count))