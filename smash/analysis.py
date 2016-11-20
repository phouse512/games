from decimal import *

from game import Game
from game import Kill
from game import Match

from typing import Any
from typing import Dict
from typing import List

getcontext().prec = 6

class GameAnalyzer:
    # this class is reponsible for analyzing large sets of games. 
    #   it is initialized with an immutable list of GAMES that can
    #   then be analyzed and broken down

    def __init__(self, games_list: List[Game]) -> None:
        self.all_games = games_list

    def simple_death_analysis(self) -> Dict[Any, Any]:
        return {}

    def character_matchup_table(self) -> List[List[str]]:
        for game in self.all_games:
            for match in game.matches:

                print(match.winner)

    def tournament_stats(self) -> Dict[Any, Any]:
        """
        This method breaks down the number of games and sets played by
        M2K as well as returns his win/loss record in sets.
        """
        databag = {}  # type: Dict[str, Any]

        databag['round_count'] = 0
        databag['set_count'] = 0
        databag['set_win_count'] = 0

        for game in self.all_games:
            databag['round_count'] += 1
            for match in game.matches:
                databag['set_count'] += 1
                if match.winner == 'm2k':
                    databag['set_win_count'] += 1

        return databag


    def simple_kill_analysis(self) -> Dict[Any, Any]:
        databag = {}  # type: Dict[str, Dict[str, Dict[str, Any]]]
        m2k_kill_count = 0  # type: int
        move_totals = {}  # type: Dict[str, int]
        
        for game in self.all_games:
            for match in game.matches:
                for player in match.players:
                    if player['player'] == 'mew2king':
                        character = player['character']
                
                if character not in databag:
                    databag[character] = {}

                if character not in move_totals:
                    move_totals[character] = 0

                for kill in match.kills:
                    if kill.attacker == 'm2k':
                        move_totals[character] += 1

                        if kill.killing_move not in databag[character]:
                            databag[character][kill.killing_move] = { 'counter': 0, 'total_percent': 0, 'edge_guard': 0 }

                        databag[character][kill.killing_move]['counter'] += 1
                        databag[character][kill.killing_move]['total_percent'] += kill.defender_percent
                        if kill.edge_guard == 'TRUE':
                            databag[character][kill.killing_move]['edge_guard'] += 1
        

        for key in databag:
            for move in databag[key]:
                avg_percent = Decimal(databag[key][move]['total_percent']) / Decimal(databag[key][move]['counter'])
                databag[key][move]['avg_percent'] = str(avg_percent)

                count_percent = Decimal(databag[key][move]['counter']) / Decimal(move_totals[key])
                databag[key][move]['usage_proportion'] = str(count_percent)

                del databag[key][move]['total_percent']
                del databag[key][move]['counter']


        return databag 
