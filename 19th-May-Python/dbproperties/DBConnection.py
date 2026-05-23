from urllib.parse import quote_plus
from sqlalchemy import create_engine, text

class DBConnection:
    password = quote_plus("M1racle@123")
    DB_URL = f"mysql+pymysql://root:{password}@localhost/ITG_170"
    engine = create_engine(DB_URL)

    @staticmethod
    def fetch_all_users():
        with DBConnection.engine.connect() as connection:
            query = text('SELECT * FROM users')
            result = connection.execute(query)


            rows = result.fetchall()


            for row in rows:
                print(row)



DBConnection.fetch_all_users()