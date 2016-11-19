from game import Game
from game import Kill
from game import Match

from typing import Any
from typing import Dict
from typing import List


class GameAnalyzer:
    # this class is reponsible for analyzing large sets of games. 
    #   it is initialized with an immutable list of GAMES that can
    #   then be analyzed and broken down

    def __init__(self, games_list: List[Game]) -> None:
        self.all_games = games_list

    def kill_analysis(self) -> Dict[Any, Any]:
        databag = {}  # type: Dict[str, Dict[str, Dict[str, int]]]
        
        for game in self.all_games:
            for match in game.matches:
                for player in match.players:
                    if player['player'] == 'mew2king':
                        character = player['character']
                
                if character not in databag:
                    databag[character] = {}

                for kill in match.kills:
                    if kill.attacker == 'm2k':
                        if kill.killing_move not in databag[character]:
                            databag[character][kill.killing_move] = { 'counter': 0, 'total_percent': 0 }

                        databag[character][kill.killing_move]['counter'] += 1
                        databag[character][kill.killing_move]['total_percent'] += kill.defender_percent
                        
        return databag 
