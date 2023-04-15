import os
import pygame

class MusicPlayer:
    def __init__(self):
        self.tracks = []
        self.current_track = None
        self.paused = False
        self.index = -1

        # initialize Pygame mixer for audio playback
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

    def get_tracks(self):
        # get the list of MP3 files in the music folder
        music_folder = "C:/Users/jalaj/VsCodeLiter/PYs/music_player/music"
        for filename in os.listdir(music_folder):
            if filename.endswith(".mp3"):
                self.tracks.append(filename)

    def play_track(self, index):
        # load and play the selected track
        track = self.tracks[index]
        track_path = os.path.join("C:/Users/jalaj/VsCodeLiter/PYs/music_player/music", track)
        self.current_track = pygame.mixer.Sound(track_path)
        self.current_track.play()

    def pause_track(self):
        # pause or unpause the current track
        if not self.paused:
            pygame.mixer.pause()
            self.paused = True
        else:
            pygame.mixer.unpause()
            self.paused = False

    def stop_track(self):
        # stop the current track
        pygame.mixer.stop()

    def next_track(self):
        # play the next track in the playlist
        self.index = (self.index + 1) % len(self.tracks)
        self.stop_track()
        self.play_track(self.index)

    def prev_track(self):
        # play the previous track in the playlist
        self.index = (self.index - 1) % len(self.tracks)
        self.stop_track()
        self.play_track(self.index)

    def select_track(self):
        # show the available tracks and ask the user to select one
        self.get_tracks()
        for i, track in enumerate(self.tracks):
            print(i, track)
        self.index = int(input("Enter the index of the track you want to play: "))

    def play_music(self):
        # play the selected track and handle user input
        self.select_track()
        self.play_track(self.index)
        while True:
            # display the current track and its playback status
            current_time = pygame.mixer.music.get_pos() / 1000
            duration = self.current_track.get_length()
            print(f"Now playing: {self.tracks[self.index]} [{int(current_time)}s/{int(duration)}s] {'[PAUSED]' if self.paused else ''}")

            user_input = input("Enter 'p' to pause, 'r' to resume, 's' to stop, 'n' to play next track, 'b' to play previous track, or 'i' for song info: ")
            if user_input == 'p':
                self.pause_track()
            elif user_input == 'r':
                self.pause_track()
            elif user_input == 's':
                self.stop_track()
                break
            elif user_input == 'n':
                self.next_track()
            elif user_input == 'b':
                self.prev_track()
            elif user_input == 'i':
                print(f"Now playing: {self.tracks[self.index]}")

        self.stop_track()

# create the music player and play music
music_player = MusicPlayer()
music_player.play_music()
