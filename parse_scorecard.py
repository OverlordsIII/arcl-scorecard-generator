from utils import batting_map, bowling_map, bowling_stats
from math import floor


class BattingWrapper(object):
    def __init__(self, runs, balls, fours, sixes, sr) -> None:
        self.runs = runs
        self.balls = balls
        self.fours = fours
        self.sixes = sixes
        self.sr = sr

    def as_array(self, name):
        return [name, self.runs, self.balls, self.fours, self.sixes, self.sr]


class BowlingWrapper(object):
    def __init__(self, runs, balls, no_balls, wides, wickets) -> None:
        self.runs = runs
        self.no_balls = no_balls
        self.wides = wides
        self.wickets = wickets

        self.overs = floor(balls/6)
        self.remaining_balls = balls % 6

    def as_array(self, name):
        return [f'{name, self.overs}.{self.remaining_balls}', self.no_balls, self.wides, self.wickets]


def parse_batting(s, ball_by_ball=False):
    balls = 0
    runs = 0
    fours = 0
    sixes = 0
    for char in s:
        value = batting_map(char)

        if value == 4:
            fours += 1

        if value == 6:
            sixes += 1

        balls += 1
        runs += value
        if ball_by_ball:
            print(f"{runs} ({balls})")

    sr = round(100 * (runs / balls), 2)

    return BattingWrapper(runs, balls, fours, sixes, sr)


def parse_bowling(s, ball_by_ball=False):
    balls = 0
    runs = 0

    stats = {
        'wickets': 0,
        'no_balls': 0,
        'wides': 0
    }

    special = ['w', 'n', 'o']

    for char in s:
        (value, append_ball) = bowling_map(char)

        if append_ball:
            balls += 1

        runs += value

        if char in special:
            stats[bowling_stats(char)] += 1

    return BowlingWrapper(runs, balls, **stats)
