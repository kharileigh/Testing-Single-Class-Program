import math

class DiaryEntry:
    def __init__(self, title, contents):

        # EMPTY -- ERROR
        if title == "" or contents == "":
            raise Exception("Diary entries must have titles and contents")
        
        self.title = title
        self.contents = contents


    def format(self):
        
        return f"{self.title} : {self.contents}"


    def count_words(self):
        
        words = self.format().split()
        return len(words)


    def reading_time(self, wpm):
        
        if wpm == 0:
            raise Exception("Cannot calculate reading time")

        contents_word_count = len(self.contents.split())
        return math.ceil(contents_word_count / wpm)


    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass
