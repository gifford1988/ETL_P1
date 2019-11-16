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

def GetPopularTVShows():
	import json 
	import pandas as pd 
	import requests
	from pprint import pprint
	import time

	show_url = 'https://api.themoviedb.org/3/tv/popular?api_key=6740709218b69a4e877ef5015c2bcd5d&language=en-US&page='

	url = show_url + '1'
	response = requests.get(url).json()
	pages = response['total_pages']

	results = []
	n = 0
	droppedcount = []

	for p in range(pages):
	    p+=1
	    url = show_url + str(p)
	    if n == 39:
	        time.sleep(3)
	        n = 0
	    response = requests.get(url).json()
	    try:
	        results.append(response['results'])
	    except KeyError:
	        droppedcount.append(response)

	Shows = []
	for result in results:
	    for show in result:
	        try:
	            Shows.append(show)
	        except:
	            pass

	popular_shows_df = pd.DataFrame(Shows)
	return popular_shows_df

def GetCharacters(apikey, movie):
	#
	from bs4 import BeautifulSoup
	import requests

	url = f'http://www.omdbapi.com/?apikey={apikey}&t={movie}'
	response = requests.get(url).json()
	try:
	    tconst = response['imdbID']

	    # Scrape IMDB for characters
	    URL = f'https://www.imdb.com/title/{tconst}/'
	    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

	    response = requests.get(URL, headers=headers)

	    soup = BeautifulSoup(response.content, 'html.parser')
	    table = soup.find_all('td', class_="character")

	    Character_List = []

	    for c in table:
	        try:
	            Character_List.append(c.find('a').contents[0])
	        except:
	            pass

	    #print(Character_List)
	except:
	    Character_List = []

	return Character_List
# def GetBabyNames():
# 	#

