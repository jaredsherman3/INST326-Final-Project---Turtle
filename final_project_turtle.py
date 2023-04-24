""" Song suggestions for a user based on personality """


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
    

def highest_score(dict):
    '''Returns key with the highest value. 
    Could be used to find the highest trait score to return suggested songs? -  Chiamaka'''
    return max(dict, key=dict.get)


class Song():
    def __init__(self, title):
        """ Initalizes a new instance of Song class 
        
        Args: 
            title (str): title of a song
        """
        self.title = title
        
    def playlist (self,songdict):
        """Creates a dictionary of different songs
            Args:
                songdict (dict): derived from JSON file that holds multiple dictionaries 
                with songs that represent different time periods/genres and are
                meant to correspond to the traits in BigFiveTest 
                -- can edit this to fit other persoanlity test if necessary
                 and I'm still working on the JSON file -> Chiamaka
            Returns:
                play (dict): a dictionary of songs with the artist as the key 
                and the song as the value"""
        # Will take the max value of the the highest trait and return a dictionary 
        # (maybe a list?) of songs for the user 
        self.play = {}
        User = BigFiveTest()
        max_score = max(max(User.trait_scores.values()))
        for track in songdict.keys():
            for key in User.trait_scores.keys():
                if max_score == songdict[track]:
                   
                        


def main(user):
    """ Sets up someone to go through the personallity test
    Args:
        user: an instance of the BigFive Test Class for a new user
        
                        
    Side Effects:
        Prints the song instance 
        S: an instance of the song class with the song choice based on the user instance
     
     """ 
   
    a=BigFiveTest(user)
    s=Song(a)
    print(F"Your persontality trait was {a}, The song we recomend for you is {s}!")