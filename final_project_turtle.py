""" Song suggestions for a user based on personality """

traits = {
    "creative": 4,
    "adventurous": 3,
    "outgoing": 2,
    "emotional": 1,
    "organized": -1,
    "serious": -2,
    "introverted": -3,
    "guarded": -4
}

class PersonalityTest():
    """A class representing a personality test.

    Attributes:
        traits (dict): A dictionary of traits and their corresponding scores.
    """
    def __init__(self, traits):
        """Initializes instance of PersonalityTest class"""
        self.traits = traits
        
    def user_score(self):
        """Prompt user to rate themselves on each trait"""
        user_scores = {}
        for trait, score in self.traits.items():
            rating = int(input(f"On a scale of 1 to 5, how {trait} are you? "))
            user_scores[trait] = rating * score
        return user_scores
    
    def personality_type(self, user_scores):
        """Take the users score and return personality type"""
        total_score = sum(user_scores.values())
        if total_score > 10:
            return "openness"
        elif total_score > 0:
            return "creative"
        elif total_score > -10:
            return "reserved"
        else:
            return "guarded"

class Song():
    def __init__(self, title):
        """ Initalizes a new instance of Song class 
        
        Args: 
            title (str): title of a song
        """
        self.title = title
        
def playlist (track, artist):
        """Creates a dictionary of different songs
            Args:
                track (str): song written by an artist
                artist(str): the artist who wrote the song
            Returns:
                play (dict): a dictionary of songs with the song as the key 
                and the artist as the value"""
        i = 0
        play = {}
        while i < 16:
            play[track]= artist
            i+=1


def main(): 
    """ Finds a song based on the users personality 
    
    
    """
