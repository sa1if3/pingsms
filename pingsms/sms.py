import requests


"""
Get Transactional and Promotional Balance of The User
Input Parameter's Required:key
Output: JSON
"""
def get_sms_balance(custom_data):
	url = "https://www.pingsms.in/api/getsmsbalance?key="+custom_data["key"]

	payload={}
	headers = {
	  'X-Authorization': custom_data["key"]
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	return response.json()

"""
Get List of Sender Ids of The User
Input Parameter's Required:key
Output: JSON
"""

def get_sender_id(custom_data):
	url = "https://www.pingsms.in/api/getsenderids?key="+custom_data["key"]

	payload={}
	headers = {
	  'X-Authorization': custom_data["key"]
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	return response.json()

"""
Get Job Report of the User
Input Parameter's Required:key,job_id,report_date
Output: JSON
"""

def get_job_report(custom_data):
	url = "https://www.pingsms.in/api/getjobinfo?key="+custom_data["key"]+"&jid="+custom_data["job_id"]+"&date="+custom_data["report_date"]

	payload={}
	headers = {
	  'X-Authorization': custom_data["key"]
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	return response.json()


"""
Get SMS sent reports of the User
Input Parameter's Required:key,report_date,product
Output: JSON
"""

def get_sent_sms_reports(custom_data):
	url = "https://www.pingsms.in/api/getsentreports?key="+custom_data["key"]+"&date="+custom_data["report_date"]+"&product="+custom_data["product"]

	payload={}
	headers = {
	  'X-Authorization': custom_data["key"]
	}

	response = requests.request("GET", url, headers=headers, data=payload)
	return response.json()

"""
Send Single SMS
Input Parameter's Required:key,sender,mobile,language,product,message, template
Output: JSON
"""

def send_single_sms(custom_data):
	url = "https://www.pingsms.in/api/sendsms?key="+custom_data["key"]+"&sender="+custom_data["sender"]+"&mobile="+custom_data["mobile"]+"&language="+custom_data["language"]+"&product="+custom_data["product"]+"&message="+custom_data["message"]+"&template="+custom_data["template"]

	payload={}
	headers = {
	  'X-Authorization': custom_data["key"]
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	return response.json()

"""
Send Multiple SMS
Input Parameter's Required:key,sender,mobile(multiple and comma separated),language,product,message,template
Output: JSON
"""

def send_multiple_sms(custom_data):
	url = "https://www.pingsms.in/api/sendmultiplesms?key="+custom_data["key"]+"&sender="+custom_data["sender"]+"&mobile="+custom_data["mobile"]+"&language="+custom_data["language"]+"&product="+custom_data["product"]+"&message="+custom_data["message"]+"&template="+custom_data["template"]

	payload={}
	headers = {
	  'X-Authorization': custom_data["key"]
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	return response.json()