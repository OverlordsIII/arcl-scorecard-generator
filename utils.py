from parse_scorecard import parse_batting, parse_bowling


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
