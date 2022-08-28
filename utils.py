from parse_scorecard import parse_batting, parse_bowling
from tabulate import tabulate


def batting_map(char): return 0 if char in ['.', 'o'] else int(char)


def bowling_map(char):
    if char in ['.', 'o']:
        return (0, True)
    if char in ['w', 'n']:
        return (1, False)

    return int(char), True


def bowling_stats(char):
    if char == 'o':
        return 'wickets'
    if char == 'w':
        return 'wides'
    if char == 'n':
        return 'no_balls'


def get_batting_performances(perf_info: dict[str, str]):
    ret = []

    for key, value in perf_info.items():
        parsed = parse_batting(value).as_array(key)
        ret.append(parsed)

    return ret


def get_bowling_performances(perf_info: dict[str, str]):
    ret = []

    for key, value in perf_info.items():
        parsed = parse_bowling(value).as_array(key)
        ret.append(parsed)

    return ret


def print_formatted_performances(batting_perfs, bowling_perfs):
    batting_columns = ["Name", "Runs", "Balls", "4s", "6s", "SR"]
    bowling_columns = ["Name", "Overs", "No Balls", "Wides", "Runs", "Wickets"]

    print("\nBatting\n")
    print(tabulate(batting_perfs, headers=batting_columns))
    print("-"*50)
    print("\nBowling\n")
    print(tabulate(bowling_perfs, headers=bowling_columns))
