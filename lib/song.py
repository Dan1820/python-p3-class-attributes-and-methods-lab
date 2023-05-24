class Song:

    genres = []
    artists = []
    genre_count = 0

    count = 0

    def __init__(self, name, artist, genre):

        self.add_song_to_count()
        Song.genres.append(genre)
        self.add_to_artist(self)
        Song.artists.append(artist)
        # self.add_song_to_count(self)
        # Song.genres.append(genre)
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artist(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genre_count(cls, genre_count, increment=1):
        cls.genre_count += increment
        return Song.genres.append(genre_count)

    @classmethod
    def add_to_artist_count(cls, artist, increment=1):
        cls.count += increment
        return Song.artists.append(artist)
