# helps load the analytics file from a csv

import csv
from game import Game
from utility import is_empty_row

class TournamentLoader:

    def __init__(self, filename: str) -> None:
        print("loading from %s" % filename)
        self.filename = filename
        self.games = []  # type: List[Game]

    def run(self):

        file_reader = csv.reader(open(self.filename, newline=''),
                                 delimiter=',', quotechar='|')

        start_game = 0  # type: int
        end_game = 0  # type: int
        last_row = None
        last_two_row = None

        game_indexes = []  # type: List[List[int]]
        csv_array = []
        counter = 0  # type: int
        for idx, row in enumerate(file_reader):
            if row[0].strip().lower() == 'game:':
                start_game = idx
           
            if is_empty_row(row) and is_empty_row(last_row) and is_empty_row(last_two_row):
                end_game = idx - 2
                game_indexes.append([start_game, end_game])

            # we need to create an array copy because the reader disappears after one iteration
            csv_array.append(row)
            last_two_row = last_row 
            last_row = row
            counter += 1

        game_indexes.append([start_game, counter])
        
        # now that we have the start/end indexes of each game, now we can process them individually
        for index in game_indexes:
            
            game = Game("some tourney")  # type: Game
            game.load_from_list(csv_array[index[0]:index[1]])

            self.games.append(game)


loader = TournamentLoader('smash_summit_3.csv')
loader.run()
