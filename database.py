import psycopg2

conn = psycopg2.connect(host="localhost", port=5432, database="bot", user="postgres", password="postgres")
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
        return (str(text))