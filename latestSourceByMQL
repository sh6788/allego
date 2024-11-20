
import requests
import csv
from datetime import timedelta, datetime, date

GET_CONTACT_API = "https://api.hubapi.com/contacts/v1/contact/vid/{recordId}/profile"
LEAD_SOURCE_DICT = {}
lead_source_list = []

#file contains record Id and MQL Date from Hubspot
with open('records.csv', 'r') as file:
	my_reader = csv.reader(file, delimiter=",")
	next(my_reader, "Record ID - Contact")  # skip the headers
	for row in my_reader:
		record_id = row[0]
		mql_date = row[1]
		mql_date_object = datetime.strptime(mql_date, '%Y-%m-%d').date()
		contact_url = GET_CONTACT_API.format(recordId = record_id)
		#contact_url = GET_CONTACT_API.format(recordId = 48410853263)
		#contact_url = GET_CONTACT_API.format(recordId = 14507301)
    #ADD HUBSPOT KEY BELOW
		headers = {"Authorization": "Bearer pat-na1-79f5d4c0-3ec5-4eaf-fdsil938hfa8998-f"}
		response = requests.get(contact_url, headers=headers)
		
		data = response.json()
	
		propertiesDict = data['properties']
		counter = 0
		for key, value in propertiesDict.items():
			if (key == "hs_latest_source"):
				versions = value['versions']
				#print('BELOW IS THE START OF A VERSION')
				#print(versions)
				for i in versions:
					timestamp = i['timestamp']
					timestamp_object = datetime.fromtimestamp(timestamp / 1e3)
					timestamp_dateobject = timestamp_object.date()
					date_difference = mql_date_object - timestamp_dateobject
					if 0 < date_difference.days < 30:
						i['contact_id'] = record_id
						i['mql_date'] = mql_date_object
						i['action_date'] = timestamp_dateobject
						lead_source_list.append(i)
						print('this is here')
						break
		field_names = ['value','latest source', 'source-type', 'source-id', 'source-label', 'updated-by-user-id', 'timestamp', 'selected', 'contact_id', 'mql_date', 'action_date','is-encrypted', 'source-vids', 'data-sensitivity']
		with open ('Latest Source.csv', 'w') as csvfile:
			writer = csv.DictWriter(csvfile, fieldnames=field_names)
			writer.writeheader()
			writer.writerows(lead_source_list)



			
			
