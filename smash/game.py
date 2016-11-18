from typing import List, Any
from utility import is_empty_row


class Match:
    # this class represents a MATCH, a subset of a game, that might be
    #   one of 3, 5, or 7. It has players, a stage, players, and the 
    #   events that transpired

    def __init__(self) -> None:
        return

    def load_from_list(self, match: List[List[str]]) -> None:
        print("loading a match")
        for row in match:
            print(row)


class Game:
    # this class represents a GAME, set of matches (usually to best of 5)
    #   that players will compete in. For example, Winners Finals is 1 game,
    #   that might have 5 matches.
    def __init__(self, tournament: str) -> None:
        self.tournament = tournament
        self.matches = []  # type: List[Any]
        self.players = []  # type: List[str]

    def load_from_list(self, game: List[List[str]]) -> None:
        self.game_name = game[0][1]  # type: str
        for player in game[1]:
            if player:
                self.players.append(player)

        # now is time to go get match indexes
        last_row = ['dummy']  # type: List[str]
        match_indexes = []  # type: List[List[int]]
        start_index = 0  # type: int
        copy_array = []  # type: List[str]
        for idx, row in enumerate(game[3:]):

            print("idx: %s  | %s" % (idx, row))

            if 'match' in row[0].strip().lower():
                print("found starting index: %s" % idx)
                start_index = idx

            if is_empty_row(row) and is_empty_row(last_row):
                match_indexes.append([start_index, idx-1])
            
            last_row = row

        # we need to grab the last match, so just take the end of the list
        #   and pair with the last start
        match_indexes.append([start_index, len(game)])

        # now that we have all matches, pass each index pair to be loaded
        for match_index in match_indexes:
#            print(match_index)
            match = Match()  # type: Match
#            match.load_from_list(game[match_index[0]:match_index[1]])
#
        for i in game[match_indexes[0][0]:match_indexes[0][1]]:
            print(i)
