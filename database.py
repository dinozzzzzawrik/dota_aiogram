import psycopg2
from data import config


class BD:
    try:
        connection = psycopg2.connect(host=config.host, port=config.port, database=config.database, user=config.user,
                                      password=config.password)
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                 """CREATE TABLE IF NOT EXISTS users(
                     id serial PRIMARY KEY,
                     tg_id varchar(50) NOT NULL,
                     dota_id varchar(50) NOT NULL);"""
            )
            print("[INFO] Table created successfully")

        @staticmethod
        def add_id(dota_id, tg_id):
            connection = psycopg2.connect(host=config.host, port=config.port, database=config.database,
                                          user=config.user,
                                          password=config.password)
            connection.autocommit = True
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""INSERT INTO users (tg_id, dota_id) VALUES
                    ({tg_id}, {dota_id});"""
                )

    except (Exception, psycopg2.Error) as error:
        print(f"[ERROR] Error while connecting to PostgreSQL: {error}")
