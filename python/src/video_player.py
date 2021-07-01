"""A video player class."""

from .video_library import VideoLibrary
from random import randint
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._active_video = None
        # Might be better as a dict to avoid unexpected values
        self._state = ""
        self._playlists = {}

    @property
    def get_active_video(self):
        """The class instance of the active video if there is one or an empty string if not"""
        return self._active_video

    @property
    def get_state(self):
        """If active video is playing, paused or stopped"""
        return self._state

    # No idea how to make Setters in Python, but I can make them in Java
    # For now, using direct access, despite the danger

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()
        print("Here's a list of all availible videos:")
        for i in range(len(all_videos)):
            print(all_videos[i].title + " (" + all_videos[i].video_id + ") [" + ' '.join(all_videos[i].tags) + "]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        all_videos = self._video_library.get_all_videos()
        if self._active_video == None:
            found_song = False
            for i in range(len(all_videos)):
                if all_videos[i].video_id == video_id:
                    found_song = True
                    self._active_video = all_videos[i]
                    # This would be terribly slow with millions of videos, I would expect to use a hash table or something faster here in real life
            if found_song == True:
                print("Playing video: " + self._active_video.title)
                self._state = "Playing"
            elif found_song == False:
                print("Cannot play video: Video does not exist")
        else:
            # another video is already playing
            old_video = ""
            new_video = ""
            for i in range(len(all_videos)):
                if all_videos[i].video_id == self.active_video.video_id:
                    old_video = all_videos[i].title
                if all_videos[i].video_id == video_id:
                    new_video = all_videos[i].title
            print("Stopping video: " + old_video)
            print("Playing video: " + new_video)
            self._active_video = all_videos[i]
            self._state = "Playing"

    def stop_video(self):
        """Stops the current video."""
        if self.active_video == None:
            print("Cannot stop video: No video is currently playing")
        elif self.state != "Stopped":
            print("Stopping video: " + self._active_video.title)
            self._state = "Stopped"
            self._active_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        all_videos = self._video_library.get_all_videos()
        if len(all_videos) == 0:
            print("No videos availible")
        else:
            random_int = randint(0, len(all_videos) - 1)
            self.play_video(all_videos[random_int].video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self._active_video == None:
            print("Cannot pause video: No video is currently playing")
            print("Video already paused: " + self._active_video.title)
        elif self._state != "Paused":
            print("Pausing video: " + self._active_video.title)
            self._state = "Paused"
        elif self._state == "Paused":
            print("Video already paused: " + self._active_video.title)

    def continue_video(self):
        """Resumes playing the current video."""
        if self._active_video == None:
            print("Cannot continue video: No video is currently playing")
        elif self._state == "Paused":
            print("Continuing video: " + self._active_video.title)
        elif self._state != "Paused":
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        if self._active_video != None:
            print(self._active_video.title + " (" + self._active_video.video_id + ") [" + ' '.join(
                self._active_video.tags) + "] - " + self._state)
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() in self._playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            original_name = playlist_name
            new_playlist = Playlist(playlist_name.lower(), {}, original_name)
            print("Successfully created new playlist: " + original_name)
            self._playlists[playlist_name] = new_playlist

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        all_videos = self._video_library.get_all_videos()
        if playlist_name not in self._playlists:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")

        video_exists = False
        for i in range(len(all_videos)):
            if all_videos[i].video_id == video_id:
                the_video = all_videos[i]
                video_exists = True

        if video_exists:
            # fetch the playlist by name
            the_playlist = self._playlists[playlist_name]
            if video_id in the_playlist._videos:
                print("Cannot add video to " + playlist_name + ": Video already added")
            else:
                the_playlist._videos[video_id] = the_video
                print("Added video to " + playlist_name + ": " + the_video.title)
        else:
            print("Cannot add video to " + playlist_name + ": Video does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        results = list(self._playlists.values())
        names = []
        for i in results:
            names.append(i.get_original_name)
        results = sorted(names)
        print("Showing all playlists")
        for i in results:
            print(i)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name not in self._playlists:
            print("Cannot show playlist " + playlist_name + ": Playlist does not exist")
        else:
            print("Showing playlist: " + playlist_name)
            if not self._playlists[playlist_name]:
                print("No videos here yet")
            else:
                for value in self._playlists[playlist_name].values():
                    print(value.title + " (" + value.video_id + ") [" + ' '.join(value.tags) + "]")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name not in self._playlists:
            print("Cannot remove video from " + playlist_name + ": Playlist does not exist")
        else:
            the_playlist = self._playlists[playlist_name]
            video_exists = False
            for i in range(len(all_videos)):
                if all_videos[i].video_id == video_id:
                    the_video = all_videos[i]
                    video_exists = True

            if not video_exists:
                print("Cannot remove video from " + playlist_name + ": Video does not exist")
            else:
                if video_id in the_playlist:
                    the_video = the_playlist[video_id]
                    del the_playlist[video_id]
                    print("Removed video from " + playlist_name + ": " + the_video.title)
                else:
                    print("Cannot remove video from " + playlist_name + ": Video is not in playlist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name not in self._playlists:
            print("Cannot clear playlist " + playlist_name + ": Playlist does not exist")
        else:
            self._playlists[playlist_name].clear()
            print("Successfully removed all videos from " + playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name not in self._playlists:
            print("Cannot delete playlist " + playlist_name + ": Playlist does not exist")
        else:
            del self._playlists[playlist_name]
            print("Deleted playlist: " + playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        results = []
        for i in all_videos:
            if i.title.lower().find(search_term.lower()) != -1:
                results.append(i)

        results.sort(key=lambda x: x.title)
        if len(results) == 0:
            print("No search results for " + search_term)
        else:
            print("Here are the results for " + search_term)
            for i in range(len(results)):
                print(str(i) + ") " + results[i].title + " (" + results[i].video_id + ") [" + ' '.join(
                    results[i].tags) + "]")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            choice = input()
            if choice.isdigit() and int(choice) < len(results):
                self.play_video(results[int(choice) - 1].video_id)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        results = []
        for i in all_videos:
            for j in i.tags:
                if j.lower() == video_tag.lower() and i not in results:
                    results.append(i)

        results.sort(key=lambda x: x.title)
        if len(results) == 0:
            print("No search results for " + video_tag)
        else:
            print("Here are the results for " + video_tag)
            for i in range(len(results)):
                print(str(i) + ") " + results[i].title + " (" + results[i].video_id + ") [" + ' '.join(
                    results[i].tags) + "]")
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            choice = input()
            if choice.isdigit() and int(choice) < len(results):
                self.play_video(results[int(choice) - 1].video_id)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
