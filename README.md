# Line bot之今晚我想來點
The Tool use google API(feature 4) to help you find place, user can specify the place type, star, price, distance to get a list.And more detailed is in the feature 8. And also the tool can write, save and clear the text, and do sentimental analysis.

## FSM
<img src="https://i.imgur.com/Jd2ByA9.png">

## Usage
	
### help

Give the instruction

### fsm 

Show the current fsm state

### sen

Show the sentiment calculate result

### 1-8

Use feature 

## Feature
1. save text
	
	input text and save


	input:

		1

	reply:

		"Trigger save text"

	input:

		"saved text"


2. load text 
	
	show the saved text
3. show fsm picture
	
	show initial state picture
4. find place nearby

	
	input:

		address/name

	result:

		target is

		10 place nearby sorted by prominence

	input:

		target number 0-10

	result:

		target name


	show the place nearby 
	 
	 specify the tyes, including food , restaurant, political, finance, health and so on

	specify the radius distance 

	specify the star 

	specify the price range
	
	the target range is -1 - 9

5. show sticker

	Input two arguments, package id and sticker id

	Play with the sticker

6. clear text

	Clear the saved text

7. sentiment calculate

	Anaylyze the save text sentiment

8. find place
	input:

		target name

	result:

		search basic information

	Find place to get address, price, star, website and so on

## How to setup
1. pipenv install 
2. [set up pygraphviz](https://www.jianshu.com/p/a3da7ecc5303)
3. heroku login
4. heroku buildpack(Aptfile)
	```
	$ heroku buildpacks:set heroku/python
	$ heroku buildpacks:add --index 1 heroku-community/apt
	```

5. set environment variable
	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
	heroku config:set PORT=your_port
	heroku config:set FSM_GRAPH_URL=your_initial_state_fsm_picture_url
	heroku config:set GOOGLE_KEY=your_google_map_api_key
	heroku config:set DOMAIN_URL=your_domain_url
	```
6. git 
	heroku git:remote -a {HEROKU_APP_NAME}
	git add .
	git commit -m "Add code"
	git push heroku master


## Example

今晚我想來點附近

<img src="https://i.imgur.com/eooEM55.jpg" width=300>
<img src="https://i.imgur.com/hQF2d3G.jpg" width=300>
<img src="https://i.imgur.com/cgN0hdj.jpg" width=300>
<img src="https://i.imgur.com/NMPIREU.jpg" width=300>

檢查&複製名子

<img src="https://i.imgur.com/37O7eJm.jpg" width=300>

今晚我想來點

<img src="https://i.imgur.com/tzWeUho.jpg" width=300>
<img src="https://i.imgur.com/6W6K4Mg.jpg" width=300>
<img src="https://i.imgur.com/fDV3VPF.jpg" width=300>
