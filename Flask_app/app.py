from crypt import methods
from time import time
from flask import Flask, render_template, request
import time
import tweepy
import pandas as pd
import config
import requests

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
	data_from_html = request.form['data']
	data_from_html_len = int(request.form['data_1'])
	print('data len =', data_from_html)
	#Search tweets by keyword
	keyword= data_from_html
	limit=data_from_html_len

	#get tweets
	tweets = tweepy.Cursor(api.search_tweets, q=keyword, count=100,tweet_mode='extended').items(limit)

	#DF Columns
	columns = ['User','User_id', 'Tweet','Sentiment']
	columns_1 = [ 'User_id','Retweet_Count','Location','Verified_Account', 'Geo_enabled','Lang']

	#List to store the Data
	data = []
	data_1=[]
	users_id = []
	for tweet in tweets:

		
		if tweet.user.geo_enabled == True and tweet.lang == 'es':  
			if len(tweet.full_text)<100:
				Sentiment = 'Positive'
			else: 
				Sentiment = 'Negative'
			#Define Variables    
			User= tweet.user.screen_name
			User_id= tweet.user.id
			Tweet = tweet.full_text
			Retweet_count=tweet.retweet_count
			Location=tweet.user.location
			Verified= tweet.user.verified
			Geo_enabled = tweet.user.geo_enabled
			Lang = tweet.lang


			data.append([User, User_id, Tweet,Sentiment])
			data_1.append([User_id,Retweet_count,Location,Verified, Geo_enabled,Lang])

	df = pd.DataFrame(data, columns=columns)
	df_1= pd.DataFrame(data_1,columns=columns_1)

	#Print DF
	print(df.tail())


	return render_template('index-2.html', d='Negative')



if __name__ == '__main__':

	#Import api Keys
	api_key=config.API_KEY
	api_key_secret=config.API_KEY_SECRET
	access_token=config.ACCESS_TOKEN
	access_token_secret=config.ACCESS_TOKEN_SECRET
	open_weather_API= config.OW_API

	#Authentication Instance
	auth= tweepy.OAuth1UserHandler(api_key,api_key_secret)
	auth.set_access_token(access_token,access_token_secret)
	api=tweepy.API(auth)

	app.run(debug=True)