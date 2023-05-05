from argparse import ArgumentParser
import sys
import json
import matplotlib.pyplot as plt
import random
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
    
    def visualization(self):
        """Data visualization method to show a bar chart with the users 
        trait on the x-axis and the users score on the y-axis"""
        trait_names = list(self.trait_scores.keys())
        trait_scores = list(self.trait_scores.values())

        plt.bar(trait_names, trait_scores)

        plt.title('Big Five Personality Traits')
        plt.xlabel('Traits')
        plt.ylabel('Scores')

        plt.show()
        
    def score_analysis(self):
        """Analyzes the user's trait and scores with explanations
        
        
        """
        with open("score_analysis.json", "r") as f:
        explinations = json.load(f)
        results = []
        for trait, score in self.trait_scores.items():
            print(f"Trait: {trait}")
            print(f"Score: {score}")
            if trait == "Extraversion":
                if score < 4:
                    results.append(explinations[trait]["Low"])
                elif score >= 4 and score < 7:
                    results.append(explinations[trait]["Medium"])
                else:
                    results.append(explinations[trait]["High"])
            elif trait == "Agreeableness":
                if score < 4:
                    results.append(explinations[trait]["Low"])
                elif score >= 4 and score < 7:
                    results.append(explinations[trait]["Medium"])
                else:
                    results.append(explinations[trait]["High"])
            elif trait == "Conscientiousness":
                if score < 4:
                    results.append(explinations[trait]["Low"])
                elif score >= 4 and score < 7:
                    results.append(explinations[trait]["Medium"])
                else:
                    results.append(explinations[trait]["High"])
            elif trait == "Neuroticism":
                if score < 4:
                    results.append(explinations[trait]["Low"])
                elif score >= 4 and score < 7:
                    results.append(explinations[trait]["Medium"])
                else:
                    results.append(explinations[trait]["High"])
            elif trait == "Openness":
                if score < 4:
                    results.append(explinations[trait]["Low"])
                elif score >= 4 and score < 7:
                    results.append(explinations[trait]["Medium"])
                else:
                    results.append(explinations[trait]["High"])
        return results

def highest_score(dict):
    '''Returns key with the highest value. 
    Could be used to find the highest trait score to return suggested songs? -  Chiamaka'''
    return max(dict, key=dict.get)


class Song():
    def __init__(self, title):
        """Initalizes a new instance of Song class 
        
        Args: 
            title (str): title of a song
        """
        self.title = title

    def high_trait_song(self,songdict):
        ''' should give the User a specific song reccomendation best on highest trait
        
        Args: 
        songdict (dict): derived from a JSON file that holds 5 dictioanries
        with three keys 'Low, 'Medium', 'High' and each key has a value that is a list of 
        different songs.Each dictionarybkey is meant to correspond to the traits in BigFiveTest - Chiamaka 
        
        Returns:
        Reccomended song to user based on highest trait'''
        highest = highest_score(self.trait_scores)
        for key in songdict.keys():
            if highest == key:
                self.title = random.choice(songdict[key]['High'])

        return f'A song that best describes you is: {self.title}' 
    #Line above can be removed---> function can be used in main function
        
    def playlist (self,songdict,num_songs=3):
        """Creates a dictionary of different songs
            Args:
                songdict (dict): derived from a JSON file that holds 5 dictioanries
                with three keys 'Low, 'Medium', 'High' and each key has a value that is a list of 
                different songs.Each dictionarybkey is meant to correspond to the traits in BigFiveTest - Chiamaka
            Returns:
                play (list): A list of songs with the name and artist in the format ['song' by Artist Name]"""
        # Will take the max value of the the highest trait and return a list of songs for the user 
        self.play = []
        User = BigFiveTest()
        for trait, score in User.trait_scores.items():
            if  2  >= score  <= 4:
                if trait in songdict.keys():
                    for i in range (num_songs):
                        self.play.append(random.choice(songdict[trait]['Low']))

            elif  5 >= score  <= 7:
                if trait in songdict.keys():
                    for i in range (num_songs):
                        self.play.append(random.choice(songdict[trait]['Medium']))

            elif  8  >= score  <= 10:
                if trait in songdict.keys():
                    for i in range (num_songs):
                        self.play.append(random.choice(songdict[trait]['High']))
        return self.play
        
    def __repr__(self):
        """Prints a song recommendation in a readable format
        
        Returns:
            str: A string that contains the recommended song to the user
        """
        return f'A song that best describes you is: {self.title}'

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