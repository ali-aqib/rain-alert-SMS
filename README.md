# This is an API based SMS rain alert program
# This project is created using Python 3.12 and Pycharm IDE

**Steps to run the project**
1. Install python 3.12
2. Install module requests and twilio.rest

# Usage Guide
- Go-to twilio.com and signup for free account and get the twilio number, account sid and auth token from the console
- Go-to openweathermap.org  and signup for free account and create an API key (can take few minutes to activate the key).
- Make sure you have verified the e-mail
- Insert the above credentials at line 5, 6, 9 of main.py as a string.
- Insert the twilio contact number and receiver's contact number at line 36, 37 of main.py as a string.
- Enter your co-ordinates at line 14, 15.
- Upon running the main.py, openweathermap.org API fetches the weather forecast from 9AM to 6PM
- If there are chances of rain then you will receive the SMS on your mobile through twilio.
- For testing enter the co-ordinates of the location where it is raining currently. To check the current raining locations got to ventusky.com and click on precipitation.

### Created by AQIB ALI
