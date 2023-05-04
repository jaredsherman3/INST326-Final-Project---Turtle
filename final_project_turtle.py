from argparse import ArgumentParser
import sys
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
    class BigFiveTest:
        def __init__(self, questions_file):
            self.questions = self.load_questions(questions_file)
            self.trait_scores = {
                "Extraversion": 0,
                "Agreeableness": 0,
                "Conscientiousness": 0,
                "Neuroticism": 0,
                "Openness": 0
            }

        def load_questions(self, questions_file):
            questions = []
            with open(questions_file, "r") as file:
                lines = file.readlines()[1:]  # Skip the header row
                for line in lines:
                    trait, question = line.strip().split(",", 1)
                    questions.append((trait, question))
            return questions
        
        def ask_question(self, question):
            valid_answers = frozenset(["1", "2", "3", "4", "5"])
            while True:
                answer = input(question + " (1=Strongly Disagree, 2=Disagree, 3=Neutral, 4=Agree, 5=Strongly Agree) ")
                if answer in valid_answers:
                    return int(answer)
                print("Invalid answer. Please enter a number between 1 and 5.")

        def take_test(self):
            for question in self.questions:
                trait = question[0]
                question_text = question[1]
                answer = self.ask_question(question_text)
                self.trait_scores[trait] += answer
        

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


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory arguments:
        - user: Name of the person taking the test 
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument('user',type=str, help="The name of the User taking the test")
    return parser.parse_args(arglist)

# Need to figure out which one to use with the parse args

if __name__== "__main__":
    args = parse_args(sys.argv[1:])
    main(args.user)



if __name__ == "__main__":
    user = input('What is your name')
    main(user)