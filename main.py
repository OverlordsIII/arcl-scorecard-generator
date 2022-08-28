from parse_scorecard import parse_batting, parse_bowling
from tabulate import tabulate


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


def main():

    batting_scorecard = {
        "Aran": "1010000004o",
        "Neal": "11...1121.11111...11..111.2411..1.6641o",
        "Advay": ".2411.14.1.211211241.4..1441..2114111.12111",
        "Anirudh": "146",
    }

    bowling_scorecard = {
        "Anirudh": "1w11.1...14o.",
        "Thiru": "..w.w..1n241211",
        "Harshith": ".1.14.1121114411.w.",
        "Abhiram": "111.211..1....w1.1.o11n146",
        "Krish": "2411w.w411141.",
        "Shubh": "121..1124111",
        "Vishank": "216641"
    }

    batting_perfs = get_batting_performances(batting_scorecard)
    bowling_perfs = get_bowling_performances(bowling_scorecard)

    print_formatted_performances(batting_perfs, bowling_perfs)


if __name__ == "__main__":
    main()
