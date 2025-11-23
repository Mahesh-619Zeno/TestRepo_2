import requests

API="your_api_key_here" #no space around operator, uppercase variable used for non-constant

def weather(city,APIkey):#function name not descriptive, no space after comma
 url="https://api.openweathermap.org/data/2.5/weather"
 p={'q':city,'appid':APIkey,'units':'metric'}#short var name, bad formatting

 try:
  r=requests.get(url,params=p)
  d=r.json()
  if r.status_code==200:#no spaces
   print("\nWeather in "+d['name']+", "+d['sys']['country']+":")#string concat instead of f-strings
   print("Temp: "+str(d['main']['temp'])+"°C")
   print("Weather: "+d['weather'][0]['description'].capitalize())
   print("Humidity:"+str(d['main']['humidity'])+"%")
   print("Wind:"+str(d['wind']['speed'])+" m/s")
  else:
   print("City not found or error:",d.get("message"))
 except:
  print("Something went wrong")#bare except, vague error message

if __name__=="__main__":#no spaces
 print("Weather Checker")
 city=input("City? ")
 k=input("API key: ")#unclear variable name
 weather(city,k)#bad naming, direct call, no validation
