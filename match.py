import json
from pprint import pprint


def load_match(filename):
    with open(filename) as data_file:
        match_object = json.load(data_file)

    return match_object

def main(filename='league.json'):
    match = load_match(filename)

#    pprint(match['timeline'])
    print(len(match['timeline']['frames']))

    for frame in match['timeline']['frames']:
        print("iterating through frame")

#    pprint(match)


main()
