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
        
        #OPTION 2 FOR PERSONALITY TEST BASED ON THE BIG FIVE
class BigFiveTest:
    """ This test is formatted a bit diff from above. I think it is a bit easier to work
    with but we can discuss details. Personally am a big fan of the big five test. Anyway
    I think it would be good to ask them questions that doesn't expect them to already
    know how well they match with a certain trait by using scenarios - Jess
    
    CLass representing a personality test
    Attributes:
        questions (str): questions for the persoanlity test
        trait_scores (int): tracks score for each trait based on response
    """
    def __init__(self):
        self.questions = [
            "I am someone who is talkative.",  # Extraversion
            "I am someone who tends to find fault with others.",  # Agreeableness (reverse-scored)
            "I am someone who does a thorough job.",  # Conscientiousness
            "I am someone who gets nervous easily.",  # Neuroticism
            "I am someone who has an active imagination.",  # Openness
            "I am someone who is outgoing, sociable.",  # Extraversion
            "I am someone who tends to be disorganized.",  # Conscientiousness (reverse-scored)
            "I am someone who is relaxed, handles stress well.",  # Neuroticism (reverse-scored)
            "I am someone who has few artistic interests.",  # Openness (reverse-scored)
            "I am someone who is empathetic, feels for others."  # Agreeableness
            #Maybe will add more questions
        ]
        
        self.trait_scores = {
            "Extraversion": 0,
            "Agreeableness": 0,
            "Conscientiousness": 0,
            "Neuroticism": 0,
            "Openness": 0
        }
        
        def ask_question(self, question):
            valid_answers = frozenset(["1", "2", "3", "4", "5"])
            while True:
                answer = input(question + " (1=Disagree strongly, 2=Disagree a little, 3=Neutral, 4=Agree a little, 5=Agree strongly) ")
                if answer in valid_answers:
                    return int(answer)
                print("Invalid answer. Please enter a number between 1 and 5.")
                
        def take_test(self):
            """ figuring out a way to calc the scores"""
            for question in self.questions:
                answer = self.ask_question(question)
                if question in frozenset([self.questions[0], self.questions[5]]):
                    self.trait_scores["Extraversion"] += answer
                elif question in frozenset([self.questions[1], self.questions[9]]):
                    self.trait_scores["Agreeableness"] += 6 - answer
                elif question in frozenset([self.questions[2], self.questions[6]]):
                    self.trait_scores["Conscientiousness"] += 6 - answer
                elif question in frozenset([self.questions[3], self.questions[7]]):
                    self.trait_scores["Neuroticism"] += 6 - answer
                elif question in frozenset([self.questions[4], self.questions[8]]):
                    self.trait_scores["Openness"] += 6 - answer
    
        

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
    """ Finds a song based on the users personality. Returns a graph analysis of their 
        personality based on the results. 
    
    
    """
