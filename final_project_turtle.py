import argparse 
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
        
    def score_analysis(self):
        """Analyzes the user's trait and scores with explanations
        
        Returns:
            list with a string representing detailed analysis of trait `
        """
        with open("score_analysis.json", "r") as f:
            explinations = json.load(f)
            results = []
            for trait, score in self.trait_scores.items():
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


class Song():
    def __init__(self, trait_scores, songfile):
        """Initializes new instances of Song class - Chiamaka

        Args: 
            trait_scores(dict): the scores that correspond to the traits in the BigFiveTest
            songfile(str): the path to the JSON file that holds the song recommendations
        """
        self.trait_scores = trait_scores
        self.music = self.load_music(songfile)

    def load_music(self, songfile):
        ''' loads the songs.json file  -Chiamaka
        
        ''' 
        with open(songfile, 'r') as f:
            songs = json.load(f)
        return songs

        
    def song_playlist (self,trait_scores, num_songs=3):
        """Creates a dictionary of different songs - Chiamaka


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
        ''' Returns highest trait - Chiamaka'''
        highest_trait = max(trait_scores, key=trait_scores.get)
        return highest_trait
    
    def __str__(self):
        highest_score = self.highest_score(self.trait_scores)
        return highest_score
    

def main(arglist):
    """ Sets up someone to go through the personallity test
    Args:
        Arglist: A new user going through the test
                              
    Side Effects:
        Prints the songs in a playlist, highest personality trait, and an 
        instance of the song class  
        Song: a Song in the recomended playlist 
        highest_trait: Someones most aligned personality trait 
        song_obj= an instance of the song class
     """ 
    args = parse_args(arglist)

    test = BigFiveTest(args.questions_file)
    test.take_test()
    test.print_results()
    test.visualization()

    song_obj = Song(test.trait_scores, args.song_file)
    playlist = song_obj.song_playlist(test.trait_scores, num_songs=args.num_songs)

    print("Here's your playlist:")
    for song in playlist:
        print(song)

    highest_trait = song_obj.highest_score(test.trait_scores)
    print(f"-{highest_trait} seems to be one of your strongest traits! Enjoy a curated playlist made just for you!-")

    print(song_obj)

if __name__ == '__main__':
    main(sys.argv[1:])
   
    

def parse_args(arglist):
    
    parser = argparse.ArgumentParser(description='Big Five Test and Song Recommendation')

    parser.add_argument('questions_file', metavar='QUESTIONS_FILE', type=str,
                        help='path to the questions file')

    parser.add_argument('song_file', metavar='SONG_FILE', type=str,
                        help='path to the song recommendations file')

    parser.add_argument('--num-songs', type=int, default=3,
                        help='number of songs to include in the playlist (default: 3)')

    return parser.parse_args(arglist)