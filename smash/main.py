import pprint

from analysis import GameAnalyzer
from load_csv import TournamentLoader
from utility import write_multi_array_to_csv

loader = TournamentLoader('smash_summit_3.csv')
loader.run()

analyzer = GameAnalyzer(loader.games)

#results = analyzer.kill_analysis()
#results = analyzer.tournament_stats()
#results = analyzer.character_matchup_table()
results = analyzer.gimp_analysis()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(results)

# write_multi_array_to_csv(results, 'm2k_character_matchups')
