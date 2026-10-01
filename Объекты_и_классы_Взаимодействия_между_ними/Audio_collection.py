# Creating the Track class
class Track :
    def __init__(self, track_title, duration_in_minutes):
        self.track_title = track_title
        self.duration_in_minutes = duration_in_minutes

    def show(self):
        print(f"<{self.track_title}-{self.duration_in_minutes}>")

track1 = Track("Song1", 5)
track2 = Track("Song2", 3)
track3 = Track("Song3", 4)

# Created three tracks for album 2

track4 = Track("Song4", 2)
track5 = Track("Song5", 6)
track6 = Track("Song6", 7)


# Creating the Album class
class Album :
    def __init__(self, album_title, group, tracklist):
        self.album_title = album_title
        self.group = group
        self.tracklist = tracklist

    def get_tracks(self):
        for track in self.tracklist :
            track.show()


    def add_track(self, track) :
        self.tracklist.append(track)

    def get_duration(self):

        total_time = 0
        for track in self.tracklist :
            total_time += track.duration_in_minutes

        print(total_time)


# Creating Album 1 and Album 2

album1 = Album("Album1", "Group1", [track1, track2])
album2 = Album("Album2", "Group1", [track4, track5, track6])

#  Adding a new track to Album 1
album1.add_track(track3)

# Displaying the duration of both albums
album1.get_duration()
album2.get_duration()

# Displaying the tracks of both albums
album1.get_tracks()
album2.get_tracks()





