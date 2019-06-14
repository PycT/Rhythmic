import sqlite3;

class SQLiteDB:
    """ A class to handle SQLite3 database """

    def __init__(self, db_filename):

        self.connection = sqlite3.connect(db_filename);
        self.cursor = self.connection.cursor();

    def execute(self, sql_request):
        """ Execute a single sql command """

        self.cursor.execute(sql_request);

        return self.cursor.fetchall();

    def runScript(self, sql_script):
        """ Execute a script passed as a byte- or unicode string """

        self.cursor.executescript(sql_script);

        return self.cursor.fetchall();

    def __enter__(self):

        return self;

    def __exit__(self, type, value, traceback):

        self.connection.commit();
        self.connection.close();