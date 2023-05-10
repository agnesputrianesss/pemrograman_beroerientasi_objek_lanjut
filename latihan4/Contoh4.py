class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print("Title", song.title)

class MediaPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        print("Play Music")

song1 = Song("Sial", "Mahalini Raharja")
song2 = Song("Diamond", "Rihana")
playlist = Playlist()
media_player = MediaPlayer(playlist)
print("="*40)
playlist.add_song(song1)
playlist.add_song(song2)
media_player.playlist.songs
