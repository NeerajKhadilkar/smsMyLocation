

'''

send the location via sms to Mentioned Phone Numbers

required fields sender phone number,API Key for FAST2SMS and actual message


'''


import requests,urllib3,json


# phone number you want to send message 
sender=+91-#######

YOUR_API_KEY=***************

message="This is Test Message"


class smsLocation:


	def __init__(self,YOUR_API_KEY,sender,message):

		self.YOUR_API_KEY=YOUR_API_KEY
		self.sender=sender
		self.message=message

	def getLocation(self):

		http = urllib3.PoolManager()
		r = http.request('GET', 'http://ipinfo.io/json')

		if r:
			data = json.loads(r.data.decode('utf-8'))

			return data


		else:
			return None


	def sendMessage(self):

		get_curr_location=self.getLocation()

		print(get_curr_location)

		import requests

		url = "https://www.fast2sms.com/dev/bulkV2"

		querystring = {"authorization":self.YOUR_API_KEY,"message":self.message,"language":"english","route":"q","numbers":self.sender}

		headers = {
		    'cache-control': "no-cache"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		print(response.text)

		status=response.json()

		print(status['message'][0])



obj=smsLocation(YOUR_API_KEY,sender,message)

obj.sendMessage()



