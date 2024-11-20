
import requests
import csv
from datetime import timedelta, datetime, date

GET_CONTACT_API = "https://api.hubapi.com/contacts/v1/contact/vid/{recordId}/profile"
field_list = []

with open('records2.csv', 'r') as file:
	my_reader = csv.reader(file, delimiter=",")
	next(my_reader, "Record ID - Contact")  # skip the headers
	for row in my_reader:
		record_id = row[0]
		contact_url = GET_CONTACT_API.format(recordId = record_id)
#UPDATE HUBSPOT KEY BELOW
		headers = {"Authorization": "Bearer gfdgd573fd-9837082f22df"}
		response = requests.get(contact_url, headers=headers)
		data = response.json()

		
		
		for key, value in data['properties'].items():
			if key in ['hs_latest_source','hs_latest_source_data_1','hs_latest_source_data_2']:
				number_of_changes = len(data['properties']['hs_latest_source']['versions'])
				counter = 0
				print(record_id)
				while counter < number_of_changes:
					add_field = {}
					try: 
						hs_latest_source = data['properties']['hs_latest_source']['versions'][counter]['value']
					except Exception:
						hs_latest_source = "no value"
					try: 
						hs_latest_source_data_1 = data['properties']['hs_latest_source_data_1']['versions'][counter]['value']
					except Exception:
						hs_latest_source_data_1 = "no value"
					try:
						hs_latest_source_data_2 = data['properties']['hs_latest_source_data_2']['versions'][counter]['value']
					except Exception:
						hs_latest_source_data_2 = "no value"
					timestamp = data['properties']['hs_latest_source']['versions'][counter]['timestamp']
					timestamp_formatted = datetime.fromtimestamp(timestamp / 1e3)
					add_field['hs_latest_source'] = hs_latest_source
					add_field['hs_latest_source_data_1'] = hs_latest_source_data_1
					add_field['hs_latest_source_data_2'] = hs_latest_source_data_2
					add_field['timestamp'] = timestamp_formatted
					add_field['contactId'] = record_id
					if add_field in field_list:
						counter += 1
					else: 
						field_list.append(add_field)
						counter += 1
					#if counter == 1:
					#	field_names = ['hs_latest_source_data_1', 'hs_latest_source', 'hs_latest_source_data_2', 'timestamp', 'contactId']
					#	with open ('Latest Source.csv', 'w') as csvfile:
					#		writer = csv.DictWriter(csvfile, fieldnames=field_names)
					#		writer.writeheader()
					#		writer.writerow(add_field)
#
					


with open('test.csv', "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["hs_latest_source_data_1", "hs_latest_source", "hs_latest_source_data_2", "timestamp", "contactId"], delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerows(field_list)


		




			
			



					
				
	
