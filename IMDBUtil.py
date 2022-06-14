from imdb import Cinemagoer

class IMDBUtil:
    def __init__(self):
        self.cinemagoer = Cinemagoer()
        movies = self.cinemagoer.search_movie_advanced('Doctor Who')
        movie_id = movies[0].getID()
        self.dw = self.cinemagoer.get_movie(movie_id)

    def get_actor(self, actor_name):
        actor = self.cinemagoer.search_person(actor_name)[0]
        cast = self.dw['cast']
        if actor in cast:
            person = self.cinemagoer.get_person(actor.getID())
            keys = person.keys()
            values = person.values()
            result = {}

            non_wanted_result_keys = ['filmography', 'imdbID', 'imdbIndex', 'trade mark', 'trivia',
                                      'birth notes', 'canonical name', 'long imdb name', 'long imdb canonical name',
                                      'death notes', 'salary history', 'quotes']

            for i, key in enumerate(keys):
                if key not in non_wanted_result_keys:
                    result[key] = values[i]

            return result
        return f'Could not find actor "{actor_name}"'

    def get_cast(self):
        return self.dw['cast']

    def get_rating(self):
        return str(self.dw['rating'])

    def get_cover_url(self):
        return str(self.dw['full-size cover url'])
