from typing import List, Dict, Union

import psycopg2
import psycopg2.extras


class PostgreSQLManager:

    def __init__(self, host, database, user, password, port):
        # Parameters will be inserted from a config file
        self.conn = None

        # Parameters for Postgres connection
        self.HOST = host
        self.DATABASE = database
        self.USER = user
        self.PASSWORD = password
        self.PORT = port

        # Parameters for schema of Postgres
        self.schema_name = 'public'

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(host=self.HOST,
                                         database=self.DATABASE,
                                         user=self.USER,
                                         password=self.PASSWORD,
                                         port=self.PORT)
            return self
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.conn:
            self.conn.close()

    def select(self, sql: str) -> Union[List[Dict], None]:
        cur = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        try:
            cur.execute(sql)
            res = cur.fetchall()
            if res:
                return res
            else:
                return [{"Error": "customer_id no encontrado"}]
        except psycopg2.errors.NumericValueOutOfRange:
            return None
