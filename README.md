# Line bot之今晚我想來點

## FSM
<img src="https://i.imgur.com/Jd2ByA9.png">

## Usage
	
### help

help can give the introduction

### fsm 

can show the current fsm state

### sen

can show the sentiment calculate result

### 1-8

use feature 

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

		```address/name```

	result:

		target is

		```...```

	input:

		```target number```

	result:

		```target name```


	show the place nearby 
	 
	 specify the tyes, including food , restaurant, political, finance, health and so on

	specify the radius distance 

	specify the star 

	specify the price range
	
	the target range is -1 - 9
5. show sticker

	can input two arguments, package id and sticker id

	can play with the sticker

6. clear text

	can clear the saved text

7. sentiment calculate

	can anaylyze the save text sentiment

8. find place
	input:

		```target name```

	result:

		```search basic information ```

	find place to get address, price, star, website and so on

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

檢查&複製名子
<img src="https://i.imgur.com/37O7eJm.jpg" width=300>

今晚我想來點

<img src="https://i.imgur.com/tzWeUho.jpg" width=300>
<img src="https://i.imgur.com/6W6K4Mg.jpg" width=300>
<img src="https://i.imgur.com/fDV3VPF.jpg" width=300>
