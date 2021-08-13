class isVideoPlaying:
    def __init__(self):
        self.playing_state = False
        self.which_video = None
    def yes(self, video):
        self.playing_state = True
        self.which_video = video
    def no(self):
        self.playing_state = False
        self.which_video = None

