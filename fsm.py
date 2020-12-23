from transitions.extensions import GraphMachine
from config import set_machine
from utils import send_text_message, send_sticker
from utils import send_fsm_graph
from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
import os
import googlemaps
import requests
import json
import time
load_dotenv()

google_key = os.getenv("GOOGLE_KEY", None)
gmaps = googlemaps.Client(key=google_key)

#global machine
int_machine = set_machine()
machine = GraphMachine(states= int_machine.state(),
                        transitions=int_machine.transition(),
                        initial=int_machine.initial(),
                        auto_transitions=int_machine.auto_transitions(),
                        show_conditions=int_machine.show_conditions(),
                        )

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        # self.machine = GraphMachine(model=self, **machine_configs)
        int_machine = set_machine()
        self.machine = GraphMachine(model = self, states= int_machine.state(),
                        transitions=int_machine.transition(),
                        initial=int_machine.initial(),
                        auto_transitions=int_machine.auto_transitions(),
                        show_conditions=int_machine.show_conditions(),
                        )
    def is_going_to_dinner(self, event):
        text = event.message.text
        return text.lower() == "4"

    def is_going_to_save_text(self, event):
        text = event.message.text
        return text.lower() == "1"

    def is_going_to_load_text(self, event):
        text = event.message.text
        return text.lower() == "2"

    def is_going_to_show_image(self, event):
        text = event.message.text
        return text.lower() == "3"

    def is_going_to_sticker(self, event):
        text = event.message.text 
        return text.lower() == "5"

    def is_going_to_clear_text(self, event):
        text = event.message.text 
        return text.lower() == "6"

    def is_going_to_initial_from_save_text(self, event):
        print("Going to initial")
        file = open("text.txt", "a")
        file.write(event.message.text)
        file.close()
        return True

    def is_going_to_initial_from_sticker(self, event):
        all_stikcer = event.message.text.split(' ')
        print(all_stikcer)
        if len(all_stikcer) > 0:
            package_id = all_stikcer[0]
        if len(all_stikcer) > 1:
            sticker_id = all_stikcer[1]
        try:
            send_sticker(event.reply_token, [package_id, sticker_id])
        except:
            send_text_message(event.reply_token, "no such sticker")
        return True

    def is_going_to_initial_from_dinner(self, event):
        print("Going to initial")
        input_query = event.message.text 
        reply_token = event.reply_token
        target_place = "701台南市東區莊敬路136巷12號"
        input_query = input_query.split(' ')
        target_place = ""
        target_types = ""
        target_radius = 1
        target_star = -1
        target_price = 0
        print(input_query)
        if(len(input_query) > 0 and input_query[0] != ''):
            target_place = input_query[0]
        if(len(input_query) > 1 and input_query[1] != ''):
            target_types = input_query[1]
        if(len(input_query) > 2 and input_query[2] != ''):
            target_radius = input_query[2]
        if(len(input_query) > 3 and input_query[3] != ''):
            target_star = input_query[3]
        if(len(input_query) > 4 and input_query[3] != ''):
            target_price = input_query[4]

        lat = 0
        lng = 0
        
        geocode_result = gmaps.geocode(target_place)
        target_place_list = []
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        count = 0
        while True:
            print("# of page token", count)
            count += 1
            if(count > 5):
                break
            time.sleep(1)
            place = gmaps.places_nearby(location=(lat, lng), radius=target_radius, language="zh-TW")
            target_place_list.append(place)
            if(self.check_key('next_page_token', place)):
                next_token = place['next_page_token']
                place = gmaps.places_nearby(location=(lat, lng), radius=target_radius, keyword="restaurant", language="zh-TW")
                target_place_list.append(place)
            else:
                break
        
        target_list = []
        for j in target_place_list:
            for i in j['results']:
                location = ""
                busy = True
                name = "Hello"
                rating = 3
                num_rating = 0
                types_list = []
                price = -1
                if(self.check_key('geometry', i)):
                    if(self.check_key('location', i['geometry'])):
                        location = i['geometry']['location']
                if(self.check_key('opening_hours', i)):
                    if(self.check_key('open_now', i['opening_hours'])):
                        busy = i['opening_hours']['open_now']
                if(self.check_key('name', i)):
                    name = i['name']
                if(self.check_key('rating', i)):
                    rating = i['rating']
                if(self.check_key('user_ratings_total', i)):
                    num_rating = i['user_ratings_total']
                if(self.check_key('types', i)):
                    types_list = i['types']
                if(self.check_key('price_level', i)):
                    price = i['price_level']
                #types check
                if target_types not in types_list and target_types != "":
                    continue
                #star check
                if rating < int(target_star):
                    continue
                if price > int(target_price):
                    continue
                target_list.append([location, busy, name, rating, num_rating, types_list, price])
            
            text = "target is" + '\n'
            count = 0
            for i in target_list:
                count += 1
                if(count > 10):
                    break
                # text += "location " + str(i[0]['lat']) + " " + str(i[0]['lng']) + '\n' 
                text += "Is open: " + str(i[1]) + '\n'
                text += "Name: " + i[2] + '\n'
                text += "Rating: " + str(i[3]) + '\n'
                text += "Num rating: " + str(i[4]) + '\n'
                t = ""
                for k in i[5]:
                    t += k + " "
                text += "Types: " + t + '\n'
                text += "Price level: " + str(i[6]) + '\n'
                text += '\n'

        print(text)
        send_text_message(reply_token, text)
        return True

    def on_enter_save_text(self, event):
        print("I'm entering save text")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger save text")

    # def on_exit_save_text(self):
    #     print("Leaving save text")

    def on_enter_load_text(self, event):
        print("I'm entering state2")
        file = open("text.txt", "r")
        word = file.read()
        reply_token = event.reply_token
        send_text_message(reply_token, "load text:\n"+word)
        self.go_back()

    def on_exit_load_text(self):
        print("Leaving state2")


    def on_enter_show_image(self, event):
        print("I'm entering show image")

        # machine.get_graph().draw("fsm.png", prog="dot", format="png")
        reply_token = event.reply_token
        send_fsm_graph(reply_token)
        # send_file("fsm.png", mimetype="image/png")
        # send_text_message(reply_token, "Trigger show image")
        self.go_back()

    def on_exit_show_image(self):
        print("Leaving show image")

    def check_key(self, key , target):
        if key in target.keys():
            return True
        return False


    def on_enter_dinner(self, event):
        print("I'm entering dinner")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入地點以及最低星數(0~5), \n ex: \n 701台南市東區莊敬路136巷12號(default place) ""(default types) 1(default radius meters) -1(default star) 0(default max price)")


    # def on_exit_dinner(self):
    #     print("Leaving dinner")

    def on_enter_sticker(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入 package id 和 sticker id \n  ex. \n3 3")

    def on_enter_clear_text(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger clear text")
        file = open("text.txt", "w")
        file.close()
        self.go_back()