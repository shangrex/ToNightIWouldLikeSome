import googlemaps
from datetime import datetime
import requests
import json
import os
from ipregistry import IpregistryClient
from dotenv import load_dotenv
import time
load_dotenv()

google_key = os.getenv("GOOGLE_KEY", None)
gmaps = googlemaps.Client(key=google_key)

print(os.getcwd())

# g = gmaps.geolocate()
# print(g)

#kaushiang
# client = IpregistryClient("tryout")  
# ipInfo = client.lookup() 
# print(ipInfo)

#kaushiang
# import geocoder
# g = geocoder.ip('me')
# print(g.latlng)

#Taipei
# send_url = "http://api.ipstack.com/check?access_key=b8a2d3fc38425d5649d47be25ca6550f"
# geo_req = requests.get(send_url)
# geo_json = json.loads(geo_req.text)
# latitude = geo_json['latitude']
# longitude = geo_json['longitude']
# city = geo_json['city']
# print(latitude)
# print(longitude)

# Geocoding an address
# x = gmaps.places_autocomplete('701台南市東區大學路1號')
# print(x)
# geocode_result = gmaps.geocode('701台南市東區大學路1號')

# # count = 0
# # for i in geocode_result[0]:
# #     print(count)
# #     print(i)
# #     count += 1

# lat = geocode_result[0]['geometry']['location']['lat']
# lng = geocode_result[0]['geometry']['location']['lng']
# # Look up an address with reverse geocoding
# # reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# # print(reverse_geocode_result)
# # Request directions via public transit
# now = datetime.now()
# # print(now)
# # directions_result = gmaps.directions("Sydney Town Hall",
# #                                      "Parramatta, NSW",
# #                                      mode="transit",
# #                                      departure_time=now)
# # print(directions_result)
# def check_key(key , target):
#     if key in target.keys():
#         return True
#     return False
# target_place_list = []
# target_types = "school"
# target_star = 0
# target_radius = 1
# # while True:
# #     # time.sleep(0.5)
# #     place = gmaps.places_nearby(location=(lat, lng), radius=target_radius, language="zh-TW")
# #     target_place_list.append(place)
# #     if(check_key('next_page_token', place)):
# #         next_token = place['next_page_token']
# #         place = gmaps.places_nearby(location=(lat, lng), radius=target_radius, keyword="restaurant", language="zh-TW")
# #         target_place_list.append(place)
# #     else:
# #         break# print(place)
# if(check_key('next_page_token', place)):
#     next_token = place['next_page_token']
#     place = gmaps.places_nearby(location=(lat, lng), radius=1, keyword="restaurant", language="zh-TW", page_token=next_token)
# # print()
# # print(place)
# # print(place)

# target_list = []
# for j in target_place_list:
#     for i in j['results']:
#         location = ""
#         busy = True
#         name = "Hello"
#         rating = 3
#         num_rating = 0
#         types_list = []
#         price = -1
#         if(check_key('geometry', i)):
#             if(check_key('location', i['geometry'])):
#                 location = i['geometry']['location']
#         if(check_key('opening_hours', i)):
#             if(check_key('open_now', i['opening_hours'])):
#                 busy = i['opening_hours']['open_now']
#         if(check_key('name', i)):
#             name = i['name']
#         if(check_key('rating', i)):
#             rating = i['rating']
#         if(check_key('user_ratings_total', i)):
#             num_rating = i['user_ratings_total']
#         if(check_key('types', i)):
#             types_list = i['types']
#         if(check_key('price_level', i)):
#             price = i['price_level']
#             print("price ", price)
#         #types check
#         if target_types not in types_list and target_types != "":
#             continue
#         #star check
#         if rating < int(target_star):
#             continue
#         print(name)
#         print(rating)

#         target_list.append([location, busy, name, rating, num_rating, types_list, price])
            
# # place = gmaps.places_nearby(location=(22.995, 120.2329), radius=10, language="zh-TW", page_token=)
# # print(place)