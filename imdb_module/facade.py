from imdb_module.model import VersioningFirstEvent
from imdb_module.model import VersioningSecondEvent
from imdb_module.imdb_request import ImdbRequest
import json

class VersioningEventFacade:
    
    def get_versioning_title(title)-> [VersioningFirstEvent]:
        # get the title from Imdb
        versioning_titles = []
        movie_titles = ImdbRequest.get_title(title).content
        # get only the "results" part from the json
        movie_titles = movie_titles["results"]
        # # dowload movie_titles in the local disk
        # movie_titles_json = json.dumps(movie_titles)
        # with open('movie_titles.json', 'w') as outfile:
        #   json.dump(movie_titles_json, outfile)
        # with open('movie_titles.json') as json_file:
        #   movie_titles = json.load(json_file)
      
        # get title, id from movie_titles json

        for movie_title in movie_titles:
            versioning_title = VersioningFirstEvent(
                title=movie_title["title"],
                id=movie_title["id"]
            )
            versioning_titles.append(versioning_title)
        return versioning_titles
    

    def get_versioning_rating(movie_id)->[VersioningSecondEvent]:
        versioning_ratings = []
        movie_rating = ImdbRequest.get_ratings(movie_id).content   
        # get all the ratings 
        versioning_rating = VersioningSecondEvent(
                 title = movie_rating["title"],
                 imDb = movie_rating["imDb"],
                 metacritic = movie_rating["metacritic"],
                 filmAffinity = movie_rating["filmAffinity"],
                 rottenTomatoes = movie_rating["rottenTomatoes"],
                 theMovieDb = movie_rating["theMovieDb"]
            )
        return versioning_rating
