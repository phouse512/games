from typing import List, Any

class Match:

    def __init__(self, match: str, tournament: str, players: List[str]) -> None:
        self.match = match
        self.tournament = tournament
        self.players = players
        self.matches = []  # type: List[Any] 

    
