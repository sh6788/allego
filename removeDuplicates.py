
import requests

emailIds = [1962163,
31355901,
39928469,
1876027,
28166701,
35924254,
12004451,
2017868,
23654101,
1688554,
22915938714,
36095051,
34991351,
41324264269,]

for i in emailIds:
	#base of the endpoint we're going to call
	secondaryEmailEndpointURL = "https://api.hubapi.com/contacts/v1/secondary-email"
	#looping through the list of ids
	email_id = i
	#append the emailId to the URL for the endpoint
	secondaryEmailEndpoint = "{}/{}".format(secondaryEmailEndpointURL, email_id)
	#necessary auth token for the private app i created
	headers = {"Authorization": "Bearer pat-na1-79f5d4c0-3ec5-4eaffdsfs2df"}
	#actually call the API to get the secondary email addressess asscoiated with this id
	response = requests.get(secondaryEmailEndpoint, headers=headers)
	
	data = response.json()
	print('alook belo')
	print(data)
	print(data['secondaryEmails'])
	#put all of these secondary emails into a list (there can be more than 1 per contact)
	secondaryEmailList = data['secondaryEmails']
	for secondaryEmail in secondaryEmailList:
		#base of the delete endpoing
		deleteSecondaryEmailEndpointURL = "https://api.hubapi.com/contacts/v1/secondary-email"
		#looping through the list of the secondary emails (there might be more than 1)
		secondaryEmailtoDelete = secondaryEmail
		#step 1 of creating the endpoint URL
		deleteSecondaryEmailEndpoint1 = "{}/{}".format(secondaryEmailEndpointURL, email_id)
		#step 2 of creating the endpoint URL
		deleteSecondaryEmailEndpoint = "{}/email/{}".format(deleteSecondaryEmailEndpoint1, secondaryEmailtoDelete)
		#actually call the API to delete the secondary email
		response = requests.delete(deleteSecondaryEmailEndpoint, headers=headers)
