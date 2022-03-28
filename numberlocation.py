import phonenumbers, folium

from yournumber import number

from phonenumbers import geocoder, carrier

sumNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(sumNumber, "en")

key = "3374e638cf824c33a4891c783a234ff7"

print(yourLocation)

## get service provider

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))


from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)
result = geocoder.geocode(query)
##print(result)

lat = result[0]['geometry']['lat']
lng = result[1]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

## save map to html file

myMap.save("myLocation.html")

