# helps load the analytics file from a csv

import csv

class TournamentLoader:

    def __init__(self, filename):
        print("loading from %s" % filename)
        self.filename = filename
        self.games = []

    @staticmethod
    def is_empty_row(row):
        any_empty = False
        for i in row:
            any_empty = any_empty or i

        return not any_empty

    def run(self):

        file_reader = csv.reader(open(self.filename, newline=''),
                                 delimiter=',', quotechar='|')

        start_game = 0
        end_game = 0
        last_row = None
        last_two_row = None

        game_indexes = []
        csv_array = []
        for idx, row in enumerate(file_reader):
            if row[0].strip().lower() == 'game:':
                start_game = idx
           
            if self.is_empty_row(row) and self.is_empty_row(last_row) and self.is_empty_row(last_two_row):
                print("end of a game")
                end_game = idx - 2
                game_indexes.append([start_game, end_game])

            # we need to create an array copy because the reader disappears after one iteration
            csv_array.append(row)
            last_two_row = last_row 
            last_row = row

        print(game_indexes)
        
        # now that we have the start/end indexes of each game, now we can process them individually
        for index in game_indexes:
            print(len(list(csv_array)[index[0]:index[1]]))

            print("start row: %s" % csv_array[index[0]])
            print("end row: %s" % csv_array[index[1]])

loader = TournamentLoader('smash_summit_3.csv')
loader.run()
