import psycopg2
from data import config

conn = psycopg2.connect(host=config.host, port=config.port, database=config.database, user=config.user, password=config.password)
cur = conn.cursor()
print("Database opened successfully")


class BD:
    def __init__(self):
        self.id = None
        self.nickname_tg = None

    def add_id(self):
        cur.execute("""SELECT * FROM users""")
        query_results = cur.fetchall()
        text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
        return str(text)
