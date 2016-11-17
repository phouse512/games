from typing import List, Any
from utility import is_empty_row


class Match:

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
        for idx, row in enumerate(game[3:]):

            if 'match' in row[0].strip().lower():
                start_index = idx

            if is_empty_row(row) and is_empty_row(last_row):
                match_indexes.append([start_index, idx-1])
            
            last_row = row

        # we need to grab the last match, so just take the end of the list
        #   and pair with the last start
        match_indexes.append([start_index, len(game)-1])

        for match_index in match_indexes:
            match = Match()  # type: Match
            match.load_from_list(game[match_index[0]:match_index[1]])

