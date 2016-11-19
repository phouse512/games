import pprint

from analysis import GameAnalyzer
from load_csv import TournamentLoader

loader = TournamentLoader('smash_summit_3.csv')
loader.run()

analyzer = GameAnalyzer(loader.games)

results = analyzer.kill_analysis()

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(results)
