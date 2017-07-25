import wave

class Recorder():

    def __init__(self):
        print "recorder initialized"

    def read_file(self, path):
        f = wave.open(path, "rb")
        params = f.getparams()
        channels, width, framerate, frames = params[:4]
        data = f.readframes(frames)
        f.close()
        return data