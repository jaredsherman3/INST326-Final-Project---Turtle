import argparse 
import sys
import json
import matplotlib.pyplot as plt
import random
""" Song suggestions for a user based on personality """


class BigFiveTest:
    """A class representing a personality test based on the Big Five personality 
        traits.
    
    Attributes:
        questions (str): questions for the persoanlity test
        trait_scores (int): tracks score for each trait based on response
    """
    def __init__(self, questions_file):
        """Initializes instance of the BigFiveTest class.

        Args:
            questions_file (str): path to the CSV file containing the test questions
        """
        self.questions = self.load_questions(questions_file)
        self.trait_scores = {
            "Extraversion": 0,
            "Agreeableness": 0,
            "Conscientiousness": 0,
            "Neuroticism": 0,
            "Openness": 0
        }

    def load_questions(self, questions_file):
        """Loads the questions from a CSV file and returns them as a list of tuples.

        Args:
            questions_file (str): path to the CSV file containing the test questions

        Returns:
            questions (list): a list of tuples, where each tuple contains a 
                trait and a question string
        """
        questions = []
        with open(questions_file, "r") as file:
            lines = file.readlines()[1:]  # Skip the header row
            for line in lines:
                trait, question = line.strip().split(",", 1)
                questions.append((trait, question))
        return questions
    
    def ask_question(self, question):
        """Asks the user a question and returns their answer as an integer.

        Args:
            question (str): the question to ask the user

        Returns:
            answer (int): the user's answer, as an integer between 1 and 5
        """
        valid_answers = frozenset(["1", "2", "3", "4", "5"])
        while True:
            answer = input(question + " (1=Strongly Disagree, 2=Disagree, 3=Neutral, 4=Agree, 5=Strongly Agree) ")
            if answer in valid_answers:
                return int(answer)
            print("Invalid answer. Please enter a number between 1 and 5.")

    def take_test(self):
        """Asks the user all the questions in the test and returns their trait 
            scores.

        Returns:
            trait_scores (dict): a dictionary mapping trait names to scores 
        """
        for question in self.questions:
            trait = question[0]
            question_text = question[1]
            answer = self.ask_question(question_text)
            self.trait_scores[trait] += answer
        return self.trait_scores
    
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
        
    def score_analysis(self, score_analysis_file):
        """Analyzes the user's trait and scores with explanations
        
        Args:
            score_analysis_file (str): path to the JSON file containing the 
                trait explanations

        Returns:
            results (list): a list of strings, where each string is an 
                explanation for one of the user's traits
        """
        with open(score_analysis_file, "r") as f:
            explanations = json.load(f)
            results = [
                explanations[trait]["Low"] if score < 4 else
                explanations[trait]["Medium"] if score >= 4 and score < 7 else
                explanations[trait]["High"]
                for trait, score in self.trait_scores.items()
                ]
            return results

class Song:
    """A class representing a song recommendation system based on the user's 
        personality traits.

    Attributes:
        trait_scores (dict): the user's trait scores, as a dictionary mapping 
            trait names to scores
        songfile (str): path to the JSON file containing the song recommendations
    """
    def __init__(self, trait_scores, songfile):
        """Initializes new instances of Song class - Chiamaka

        Args: 
            trait_scores (dict): the scores that correspond to the traits in the 
                BigFiveTest
            songfile (str): the path to the JSON file that holds the song 
                recommendations
        """
        self.trait_scores = trait_scores
        self.music = self.load_music(songfile)

    def load_music(self, songfile):
        """Loads the song recommendations from a JSON file.

        Args:
            songfile (str): path to the JSON file containing the song recommendations

        Returns:
            songs (dict): a dictionary mapping trait names to lists of r
                ecommended songs
        """
        with open(songfile, 'r') as f:
            songs = json.load(f)
        return songs

        
    def song_playlist (self,trait_scores, num_songs=3):
        """Creates a playlist of songs based on the user's personality traits.

        Args:
            trait_scores (dict): the user's trait scores, as a dictionary mapping 
                trait names to scores
            num_songs (int): the number of songs to include in the playlist for 
                each trait (default is 3)

        Returns:
            play (list): a list of recommended songs
        """
        self.play = []
        for trait, score in trait_scores.items():
            if trait in self.music.keys():
                if score <= 4:
                    for i in range(num_songs):
                        song = random.choice(self.music[trait]['Low'])
                        while song in self.play:
                            song = random.choice(self.music[trait]['Low'])
                        self.play.append(song)

                elif score >= 4 and score <= 7:
                    for i in range(num_songs):
                        song = random.choice(self.music[trait]['Medium'])
                        while song in self.play:
                            song = random.choice(self.music[trait]['Medium'])
                        self.play.append(song)

                else:
                    for i in range(num_songs):
                        song = random.choice(self.music[trait]['High'])
                        while song in self.play:
                            song = random.choice(self.music[trait]['High'])
                        self.play.append(song)
        
        random.shuffle(self.play)
        return self.play
    
    def highest_score(self,trait_scores):
        """Returns the name of the trait with the highest score.

        Args:
            trait_scores (dict): the user's trait scores, as a dictionary 
                mapping trait names to scores

        Returns:
            highest_trait (str): the name of the trait with the highest score
        """
        highest_trait = max(trait_scores, key=trait_scores.get)
        return highest_trait
    
    def __str__(self):
        """Returns an informal string representing the Song object."""
        highest_score = self.highest_score(self.trait_scores)
        return f"{highest_score} is one of your strongest traits!"
    
def parse_args(arglist):
    """Parse command line arguments.
    
    Args:
        arglist (list): A list of command line arguments
        
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = argparse.ArgumentParser(description='Big Five Test and Song Recommendation')
    parser.add_argument('questions_file', metavar='QUESTIONS_FILE', type=str,
                        help='path to the questions file')
    parser.add_argument('song_file', metavar='SONG_FILE', type=str,
                        help='path to the song recommendations file')
    parser.add_argument('score_analysis_file', metavar='ANALYSIS_FILE', type=str,
                        help='path to the score analysis file')
    parser.add_argument('num_songs', type=int, default=3,
                        help='number of songs to include in the playlist (default: 3)')
    return parser.parse_args(arglist)
    
def main(arglist):
    """Sets up someone to go through the personallity test.
    
    Args:
        arglist: A new user going through the test
                              
    Side Effects:
        Prints the songs in a playlist, highest personality trait, and an 
        instance of the song class 
        Creates a new window with a graph displaying users results  
        Song: a Song in the recomended playlist 
        highest_trait: Someones most aligned personality trait 
     """ 
    args = parse_args(arglist)

    test = BigFiveTest(args.questions_file)
    test.take_test()
    
    song_obj = Song(test.trait_scores, args.song_file)
    playlist = song_obj.song_playlist(test.trait_scores, args.num_songs)

    print('\n')
    print(f"{song_obj} Enjoy a curated playlist made just for you!")
    print('\n')

    print("Here's your playlist:")
    for song in playlist:
        print(song)
    
    print('\n')
    print("Here is a more detailed explanation of your five traits:")
    result = test.score_analysis(args.score_analysis_file)
    for sentence in result:
        print(sentence)

    test.visualization()

if __name__ == '__main__':
    main(sys.argv[1:])
   
    

