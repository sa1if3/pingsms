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
 There are total 9 elements(known as key:value pairs) allowed in the dictionary. Any additional parameters are ignored.
 1. **key :** 
 2. **job_id :**
 3. **report_date :**
 4. **product :**
 5. **language :**
 6. **sender :**
 7. **mobile :**
 8. **template :**
 9. **message :** 
 ### Methods
 There are 5
 ### Output
