from decimal import *

from game import Game
from game import Kill
from game import Match

from math import floor

from typing import Any
from typing import Dict
from typing import List

from utility import time_difference_to_int

getcontext().prec = 6


class GameAnalyzer:
    # this class is reponsible for analyzing large sets of games. 
    #   it is initialized with an immutable list of GAMES that can
    #   then be analyzed and broken down

    def __init__(self, games_list: List[Game]) -> None:
        self.all_games = games_list

    def simple_death_analysis(self) -> Dict[Any, Any]:
        return {}

    def damage_per_min_analysis(self) -> Dict[Any, Any]:
        damage_dealt = {}  # type: Dict[Any, Any]
        for game in self.all_games:
            for match in game.matches:
                player_map = {}                
                for player in match.players:
                    if player['player'] == 'mew2king' and 'm2k' not in damage_dealt:
                        print("enter only once")
                        damage_dealt['m2k'] = {}
                    elif player['player'] not in damage_dealt and player['player'] != 'mew2king':
                        damage_dealt[player['player']] = { }
                   
                    if player['player'] == 'mew2king':
                        key = 'm2k'
                    else:
                        key = player['player']

                    player_map[key] = player['character']
                    if player_map[key] not in damage_dealt[key]:
                        damage_dealt[key][player_map[key]] = { 'count': 0, 'match_time': 0 }

                    damage_dealt[key][player_map[key]]['match_time'] += time_difference_to_int('8:00', match.kills[len(match.kills)-1].time) 
                print(player_map)
                print(damage_dealt)
                for idx, kill in enumerate(match.kills):
                    print(player_map[kill.attacker])
                    damage_dealt[kill.attacker][player_map[kill.attacker]]['count'] += kill.defender_percent

                    if idx == len(match.kills) -1:
                        damage_dealt[kill.defender][player_map[kill.defender]]['count'] += kill.attacker_percent

        for key in damage_dealt:
            for char_key in damage_dealt[key]:
                match_time_minutes = Decimal(damage_dealt[key][char_key]['match_time']) / 60  # type: Decimal
                dmg_per_min = Decimal(damage_dealt[key][char_key]['count']) / match_time_minutes
                damage_dealt[key][char_key]['dpm'] = dmg_per_min

        return damage_dealt


    def comeback_analysis(self, player_name: str) -> Dict[Any, Any]:
        DEFAULT_STOCK = 4  # type: int
        comeback_counts = {}

        for game in self.all_games:
            for match in game.matches:
                stock_count = {}
                for player in match.players:
                    if player['player'] != 'mew2king':
                        other_player = player['player']

                stock_count[player_name] = DEFAULT_STOCK
                stock_count[other_player] = DEFAULT_STOCK

                for kill in match.kills:
                    
                    # we need to compare stock counts to each other
                    if stock_count[other_player] > 1 and stock_count[other_player] == stock_count[player_name]:
                        print("found a 2-2, 3-3, 4-4 situation:  %s-%s" % (stock_count[other_player], stock_count[player_name]))

                        # now that it's even (before subtracting this kill), see if the player (m2k) is going down
                        if kill.defender == player_name and kill.attacker_percent < 50:

                            comeback_key = "%s-%s" % (game.game_name, match.match_name)
                            
                            if comeback_key not in comeback_counts:
                                comeback_counts[comeback_key] = { }
                            
                            comeback_counts[comeback_key]['winner'] = match.winner
                            stock_key = "%s-%s" % (stock_count[other_player], stock_count[player_name])
                            comeback_counts[comeback_key][stock_key] = 1
                    
                    # adjust stock count for latest kill
                    stock_count[kill.defender] = stock_count[kill.defender]-1

        return comeback_counts

    def gimp_analysis(self) -> Dict[Any, Any]:
        gimp_kills = {}  # type: Dict[Any, Any] 
        gimp_kills['victim'] = {}
        gimp_kills['attacker'] = {}
        
        for game in self.all_games:
            for match in game.matches:
                
                m2k_char = ""  # type: str
                other_char = ""  # type: str
                for player in match.players:
                    if player['player'] == 'mew2king':
                        m2k_char = player['character']
                    else:
                        other_char = player['character']

                for kill in match.kills:
                    if kill.defender_percent <= 50:

                        if kill.attacker == 'm2k':
                            key = m2k_char + '-' + kill.killing_move
                            gimp_kills['attacker'][key] = gimp_kills['attacker'].get(key, 0) + 1
                        else:
                            key = other_char + '-' + kill.killing_move
                            gimp_kills['victim'][key] = gimp_kills['victim'].get(key, 0) + 1

        return gimp_kills


    def character_matchup_table(self) -> List[List[str]]:
        match_table = {}  # type: Dict[str, Any]

        for game in self.all_games:
            for match in game.matches:
                for player in match.players:
                    if player['player'] == 'mew2king':
                        m2k = player['character']
                    else:
                        other = player['character']

                string_hash = m2k + '-' + other
                if string_hash not in match_table:
                    match_table[string_hash] = { 'count': 0, 'win_count': 0, 'match_time': 0 }

                match_table[string_hash]['count'] += 1
                
                match_table[string_hash]['match_time'] += time_difference_to_int('8:00', match.kills[len(match.kills)-1].time)

                if match.winner == 'm2k':
                    match_table[string_hash]['win_count'] += 1

        # perform time avg calculations, and handle formatting back to string format: "mm:ss"
        for key in match_table:
            time_avg = Decimal(match_table[key]['match_time']) / Decimal(match_table[key]['count'])

            time_avg_minutes = floor(float(time_avg) / 60)  # type: float
            time_avg_seconds = time_avg % 60  # type: Decimal

            if time_avg_seconds < 10:
                time_avg_seconds_string = "0" + str(time_avg_seconds)  # type: str
            else:
                time_avg_seconds_string = str(time_avg_seconds)

            match_table[key]['avg_match_time'] = "%s:%s" % (str(time_avg_minutes), time_avg_seconds_string)
            del match_table[key]['match_time']

        # turn dict into a list that can be turned into a csv
        header_row = ['character matchup', 'win-loss record', 'avg time per game']
        return_list = [header_row]

        for key in match_table:
            win_count = match_table[key]['win_count']
            loss_count = match_table[key]['count'] - win_count
            win_loss_str = str(win_count) + '-' + str(loss_count)
            temp_row = [key, win_loss_str, match_table[key]['avg_match_time']]
            return_list.append(temp_row)

        return return_list

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
