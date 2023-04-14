""" Song suggestions for a user based on personality """

class Song():
    def __init__(self, title):
        """ Initalizes a new instance of Song class 
        
        Args: 
            title (str): title of a song
        """
        self.title = title
        
def playlist (track, artist):
        ''' Creates a dictionary of different songs
            Args:
                track (str): song written by an artist
                artist(str): the artist who wrote the song
            Returns:
                play (dict): a dictionary of songs with the song as the key 
                and the artist as the value'''
        i = 0
        play = {}
        while i < 16:
            play[track]= artist
            i+=1

class PersonalityTest():
    def __init__(self, traits):
        self.traits = traits
        
    def user_score(self):
        """Prompt user to rate themselves on each trait"""
        pass
    
    def personality_type(self, score):
        """Take the users score and return personality type"""
        pass  

def main(): 
    """ Finds a song based on the users personality 
    
    
    """
