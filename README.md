# Python Pingsms API Package
 This is a python package for https://pingsms.in API. If you are looking for API usage in PHP [click here!](https://github.com/sa1if3/Quickstart-guide-on-sending-SMS-using-API)
 
 ## Installation
 The package is located at [PyPI](https://pypi.org/project/pingsms-api/) and can be installed with a ```pip``` command. To install the package simply run :-
 ```
 pip install pingsms-api 
 ```
 ## Usage
 ### Importing the package
 To start using the package first we need to import the package.<br/>
 **Note: Our package name is ```pingsms-api``` but from now we will be using ```pingsms``` only for all our tasks.** <br/>
 To import the package run the following command:-
 ```
 import pingsms
 ```
 ### Input
 Only one variable of dictionary data type is sent to the methods. A sample dictionary variable is provided for reference:<br/>
 ```python
 """
 Sample Variable
 """
 custom_data = {
  "key": "AMjdkshmsaZdoV6PGWoSbejmEgFZ905EdmaanahwqkwNVc ",
  "job_id": "021839426237963",
  "report_date":"2021-06-12",
  "product":"1",
  "language":"1",
  "sender":"PNGSMS",
  "mobile":"1232123451",
  "template":"282222382902",
  "message":"Hello World!"
}
 ```
 There are total 9 elements (known as key:value pairs) allowed in the dictionary. Any additional parameters are ignored.
 1. **key :** A user is identified by a unique hashed key. This key can be generated from the https://pingsms.in user panel. All pingsms customers have free access to API keys. This is an mandatory field required by all the methods.
 2. **job_id :** The Job Id number. This parameter is only used in the method ```get_job_report()```
 3. **report_date :** Date Of Report in YYYY-MM-DD Format.This parameter is used in the method ```get_job_report()``` and ```get_sent_sms_reports()```
 4. **product :** Choose between two product types <br/>1 - Transactional<br/>2 - Promotional <br/>This parameter is only used in the method ```send_single_sms()``` and ```send_multiple_sms(custom_data)```
 5. **language :** Choose between two language formats <br/>1 - English<br/>2 - Unicode (Regional Language) <br/>This parameter is only used in the method ```send_single_sms()``` and ```send_multiple_sms(custom_data)```
 6. **sender :**  	User's approved 6 characters Sender Id.<br/>This parameter is only used in the method ```send_single_sms()``` and ```send_multiple_sms(custom_data)```
 7. **mobile :**  	10 digit recipient mobile number. (In case of multiple sms mobile numbers should be provide in comma(,) separated form).<br/>This parameter is only used in the method ```send_single_sms()``` and ```send_multiple_sms(custom_data)```
 8. **template :** Authorised Template number of the user.<br/>This parameter is only used in the method ```send_single_sms()``` and ```send_multiple_sms(custom_data)```
 9. **message :** Authorised message format against the Template number.<br/>This parameter is only used in the method ```send_single_sms()``` and ```send_multiple_sms(custom_data)```
 ### Methods
 There are total of 5 available methods:
 1. **get_sms_balance(custom_data) :** <br/>Get Transactional and Promotional Balance of The User.<br/>Input Parameter's Required:key <br/>Output: JSON 
 2. **get_sender_id(custom_data) :** <br/>Get List of Sender Ids of The User. <br/>Input Parameter's Required:key <br/> Output: JSON
 3. **get_job_report(custom_data) :** <br/>Get Job Report of the User. <br/>Input Parameter's Required:key,job_id,report_date<br/>Output: JSON
 4. **get_sent_sms_reports(custom_data) :** <br/>Get SMS sent reports of the User. <br/>Input Parameter's Required:key,report_date,product <br/>Output: JSON
 5. **send_single_sms(custom_data) :** <br/>Send Single SMS. <br/>Input Parameter's Required:key,sender,mobile,language,product,message, template<br/>Output: JSON
 6. **send_multiple_sms(custom_data) :** <br/>Send Multiple SMS. <br/>Input Parameter's Required:key,sender,mobile(multiple and comma separated),language,product,message,template<br/>Output: JSON
 ### Examples
  ```python
 """
 Example 1
 """
 import pingsms
 custom_data = {
  "key": "AMjdkshmsaZdoV6PGWoSbejmEgFZ905EdmaanahwqkwNVc ",
}
pingsms.get_sms_balance(custom_data)

 ```
 
  ```python
 """
 Example 2
 """
 import pingsms
 custom_data = {
  "key": "AMjdkshmsaZdoV6PGWoSbejmEgFZ905EdmaanahwqkwNVc ",
  "product":"1",
  "language":"1",
  "sender":"PNGSMS",
  "mobile":"1232123451",
  "template":"282222382902",
  "message":"Hello World!"
}
pingsms.send_multiple_sms(custom_data)
 ```
 ### Output
All outputs are returned in the form of JSON.
```json
"""
Example 1 Output
"""
{
    "code": 201,
    "status": "Success",
    "message": "User balance details found",
    "available_balance": {
        "transactional_balance": 9248,
        "promotional_balance": 1029
    }
}
```
```json
"""
Example 2 Output
"""
{
    "code": 201,
    "status": "Success",
    "message": "Message Sent",
    "job_id": "11312351841231313"
}
```
## Error Codes
| Error Code   | Meaning                                                                                                                                                                                                                    |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unauthorized | Incorrect API key or the account is blocked.                                                                                                                                                                               |
| 1            | This error occurs when no recepients found.                                                                                                                                                                                |
| 2            | This error occurs when no sender name specied.                                                                                                                                                                             |
| 3            | Invalid Sender Id for this domain. This error appears if you use an  Sender Id non specified for your account.                                                                                                             |
| 4            | This error occurs when Language id  is missing or not specified. Choose between two language formats                                      1 - English                                      2 - Unicode (Regional Language) |
| 5            | This error occurs when Product id is  missing or not specified. Choose between two Product types                                      1 - Transactional                                      2 - Promotional               |
| 6            | This error occurs when no Message  Content is found. This error occurs when message content is missing.                                                                                                                    |
| 11           | This error occurs when Message size  exceeds the given limit. Please check your account balance and message  size.                                                                                                         |
| 12           | Mobile numbers should not more than  500. This error occurs when the number of mobile number in multiple sms  exceeds 500.                                                                                                 |
| 15           | This error occurs when Job Id is missing.                                                                                                                                                                                  |
| 17           | This error occurs when Date is missing.                                                                                                                                                                                    |
| 18           | This error occurs when Date format is invalid. Date should be in YYYY-MM-DD format.                                                                                                                                        |
| 101          | This error occurs when when the  account has Insufficient Balance. Recharge your account to fix this  issue.                                                                                                               |
| 102          | This error occurs when API Key is not specified.                                                                                                                                                                           |
| 143          | This error occurs when User not found or Inactive.                                                                                                                                                                         |
| 151          | This error occurs when Job Id and date doesn't match or the Job Id is incorrect.                                                                                                                                           |
| 142          | Unauthorized IP Address. This error appears when the IP of the server which sent the GET request didn't match the whitelisted IP list.                                                                                     |
| 500          | This error occurs usually when the  problem is on our end. Kindly, notify us immediately when you face this  issue.                                                                                                        |

# GET https://pingsms.in API KEY
         -Sign Up in https://pingsms.in
         -Get API Key from Developer API Tab
         
  ![API_KEY](https://github.com/sa1if3/auto-sms-wisher/blob/master/api-key.png)
