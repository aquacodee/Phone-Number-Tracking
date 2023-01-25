#Import the required modules
import phonenumbers
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

####
phonenumber = input("Enter phone number with country code: ")
number = phonenumbers.parse(phonenumber)

#location of the number
location = geocoder.description_for_number(number, 'en')
print(location)
#checking  for the servie provider
service_provider = carrier.name_for_number(number, 'en')
print(service_provider)
#API Key
key = "7930290e770645f592b2d4171ab0c906"
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat)
print(lng)
#Using folium to create a map
myMap = folium.Map(location = [lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup = location).add_to(myMap)
myMap.save('number.html')