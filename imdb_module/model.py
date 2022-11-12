# VersioningEvent.py

# first event is the title
class VersioningFirstEvent:

    def __init__(self, title, id):
        self.title = title
        self.id = id

# second event is the ratings
class VersioningSecondEvent:

    def __init__(self, imDb, metacritic, filmAffinity, rottenTomatoes, theMovieDb, title):
        self.title = title
        self.imDb = imDb
        self.metacritic = metacritic
        self.filmAffinity = filmAffinity
        self.rottenTomatoes = rottenTomatoes
        self.theMovieDb = theMovieDb
