from crypt import methods
from time import time
from flask import Flask, render_template, request



import tweepy
import pandas as pd
import config
import requests
from sqlalchemy import create_engine
import numpy as np
import string
from string import  Template
from flask import Flask, render_template, request

from collections import Counter
from statistics import mode


import os
import nltk
import requests as req
import re
import numpy as np

import pprint
import time

from pyspark.sql import SparkSession
from pysentimiento import create_analyzer

# Import functions
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF, StringIndexer
from pyspark.sql.functions import length


from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vector

from pyspark.ml import Pipeline
from sklearn.model_selection import train_test_split

import pprint
from sklearn.feature_extraction.text import TfidfVectorizer


from sklearn import svm
from sklearn.metrics import classification_report

import json

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

	columns = ['User','User_id', 'Tweet','Sentiment']
	columns_1 = [ 'User_id','Retweet_Count','Location','Verified_Account', 'Geo_enabled','Lang','Post Date']

	#List to store the Data
	data = []
	data_1=[]
	users_id = []
	for tweet in tweets:
		#Buscar solo tweets en español
		if tweet.lang == 'es': 
			#se asigna un sentimiento por defecto 'Mock' para tener datos,  
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
			
			Date = tweet.created_at

			
			data.append([User, User_id, Tweet,Sentiment])
			data_1.append([User_id,Retweet_count,Location,Verified, Geo_enabled,Lang, Date])
	#Crear DF con los datos adquiridos
	df = pd.DataFrame(data, columns=columns)
	df_1= pd.DataFrame(data_1,columns=columns_1)



	#Divid la el texto en la columna de 'Location'
	df_Loc = df_1['Location'].str.split(',', 1,expand=True)
	#Crear nueva columna con los datos separados en coudad y pais
	df_Loc.columns = ['City','State']
	df_clean=df_Loc.drop(columns=['State'])

	#reemplazar las celdas vacias con Nan
	df_join = df_1.join(df_clean)
	df_join.replace("", np.NAN, inplace=True)
	#Eliminar Nan's
	df_join.dropna(subset=['City'], inplace=True)

	#FUNCION PARA OBTENER LATITUD Y LONGITUD DE LAS CIUDADES DE LOS USUARIOS
	#Get Lat & Lon"
	data_lat = []
	data_lon = []

	cities =[]
	countries =[]

	for index, row in df_join.iterrows():
		city = str(row['City'])  
		if city not in cities :    

			Query_url= ('http://api.openweathermap.org/geo/1.0/direct?q='+city+'&limit=1&appid='+open_weather_API)

			try:
				r = requests.get(Query_url)
				data = r.json()[0]
				Lat = str(data['lat'])
				Lon = str(data['lon'])
				Country = str(data['country'])
				data_lat.append(Lat)
				data_lon.append(Lon)
				cities.append(city)
				countries.append(Country)


				print("La latitud de "+city+" es = "+Lat)
				
			except Exception as e :
				data_lat.append(np.NaN)
				data_lon.append(np.NaN)
				countries.append(np.NaN)

				
				print("Error desconociddo, status code =", e)
		else :
				data_lat.append(np.NaN)
				data_lon.append(np.NaN)
				countries.append(Country)


		
	print(data_lat)
	df_join['Lat']=data_lat
	df_join['Lon']=data_lon
	df_join['Country']=countries

	#SI LA CIUDAD NO SE ENCUENTRA, SE PONDRA UN NAN EN LA CELDA


	#ELIMINAR TWEETS SIN CIUDAD
	df_clean = df_join.dropna()
	#df_clean.count()

	#UNIR DATA FRAMES
	df_final = df.set_index('User_id').join(df_clean.set_index('User_id'))
	df_final_2 = df_final.dropna()
	#df_final_2


	tweet_df=df_final_2
	#Fuction to remove links
	def remove_links(tweet):
		'''Takes a string and removes web links from it'''
		tweet = re.sub(r'http\S+', '', tweet) # remove http links
		tweet = re.sub(r'bit.ly/\S+', '', tweet) # rempve bitly links
		tweet = tweet.strip('[link]') # remove [links]
		return tweet
	# Function to find hashtags
	def find_hashtags(tweet):
		return re.findall('(#[A-Za-z]+[A-Za-z0-9-_]+)', tweet) 
	# Function to remove users
	def remove_users(tweet):
		tweet = re.sub('(rt+ )', '', tweet) # remove retweet
		tweet = re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', tweet) # remove tweeted at
		return tweet
	# Master cleaning function
	my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@'
	my_stopwords = nltk.corpus.stopwords.words('spanish')
	#word_rooter = nltk.stem.snowball.SnowballStemmer("spanish", ignore_stopwords=True).stem
	def clean_tweet(tweet, bigrams=False):
		tweet = remove_users(tweet)
		tweet = remove_links(tweet)
		tweet = tweet.lower() # lower case
		tweet = re.sub('['+my_punctuation + ']+', ' ', tweet) # strip punctuation
		tweet = re.sub('\s+', ' ', tweet) #remove double spacing
		tweet = re.sub('([0-9]+)', '', tweet) # remove numbers
		tweet_token_list = [word for word in tweet.split(' ')
								if word not in my_stopwords] # remove stopwords

	#    tweet_token_list = [word_rooter(word) if '#' not in word else word
	#                       for word in tweet_token_list] # apply word rooter
		if bigrams:
			tweet_token_list = tweet_token_list+[tweet_token_list[i]+'_'+tweet_token_list[i+1]
												for i in range(len(tweet_token_list)-1)]
		tweet = ' '.join(tweet_token_list)
		
		return tweet

	# Clean tweet

	tweet_df["clean_Tweet"] = tweet_df.Tweet.apply(clean_tweet)

	# Get hashtags
	tweet_df['hashtags'] = tweet_df.Tweet.apply(find_hashtags)
	hashtags_list_df = tweet_df.loc[
						tweet_df.hashtags.apply(
							lambda hashtags_list: hashtags_list !=[]
						),['hashtags']]
	# create dataframe where each use of hashtag gets its own row
	flat_hashtags_df = pd.DataFrame(
		[hashtag for hashtags_list in hashtags_list_df.hashtags
		for hashtag in hashtags_list],
		columns=['hashtag'])



		# EDA before treatment
	print('shape: ',tweet_df.shape)
	print('null values: ', np.sum(tweet_df.isnull().any(axis=1)))
	#Verified account proportion
	verified_num = sum(1 for tweet in tweet_df.Verified_Account if tweet == True)

	print("Number of verified accounts: ",verified_num)
	verified_prop=verified_num/len(tweet_df)
	# City distribution
	unique_locations=Counter(tweet_df.Location).keys()
	location_values=Counter(tweet_df.Location).values()
	#top 5 RT'd tweets from verified accounts
	#flat_hashtags_df	

		# Import stop words in spanish
	url= 'https://raw.githubusercontent.com/Alir3z4/stop-words/master/spanish.txt'
	res=req.get(url)
	res=res.text
	stop_words_spanish=list(res.split('\n'))
	stop_words_spanish.append("rt")

	#print(stop_words_spanish)

	#Create sentiment analyzer
	start_time=time.time()
	analyzer = create_analyzer(task="sentiment", lang="es")
	sentiment=[]
	response=analyzer.predict(tweet_df.clean_Tweet)
	#print(time.time()-start_time)

	# Create a length column to be used as a future feature
	spark_df=spark.createDataFrame(tweet_df)
	ml_tweet_df = spark_df.withColumn('length', length(spark_df['clean_Tweet']))
	ml_tweet_df.show()

	# Create all the features to the data set
	pos_neg_to_num = StringIndexer(inputCol='Sentiment',outputCol='label')
	tokenizer = Tokenizer(inputCol="clean_Tweet", outputCol="token_text")
	stopremove = StopWordsRemover(inputCol='token_text',outputCol='stop_tokens', stopWords= stop_words_spanish)
	hashingTF = HashingTF(inputCol="stop_tokens", outputCol='hash_token')
	idf = IDF(inputCol='hash_token', outputCol='idf_token')



	# Create feature vectors
	clean_up = VectorAssembler(inputCols=['idf_token', 'length'], outputCol='features')



	# Create and run a data processing Pipeline
	data_prep_pipeline = Pipeline(stages=[pos_neg_to_num, tokenizer, stopremove, hashingTF, idf, clean_up])
	
	# Fit and transform the pipeline
	cleaner = data_prep_pipeline.fit(ml_tweet_df)
	cleaned = cleaner.transform(ml_tweet_df)

	cleaned.sample(0.1).show()

	svm_df=cleaned.select(["clean_Tweet", "label"]).toPandas()

	# Break data down into a training set and a testing set

	svm_training, svm_testing = train_test_split(svm_df, test_size=0.3)


	start_time=time.time()
	# Support Vector Machine

	# Create feature vectors
	vectorizer = TfidfVectorizer(min_df = 5,
								max_df = 0.8,
								sublinear_tf = True,
								use_idf = True)
	train_vectors = vectorizer.fit_transform(svm_training['clean_Tweet'])
	test_vectors = vectorizer.transform(svm_testing['clean_Tweet'])

	classifier_linear = svm.SVC(kernel='linear')
	classifier_linear.fit(train_vectors, svm_training['label'])
	prediction_linear = classifier_linear.predict(test_vectors)
	report = classification_report(svm_testing['label'], prediction_linear, output_dict=True)
	#print('positive: ', report['pos'])
	#print('negative: ', report['neg'])
	pprint.pprint(report)
	print(time.time()-start_time)


	#Use the model
	test_vectors = vectorizer.transform(svm_df['clean_Tweet'])
	prediction_linear = classifier_linear.predict(test_vectors)
	df_final_2=cleaned.toPandas()

	df_grouped=df_final_2.groupby('Country').sum()
	#print(df_grouped)

	#FUNCION PARA OBTENER LAS 50 PALABRAS MAS FRECUENTES DE TODOS LOS TWEETS

	#KEYS=(PALABRA MAS FRECUENTE, NUMERO DE VECES QUE APARECE)
	keys = ('word','size')

	#PASAR LOS TWEETS A UNA LISTA
	Tweets = df_final_2['Tweet'].tolist()

	temp = [wrd for sub in Tweets for wrd in sub.split()]
	words_list=[]
	for words in temp:
		#CONVERTIR A LETRAS MINUSCULAS 
		words = words.lower()
		# SI LA PALARA NO ESTA EN LA LISTA, AGREGALA 
		if words not in stop_words_spanish and len(words)>1:
			for character in string.punctuation:
				words = words.replace(character,"")
			words_list.append(words)

	try:
		res = mode(words_list)
		print("Word with maximum frequency : " + str(res))

		#Get top 10 most common words of a list
		Counters_found = Counter(words_list)
		most_occur = Counters_found.most_common(50)
		print(most_occur)
		print(get_list_of_dict(keys, most_occur))
	except:
		most_occur = words_list
		print('Exception')

		#CREAR DICCIONARIO CON LA LISTA DE PALABRAS 
	d={"data": get_list_of_dict(keys, most_occur)}
	#ABRIR ARCHIVO DE JS COMO PLANTILLA
	file_to_write = open("D3/data1.js", "r")
	src=Template(file_to_write.read())
	#SUSTITUIR CON  DAOS NUEVOS 
	result= src.substitute(d)
	file_to_write.close()

	#ESCRIBIR DATOS NUEVOS EN ARCHIVO JS
	file2= open('/Users/danie/Desktop/BootCAmp_Final_Proyect/static/words_cloud_data.js',"w")
	file2.writelines(result)
	file2.close()


	#OBTENER TOTAL DE RETWEETS
	retweet_count = df_final_2['Tweet'].count()
	total_tweets= df['Tweet'].count()


	total_tweets= df_final_2['Tweet'].count()
	positive_tweets = round((df_final_2['Sentiment'].loc[df_final_2['Sentiment']=='Positive'].count() / total_tweets)*100 , 2)
	Neg_tweets = round((df_final_2['Sentiment'].loc[df_final_2['Sentiment']=='Negative'].count() / total_tweets)*100 ,2)


	#CREAR DICCIONARIO CON LA LISTA DE PALABRAS 
	d={"Positive": positive_tweets,
	"Negative": Neg_tweets}
	#ABRIR ARCHIVO DE JS COMO PLANTILLA
	file_to_write = open("/Users/danie/Desktop/BootCAmp_Final_Proyect/static/data/tweets_temp.csv", "r")
	src=Template(file_to_write.read())
	#SUSTITUIR CON  DAOS NUEVOS 
	result= src.substitute(d)
	file_to_write.close()

	#ESCRIBIR DATOS NUEVOS EN ARCHIVO JS
	file2= open('/Users/danie/Desktop/BootCAmp_Final_Proyect/static/data/tweets.csv',"w")
	file2.writelines(result)
	file2.close()


	# Clean the data, only choose the colums we need
	cols = ['Sentiment', 'Lat', 'Lon', 'Retweet_Count', 'Country', 'Verified_Account','City']
	df = df_final_2[cols]
	# convert lat-long to floats and change address from ALL CAPS to regular capitalization
	df['Lat'] = df['Lat'].astype(float)
	df['Lon'] = df['Lon'].astype(float)
	df.head(10)
	#df


	df['color'] = np.where(df['Sentiment']== 'Negative', "Red", "Blue")
	df.head()


	# Create te formula for GeoJson. 
	def df_to_geojson(df, properties, lat='Lat', lon='Lon'):
	# create a new python dict to contain our geojson data, using geojson format
		geojson = {'type':'FeatureCollection', 'features':[]}

	# loop through each row in the dataframe and convert each row to geojson format
		for _, row in df.iterrows():
			# create a feature template to fill in
			feature = {'type':'Feature',
					'properties':{},
					'geometry':{'type':'Point',
								'coordinates':[]}}

			# fill in the coordinates
			feature['geometry']['coordinates'] = [row[lon],row[lat]]

			# for each column, get the value and add it as a new feature property
			for prop in properties:
				feature['properties'][prop] = row[prop]
			
			# add this feature (aka, converted dataframe row) to the list of features inside our dict
			geojson['features'].append(feature)
		# print(geojson)
		return geojson
	geojson = df_to_geojson(df, cols)		
	with open("/Users/danie/Desktop/BootCAmp_Final_Proyect/static/resources/cities2.json", "w") as outfile: 
		json.dump(geojson, outfile)




	df_verificadas_sort=df_final_2.sort_values(by='Retweet_Count',ascending=False).head(5)
	df_retweets_user=df_verificadas_sort[['User','Tweet','Retweet_Count','Sentiment','Country']]
	s=df_retweets_user['Tweet']
	u=df_retweets_user['Retweet_Count']

	Tweet1=str("'"+s.iloc[0]+"'")
	Tweet2=str("'"+s.iloc[1]+"'")
	Tweet3=str("'"+s.iloc[2]+"'")
	Tweet4=str("'"+s.iloc[4]+"'")
	Tweet5=str("'"+s.iloc[4]+"'")

	u=df_retweets_user['User']
	User1=str("'"+u.iloc[0]+"'")
	User2=str("'"+u.iloc[1]+"'")
	User3=str("'"+u.iloc[2]+"'")
	User4=str("'"+u.iloc[4]+"'")
	User5=str("'"+u.iloc[4]+"'")


	RTweet1=str(s.iloc[0])
	RTweet2=str(s.iloc[1])
	RTweet3=str(s.iloc[2])
	RTweet4=str(s.iloc[4])
	RTweet5=str(s.iloc[4])


	#CREAR DICCIONARIO CON LA LISTA DE PALABRAS 

	d={"user1": User1,
		"user2": User2,
		"user3": User3,
		"user4": User4,
		"user5": User5,
		"Tweet1": Tweet1,
		"Tweet2": Tweet2,
		"Tweet3": Tweet3,
		"Tweet4": Tweet4,
		"Tweet5": Tweet5}
		
	#ABRIR ARCHIVO DE JS COMO PLANTILLA
	file_to_write = open("/Users/danie/Desktop/BootCAmp_Final_Proyect/static/myDiv_copy.js", "r")
	src=Template(file_to_write.read())
	#SUSTITUIR CON  DAOS NUEVOS
	result= src.substitute(d)
	file_to_write.close()
	#ESCRIBIR DATOS NUEVOS EN ARCHIVO JS
	file2= open("/Users/danie/Desktop/BootCAmp_Final_Proyect/static/test.js","w")
	file2.writelines(result)
	file2.close()


	return render_template('interfaz.html', d=keyword, RT_count=retweet_count, Total_tw=total_tweets, pos_tw=positive_tweets, neg_tw=Neg_tweets )



if __name__ == '__main__':
	fulltime=time.time()
	#!pip install pysentimiento
	nltk.download('stopwords')

	spark = SparkSession.builder.appName("Tokens").getOrCreate()

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



engine = create_engine('postgresql://postgres:postgres@tw-database.cusa4qve384u.us-east-1.rds.amazonaws.com:5432/postgres')	


def get_list_of_dict(keys, list_of_tuples):
	"""
	This function will accept keys and list_of_tuples as args and return list of dicts
	"""
	list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
	return list_of_dict

app.run(debug=True)