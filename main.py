import requests
import json
import win32com.client as wincom
if __name__ == '__main__':
    speak = wincom.Dispatch("SAPI.SpVoice")
city=input("Enter the name of the city\n")
url = f"http://api.weatherapi.com/v1/current.json?key=636081587ea34f91a0c131213232703&q={city}"
r = requests.get(url)
wdic=json.loads(r.text)
print(wdic["current"]["temp_c"],"°C")
w=wdic["current"]["temp_c"]
speak.Speak(f"The current weather in {city} is {w} degrees")