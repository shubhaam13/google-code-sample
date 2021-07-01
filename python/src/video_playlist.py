"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    def __init__(self, name: str, videos, original_name):
        self._name = name
        self._videos = videos
        self._original_name = original_name

    @property
    def get_name(self):
        """The name of the playlist"""
        return self._name
    
    @property
    def get_videos(self):
        """Videos in the playlist"""
        return self._videos
    
    @property
    def get_original_name(self):
        """Original name"""
        return self._original_name
