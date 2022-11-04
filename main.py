from imdb_module.facade import VersioningEventFacade
from imdb_module.model import VersioningFirstEvent
from imdb_module.model import VersioningSecondEvent
from dotenv import load_dotenv
import os



# Ask the user for a movie title
movie_title = input("Enter a movie title: ")
versioning_titles = VersioningEventFacade.get_versioning_title(movie_title)

for versioning_title in versioning_titles:
    assert isinstance(versioning_title, VersioningFirstEvent)

# store the different movie id in a list
id_list = []
for versioning_title in versioning_titles:
    id_list.append(versioning_title.id)

versioning_ratings = []

# get the ratings for each movie id
for id in id_list:
 versioning_rating = VersioningEventFacade.get_versioning_rating(id)
 versioning_ratings.append(versioning_rating)

for versioning_rating in versioning_ratings:
    assert isinstance(versioning_rating, VersioningSecondEvent)


# print the ratings for each
for versioning_rating in versioning_ratings:
    print(f"Title: {versioning_rating.title}")
    print(f"imDb: {versioning_rating.imDb}")
    print(f"metacritic: {versioning_rating.metacritic}")
    print(f"filmAffinity: {versioning_rating.filmAffinity}")
    print(f"rottenTomatoes: {versioning_rating.rottenTomatoes}")
    print(f"theMovieDb: {versioning_rating.theMovieDb}")
    
