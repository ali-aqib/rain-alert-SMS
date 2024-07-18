import requests
from twilio.rest import Client

# twilio credentials
account_sid = ""  # your twilio account sid
auth_token = ""  # your twilio auth token

# OpenWeatherMap API key
OWM_Api_key = ""  # your open weather map api key

# open weather map API parameters
parameters = {
    "appid": OWM_Api_key,
    "lat": 20.45,
    "lon": 78.35,
    "cnt": 4
}
# getting forecast of the day from API
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

# checking the rain possibility for the day by accessing codes
for hourly_data in data["list"]:
    code = hourly_data["weather"][0]["id"]
    if int(code) < 700:
        will_rain = True

# Sending SMS using twilio
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its going to rain today. Remember to bring an umbrella ☔.",
        from_="",  # twilio mobile number
        to="",  # mobile number with country code to receive rain alert
    )
    print(message.status)
    print(message.sid)
