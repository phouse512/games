from typing import List, Any
from utility import is_empty_row


class Kill:
    # this class represents a KILL, with a timestamp of who killed who
    #   with what character, what move, where, etc
    
    def __init__(self, kill_row: List[str]) -> None:
        self.time = kill_row[0]  # type: str
        self.attacker = kill_row[1].strip().lower()  # type: str
        self.defender = kill_row[2].strip().lower()  # type: str
        self.attacker_percent = int(kill_row[3])  # type: int
        self.defender_percent = int(kill_row[4])  # type: int
        self.killing_move = kill_row[5]  # type: str
        self.death_location = kill_row[6]  # type: str
        self.edge_guard = kill_row[7]  # type: str


class Match:
    # this class represents a MATCH, a subset of a game, that might be
    #   one of 3, 5, or 7. It has players, a stage, players, and the 
    #   events that transpired

    def __init__(self) -> None:
        self.players = []  # type: List[Dict[str, str]]
        return

    def load_from_list(self, match: List[List[str]]) -> None:
        self.match_name = match[0][0].lower() # type: str
        self.video_source = match[0][1]  # type: str
        self.video_start_time = match[0][2]  # type: str

        player_loop = True  # type: bool
        loop_index = 1  # type: int
        while player_loop:
            if is_empty_row(match[loop_index]):
                player_loop = False
                continue

            # winner data is stored on first line
            if loop_index == 1:
                self.winner = match[loop_index][4].lower()

            self.players.append({ 'player': match[loop_index][0].strip().lower(), 'character': match[loop_index][1].lower() })
            loop_index += 1


        # next, time to get the stage
        loop_index += 1
        self.stage = match[loop_index][1].lower()
        
        # bump up the loop index to get to the events
        loop_index += 4
        
        self.kills = []  # type: List[Kill]
        for row in match[loop_index:]:
            new_kill = Kill(row)
            self.kills.append(new_kill)
            

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
        just_match_array = game[3:]  # type: List[List[str]]
        for idx, row in enumerate(game[3:]):

            if 'match' in row[0].strip().lower():
                start_index = idx

            if is_empty_row(row) and is_empty_row(last_row):
                match_indexes.append([start_index, idx-1])
            
            last_row = row

        # we need to grab the last match, so just take the end of the list
        #   and pair with the last start
        match_indexes.append([start_index, len(game)])

        # now that we have all matches, pass each index pair to be loaded
        for match_index in match_indexes:
            match = Match()  # type: Match
            match.load_from_list(just_match_array[match_index[0]:match_index[1]])
            self.matches.append(match)

