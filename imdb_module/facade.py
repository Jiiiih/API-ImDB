from imdb_module.model import VersioningFirstEvent
from imdb_module.model import VersioningSecondEvent
from imdb_module.imdb_request import ImdbRequest


class VersioningEventFacade:

    def get_versioning_title(title) -> [VersioningFirstEvent]:
        # get the title from Imdb
        versioning_titles = []
        movie_titles = ImdbRequest.get_title(title).content
        # get only the "results" part from the json
        movie_titles = movie_titles["results"]

        for movie_title in movie_titles:
            versioning_title = VersioningFirstEvent(
                title=movie_title["title"],
                id=movie_title["id"]
            )
            versioning_titles.append(versioning_title)
        return versioning_titles

    def get_versioning_rating(movie_id) -> [VersioningSecondEvent]:
        versioning_ratings = []
        movie_rating = ImdbRequest.get_ratings(movie_id).content
        # get all the ratings
        versioning_rating = VersioningSecondEvent(
            title=movie_rating["title"],
            imDb=movie_rating["imDb"],
            metacritic=movie_rating["metacritic"],
            filmAffinity=movie_rating["filmAffinity"],
            rottenTomatoes=movie_rating["rottenTomatoes"],
            theMovieDb=movie_rating["theMovieDb"]
        )
        return versioning_rating
