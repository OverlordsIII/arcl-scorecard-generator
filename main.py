from tabulate import tabulate
from parse_scorecard import parse_batting, parse_bowling


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

    batting_perfs = []
    bowling_perfs = []

    for key, value in batting_scorecard.items():
        parsed = parse_batting(value).as_array(key)
        batting_perfs.append(parsed)

    print("\nBatting\n")

    print(tabulate(batting_perfs, headers=[
          "Name", "Runs", "Balls", "4s", "6s", "SR"]))

    print("-"*50)

    for key, value in bowling_scorecard.items():
        parsed = parse_bowling(value).as_array(key)
        bowling_perfs.append(parsed)

    print("\nBowling\n")

    print(tabulate(bowling_perfs, headers=[
          "Name", "Overs", "No Balls", "Wides", "Runs", "Wickets"]))


if __name__ == "__main__":
    main()
