import sqlite3
from os.path import isfile
import config
import csv


class Data:
    def __init__(self, database):
        self.db = database

        if isfile(database):
            # self.build_database(database)
            print("the file exists")

        else:
            print("creating database")
            self.build_database(database)
            self.search(self)

        self.connect_db(database)

    def build_database(self, database):
        table = """CREATE TABLE IF NOT EXISTS {0}(
                'id_' INT PRIMARY KEY, 'COL_01' TEXT, 'COL_02' TEXT UNIQUE , 'COL_03' TEXT, 'COL_04' TEXT, 'COL_05' TEXT, 'COL_06' TEXT,
                'COL_07' TEXT, 'COL_08' TEXT, 'COL_09' TEXT, 'COL_10' TEXT, 'COL_11' TEXT, 'COL_12' TEXT, 'COL_13' TEXT, 
                'COL_14' TEXT, 'COL_15' TEXT, 'COL_16' TEXT, 'COL_17' TEXT, 'COL_18' TEXT, 'COL_19' TEXT, 'COL_20' TEXT, 
                'COL_21' TEXT, 'COL_22' TEXT, 'COL_23' TEXT, 'COL_24' TEXT, 'COL_25' TEXT, 'COL_26' TEXT)""".format(
            config.tn_main
        )
        self.connect_db(database)
        try:
            self.conn.execute(
                "DROP TABLE {0}".format(config.tn_main)
            )  # todo remove the drop
        except:
            print("no table to drop")
        print("table dropped")
        self.conn.execute(table)
        self.conn.commit()

        reader = csv.reader(open("data.csv", newline=""), delimiter=",", quotechar="|")

        for row in reader:
            values = (
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
                row[11],
                row[12],
                row[13],
                row[14],
                row[15],
                row[16],
                row[17],
                row[18],
                row[19],
                row[20],
                row[21],
                row[22],
                row[23],
                row[24],
                row[25],
                row[26],
            )

            self.curs.execute(
                "INSERT INTO {0} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)".format(
                    config.tn_main
                ),
                values,
            )
        self.conn.commit()

        findings = self.curs.execute(
            "SELECT * FROM {0}".format(config.tn_main)
        ).fetchall()
        # print(findings)

    def connect_db(self, database):
        self.conn = sqlite3.connect(database)
        self.curs = self.conn

    def issqlite3(self):
        if isfile(self):
            return True
        else:
            return False

    def update(self, radio, alias):
        self.connect_db(self.db)
        test = list(self.curs.execute("SELECT COL_02 FROM '{0}'".format(config.tn_main, radio)).fetchall())

        #print(indata)

        if alias in test:
            print("exists")
        else:
            print("does not")
        #print(test)

        sql = """ UPDATE {0} (SET COL_02 = '{1}' WHERE id_ = {2}) WHERE NOT EXISTS (SELECT COL_02 FROM {0} = '{1}' )) """.format(
            config.tn_main, alias, radio
        )

        # sql = """ UPDATE {0} SET COL_02 = '{1}' WHERE id_ = {2}""".format(
        #     config.tn_main, alias, radio
        # )
        self.curs.execute(sql)
        self.conn.commit()

    def search(self, id):
        self.connect_db(self.db)
        print(
            self.curs.execute(
                "SELECT * FROM '{0}' WHERE id_ = {1}".format(config.tn_main, id)
            ).fetchall()
        )
        # todo remove print


db = Data("appsql.db")
db.update(4800003, "rssoger")
db.search(4800003)
