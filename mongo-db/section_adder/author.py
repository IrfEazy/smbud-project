import json
import numpy as np

RND_DATE = np.random.RandomState(674516585) 
DATES_FILE = 'data/random_dates.json'

def email_bio_date_adder(in_file, out_file):
	with open(in_file) as f:
		my_dataset = json.load(f)
	with open(DATES_FILE) as d:
		dates = json.load(d)

	for i in range(len(my_dataset)):
		doc = my_dataset[i]
		date = dates[RND_DATE.randint(len(dates))]['date']
		doc['date'] = date
		if 'year' in doc.keys():
			doc.pop('year')
		if 'authors' in doc.keys():
			for j in range(len(doc['authors'])):
				if 'name' in doc['authors'][j].keys() and '_id' in doc['authors'][j].keys():
					doc['authors'][j]['email'] = doc['authors'][j]['name'].replace(' ','.').lower() + doc['authors'][j]['_id'][-2:] + '@gmail.com'
					doc['authors'][j]['bio'] = 'My name is ' + doc['authors'][j]['name'] + ((' and I\'m currently working for ' + doc['authors'][j]['org']) if 'org' in doc['authors'][j].keys() else '')

	with open(out_file, 'w') as out:
		json.dump(my_dataset, out, indent=4)
