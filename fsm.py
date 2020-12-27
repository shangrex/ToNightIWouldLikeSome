from transitions.extensions import GraphMachine
from config import set_machine
from utils import send_text_message, send_sticker
from utils import send_fsm_graph
from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import os
import googlemaps
import requests
import json
import re
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
    def is_going_to_find_place_nearby(self, event):
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

    def is_going_to_sentiment(self, event):
        text  = event.message.text
        return text.lower() == "7"

    def is_going_to_find_place(self, event):
        text = event.message.text 
        return text.lower() == "8"

    def is_going_to_initial_from_save_text(self, event):
        print("Going to initial")
        file = open("text.txt", "a")
        file.write(event.message.text+'\n')
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

    def is_going_to_initial_from_find_place(self, event):
        
        input_query = event.message.text 
        reply_token = event.reply_token  
        text = "taget is\n"
        try:
            candidates = gmaps.find_place(input_type="textquery",input=input_query)
            y = candidates['candidates'][0]['place_id']
            place = gmaps.place(y)
            name = ""
            types = ""
            address = ""
            phone_number = ""
            is_open = False
            price = -1
            rating = -1
            num_rating = 0
            website = ""
            for i in place['result']:
                feature = place['result'][i]
                if i == "name":
                    name = feature
                if i == "types":
                    types = feature
                if i == "formatted_address":
                    address = feature
                if i == "formatted_phone_number":
                    phone_number = feature
                if i == "opening_hours":
                    is_open = feature['open_now']
                if i == "price_level":
                    price = feature
                if i == "rating":
                    rating = feature
                if i == "user_ratings_total":
                    num_rating = feature
                if i == "website":
                    website = feature
        except Exception:
            pass

        text += "Name: " + name + '\n'
        text += "Is open: " + str(is_open) + '\n'
        text += "Rating: " + str(rating) + '\n'
        text += "Num rating: " + str(num_rating) + '\n'
        t = ""
        for k in types:
            t += k + " "
        text += "Types: " + t + '\n'
        text += "Price level: " + str(price) + '\n'
        text += "Phone Number: " + phone_number + '\n'
        text += "Website: " + website + '\n'
        text += "Address: \n" + address
        text += '\n'
        send_text_message(reply_token, text)

        return True

    def is_going_to_initial_from_select_place(self, event):
        select_num = event.message.text
        reply_token = event.reply_token
        result = re.match("^-?[0-9]*$", select_num)
        if result == None:
            send_text_message(reply_token, "Please input Number")
            return False
        if select_num == "-1":
            return True
        if(int(select_num) > 10 or int(select_num) < 0):
            send_text_message(reply_token, "Please input right range")
            return False

        send_text_message(reply_token, self.target_name[int(select_num)])

        
        return False

    def is_going_to_select_place(self, event):
        print("Going to initial")
        input_query = event.message.text 
        reply_token = event.reply_token
        target_place = "701台南市東區莊敬路136巷12號"
        input_query = input_query.split(' ')
        target_place = ""
        target_types = ""
        target_radius = 100
        target_star = -1
        target_price = 0
        print(input_query)
        if(len(input_query) > 0 and input_query[0] != ' '):
            target_place = input_query[0]
        if(len(input_query) > 1 and input_query[1] != ' '):
            target_types = input_query[1]
        if(len(input_query) > 2 and input_query[2] != ' '):
            target_radius = input_query[2]
        if(len(input_query) > 3 and input_query[3] != ' '):
            target_star = input_query[3]
        if(len(input_query) > 4 and input_query[3] != ' '):
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
            self.target_name = []
            for i in target_list:
                # text += "location " + str(i[0]['lat']) + " " + str(i[0]['lng']) + '\n' 
                text += "target number"+ str(count) + '\n'
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
                self.target_name.append(i[2])
                count += 1
                if(count > 10):
                    break

        print(text)
        send_text_message(reply_token, text+"please select target number to check name or input -1 to quit")
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
        file.close()
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


    def on_enter_find_place_nearby(self, event):
        print("I'm entering find_place_nearby")
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入地點以及最低星數(0~5), \n ex: \n 701台南市東區莊敬路136巷12號(default place) \"\"(default types) 1(default radius meters) -1(default star) 0(default max price)")


    # def on_exit_dinner(self):
    #     print("Leaving dinner")

    def on_enter_sticker(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入 package id 和 sticker id \n  ex. \n1 100")

    def on_enter_clear_text(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger clear text")
        file = open("text.txt", "w")
        file.close()
        self.go_back()


    def on_enter_sentiment(self, event):
        send_text_message(event.reply_token, "calculate sentiment")
        file = open("text.txt", "r")
        text = file.read()
        s = SnowNLP(text)
        sentiment_list = []
        for sentence in s.sentences:
            s = SnowNLP(sentence)
            print(sentence)
            sentiment_list.append(s.sentiments)
        try:
            plt.plot(range(len(sentiment_list)), sentiment_list)
            plt.savefig("sentiment.png")
            plt.close()
        except Exception:
            self.go_back()
        file.close()
        self.go_back()