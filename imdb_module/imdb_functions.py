# Contain all the funnctions that structure the main functions
# necessary to make the make the program work

from imdb_module.facade import VersioningEventFacade
from imdb_module.model import VersioningFirstEvent
from imdb_module.model import VersioningSecondEvent

# Ask the user for a movie title
def get_user_title():
    movie_title = input("Enter a movie title: ")
    return movie_title

# get movie titles
def get_title_main(movie_title):

    versioning_titles = VersioningEventFacade.get_versioning_title(movie_title)
    for versioning_title in versioning_titles:
        assert isinstance(versioning_title, VersioningFirstEvent)
    return versioning_titles

# get id list
def get_id_list(versioning_titles):
    id_list = []
    for versioning_title in versioning_titles:
        id_list.append(versioning_title.id)
    return id_list

# get all the ratings for each movie id
def get_rating_main(id_list):
    versioning_ratings = []
    for id in id_list:
        versioning_rating = VersioningEventFacade.get_versioning_rating(id)
        versioning_ratings.append(versioning_rating)
    for versioning_rating in versioning_ratings:
        assert isinstance(versioning_rating, VersioningSecondEvent)
    return versioning_ratings

# print the ratings for each movie
def print_rating(versioning_ratings):
    for versioning_rating in versioning_ratings:
        print(f"Title: {versioning_rating.title}")
        print(f"imDb: {versioning_rating.imDb}")
        print(f"metacritic: {versioning_rating.metacritic}")
        print(f"filmAffinity: {versioning_rating.filmAffinity}")
        print(f"rottenTomatoes: {versioning_rating.rottenTomatoes}")
        print(f"theMovieDb: {versioning_rating.theMovieDb}")


def main():
    movie_title = get_user_title()
    versioning_titles = get_title_main(movie_title)
    id_list = get_id_list(versioning_titles)
    versioning_ratings = get_rating_main(id_list)
    print_rating(versioning_ratings)
