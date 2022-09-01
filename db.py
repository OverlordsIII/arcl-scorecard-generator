from pg import DB

class DatabaseHandler:

    def __init__(self, dbname):
        self.db = DB(dbname=dbname)

    def setup_tables(self):
        print(self.db.get_tables())
        if not self.db.get_tables().__contains__("public.batting_performances"):
            self.db.query("create table batting_performances(id serial primary key, name varchar, runs int, balls int, fours int, sixes int, SR float)")
        if not self.db.get_tables().__contains__("public.bowling_performances"):
            self.db.query("create table bowling_performances(id serial primary key, name varchar, overs int, no_balls int, wides int, runs int, wickets int, eco_rate float)")
        if not self.db.get_tables().__contains__("public.bowling_career"):
            self.db.query("create table bowling_career(id serial primary key, name varchar, overs int, no_balls int, wides int, runs int, wickets int, eco_rate float)")
        if not self.db.get_tables().__contains__("public.batting_career"):
            self.db.query("create table batting_career(id serial primary key, name varchar, runs int, balls int, fours int, sixes int, SR float)")

    def add_batting_performance(self, name, runs, balls, fours, sixes, SR):
        self.db.insert("batting_performances", name=name, runs=runs, balls=balls, fours=fours, sixes=sixes, sr=float(SR))

    def add_bowling_performance(self, name, overs, no_balls, wides, runs, wickets, eco_rate):
        self.db.query(f"insert into bowling_performances (name, overs, no_balls, wides, runs, wickets, eco_rate) values ('{name}', {overs}, {no_balls}, {wides}, {runs}, {wickets}, {eco_rate})")

    def drop_tables(self):
        for table in self.db.get_tables():
            self.db.query(f"drop table {table};")

#for testing
if __name__ == "__main__":
    handler = DatabaseHandler("scorecard")
    handler.drop_tables()