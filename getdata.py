import csv

country_dict = {}

def Hospitals():
	li = []
	row_id = 1
	with open('covid-data.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		data = list(spamreader)
		for i in range(len(data)):
			if i == 0:
				li.append(["id", "country_id", data[i][3], data[i][17], data[i][19], data[i][60]])
			else:
				four = data[i][17]
				five = data[i][19]
				six = data[i][60]

				if four != '':
					four = float(four)
				if five != '':
					five = float(five)
				if six != '':
					six = float(six)

				li.append([row_id, country_dict[data[i][2]], data[i][3], four, five, six])
				row_id += 1

	with open("data/hospitals.csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(li)

def CountryHealth():
	li = []
	row_id = 1
	countries = []
	with open('covid-data.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		data = list(spamreader)
		for i in range(len(data)):
			if i == 0:
				li.append(["id", "country_id", data[i][55], data[i][56], data[i][61], data[i][62], data[i][65]])
			else:
				if data[i][2] not in countries:
					four = data[i][55]
					five = data[i][56]
					six = data[i][61]
					seven = data[i][62]
					eight = data[i][65]

					if four != '':
						four = float(four)
					if five != '':
						five = float(five)
					if six != '':
						six = float(six)
					if seven != '':
						seven = float(seven)
					if eight != '':
						eight = float(eight)

					li.append([row_id, country_dict[data[i][2]], four, five, six, seven, eight])
					countries.append(data[i][2])
					row_id += 1

	with open("data/countryhealth.csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(li)

def CountryConditions():
	li = []
	row_id = 1
	countries = []
	with open('covid-data.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		data = list(spamreader)
		for i in range(len(data)):
			if i == 0:
				li.append(["id", "country_id", data[i][53], data[i][54], data[i][59]])
			else:
				if data[i][2] not in countries:
					four = data[i][53]
					five = data[i][54]
					six = data[i][59]

					if four != '':
						four = float(four)
					if five != '':
						five = float(five)
					if six != '':
						six = float(six)

					li.append([row_id, country_dict[data[i][2]], four, five, six])
					countries.append(data[i][2])
					row_id += 1

	with open("data/countryconditions.csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(li)

def CountryAge():
	li = []
	row_id = 1
	countries = []
	with open('covid-data.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		data = list(spamreader)
		for i in range(len(data)):
			if i == 0:
				li.append(["id", "country_id", data[i][50], data[i][51], data[i][52]])
			else:
				if data[i][2] not in countries:
					four = data[i][50]
					five = data[i][51]
					six = data[i][52]

					if four != '':
						four = float(four)
					if five != '':
						five = float(five)
					if six != '':
						six = float(six)

					li.append([row_id, country_dict[data[i][2]], four, five, six])
					countries.append(data[i][2])
					row_id += 1

	with open("data/countryage.csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(li)

def CovidNew():
	li = []
	row_id = 1
	with open('covid-data.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		data = list(spamreader)
		for i in range(len(data)):
			if i == 0:
				li.append(["id", "country_id", data[i][3], data[i][5], data[i][8], data[i][25], data[i][38]])
			else:
				four = data[i][5]
				five = data[i][8]
				six = data[i][25]
				seven = data[i][38]

				if four != '':
					four = float(four)
				if five != '':
					five = float(five)
				if six != '':
					six = float(six)
				if seven != '':
					seven = float(seven)

				li.append([row_id, country_dict[data[i][2]], data[i][3], four, five, six, seven])
				row_id += 1

	with open("data/covidnew.csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(li)

def CovidTotals():
	li = []
	row_id = 1
	with open('covid-data.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		data = list(spamreader)
		for i in range(len(data)):
			if i == 0:
				li.append(["id", "country_id", data[i][3], data[i][4], data[i][7], data[i][26], data[i][34], data[i][37]])
			else:
				four = data[i][4]
				five = data[i][7]
				six = data[i][26]
				seven = data[i][34]
				eight = data[i][37]

				if four != '':
					four = float(four)
				if five != '':
					five = float(five)
				if six != '':
					six = float(six)
				if seven != '':
					seven = float(seven)
				if  eight != '':
					eight = float(eight)

				li.append([row_id, country_dict[data[i][2]], data[i][3], four, five, six, seven, eight])
				row_id += 1

	with open("data/covidtotals.csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(li)

def CovidRates():
	li = []
	row_id = 1
	with open('covid-data.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		data = list(spamreader)
		for i in range(len(data)):
			if i == 0:
				li.append(["id", "country_id", data[i][3], data[i][31], data[i][32], data[i][35], data[i][36]])
			else:
				four = data[i][31]
				five = data[i][32]
				six = data[i][35]
				seven = data[i][36]

				if four != '':
					four = float(four)
				if five != '':
					five = float(five)
				if six != '':
					six = float(six)
				if seven != '':
					seven = float(seven)

				li.append([row_id, country_dict[data[i][2]], data[i][3], four, five, six, seven])
				row_id += 1

	with open("data/covidrates.csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(li)

def Countries():
	li = []
	row_id = 1
	countries = []
	with open('covid-data.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		data = list(spamreader)
		for i in range(len(data)):
			if i == 0:
				li.append(["id", data[i][0], data[i][1], data[i][2], data[i][48], data[i][49]])
			else:
				if data[i][2] not in countries:
					five = data[i][48]
					six = data[i][49]

					if five != '':
						five = float(five)
					if six != '':
						six = float(six)
					li.append([row_id, data[i][0], data[i][1], data[i][2], five, six])
					countries.append(data[i][2])
					country_dict[data[i][2]] = row_id
					row_id += 1

	with open("data/countries.csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(li)

def main():
	Countries()
	CovidRates()
	CovidTotals()
	CovidNew()
	CountryAge()
	CountryConditions()
	CountryHealth()
	Hospitals()

if __name__ == "__main__":
	main()
