# Name Data Module

def GetPopularMovies():
	import json 
	import pandas as pd 
	import requests
	from pprint import pprint
	import time

	movie_url = 'https://api.themoviedb.org/3/movie/popular?api_key=6740709218b69a4e877ef5015c2bcd5d&language=en-US&page='

	url = movie_url + '1'
	response = requests.get(url).json()
	pages = response['total_pages']

	results = []
	n = 0
	droppedcount = []

	for p in range(pages):
	    p+=1
	    url = movie_url + str(p)
	    if n == 39:
	        time.sleep(3)
	        n = 0
	    response = requests.get(url).json()
	    try:
	        results.append(response['results'])
	    except KeyError:
	        droppedcount.append(response)

	Movies = []
	for result in results:
	    for movie in result:
	        try:
	            Movies.append(movie)
	        except:
	            pass

	popular_movies_df = pd.DataFrame(Movies)
	return popular_movies_df

# def GetPopularTVShows(apikey):
# 	#

# def GetCharacters(apikey):
# 	#

# def GetBabyNames():
# 	#

