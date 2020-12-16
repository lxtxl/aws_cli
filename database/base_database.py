
#!/usr/bin/env python
import sqlite3

class BaseDatabase:
    fileName = "default.db"

    def __init__(self):
        pass

    def __init__(self, filename):
        self.fileName = filename

    def exist_data(self, table_name):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        c.execute("SELECT count(*) AS count from {}".format(table_name, ))

        row = c.fetchone()
        conn.close()

        if row[0] == 0:
            return False
        return True

    def exist_common_where(self, table_name, where_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        c.execute("SELECT count(*) AS count from {} WHERE {}".format(table_name, where_string))

        row = c.fetchone()
        conn.close()

        if row[0] == 0:
            return False
        return True

    def select_common_count(self, table_name, where_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        complete_query = "SELECT count(*) AS count from {} WHERE {}".format(table_name, where_string)
        # print(complete_query)
        c.execute(complete_query)

        row = c.fetchone()
        conn.close()

        return row[0]

    def update_data_all(self, table_name, set_info):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        complete_query = "UPDATE {} set {}".format(table_name, set_info)
        # print(complete_query)
        c.execute(complete_query)
        conn.commit()
        conn.close()        

    def create_table(self, table_name, parameter_info):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        complete_query = "CREATE TABLE IF NOT EXISTS {} ( id integer NOT NULL PRIMARY KEY AUTOINCREMENT, {})".format(table_name, parameter_info)
        print(complete_query)
        c.execute(complete_query)
        conn.commit()
        conn.close()

    def update_common_data(self, table_name, set_info, where_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query_string = "UPDATE {} set {} WHERE {}".format(table_name, set_info, where_string)
        print(query_string)
        c.execute(query_string)
        conn.commit()
        conn.close()        

    def insert_common_data(self, table_name, name_string, value_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = """
        INSERT INTO {} 
        (
            {}
        ) VALUES(
            {}
        )
        """
        query_result = query.format(table_name, name_string, value_string)
        print(query_result)
        c.execute(query_result)
        id = c.lastrowid
        conn.commit()
        conn.close()

        return id

    def select_common_one(self, table_name, column_string, where_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = """
        SELECT 
            {} 
        FROM 
            {}
        WHERE
            {}
        ORDER BY id ASC
        """
        complete_query = query.format(column_string, table_name, where_string)

        c.execute(complete_query)

        row = c.fetchone()
        conn.close()

        if row == None:
            return None

        return row

    def select_common_all(self, table_name, column_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = """
        SELECT 
            {} 
        FROM 
            {}
        """

        c.execute(query.format(column_string, table_name))

        rows = c.fetchall()
        conn.close()

        return rows

    def select_common_all_asc(self, table_name, column_string, order_by_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = """
        SELECT 
            {} 
        FROM 
            {}
        ORDER BY
            {} ASC
        """

        c.execute(query.format(column_string, table_name, order_by_string))

        rows = c.fetchall()
        conn.close()

        return rows

    def select_common_where(self, table_name, column_string, where_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = """
        SELECT 
            {} 
        FROM 
            {}
        WHERE
            {}
        """

        complete_query_string = query.format(column_string, table_name, where_string)
        # print(complete_query_string)
        c.execute(complete_query_string)

        rows = c.fetchall()
        conn.close()

        return rows

    def select_common_where_asc(self, table_name, column_string, where_string, value):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = """
        SELECT 
            {} 
        FROM 
            {}
        WHERE
            {}
        ORDER BY
            {} ASC
        """

        c.execute(query.format(column_string, table_name, where_string, value))

        rows = c.fetchall()
        conn.close()

        return rows

    def select_common_distinct(self, table_name, column_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = """
        SELECT 
            DISTINCT {} 
        FROM 
            {}
        """

        c.execute(query.format(column_string, table_name))

        rows = c.fetchall()
        conn.close()

        return rows

    def select_common_distinct_where(self, table_name, column_string, where_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = """
        SELECT 
            DISTINCT {} 
        FROM 
            {}
        WHERE
            {}
        """

        c.execute(query.format(column_string, table_name, where_string))

        rows = c.fetchall()
        conn.close()

        return rows

    def select_distinct(self, table_name, column_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = """
        SELECT 
            DISTINCT {} 
        FROM 
            {}
        """

        c.execute(query.format(column_string, table_name))

        rows = c.fetchall()
        conn.close()

        return rows

    def select_raw_all(self, query_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = query_string

        c.execute(query)

        rows = c.fetchall()
        conn.close()

        return rows

    def select_raw_one(self, query_string):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        query = query_string

        c.execute(query)

        row = c.fetchone()
        conn.close()

        if row == None:
            return None

        return row

    def delete_all(self, table_name):
        conn = sqlite3.connect(self.fileName)
        c = conn.cursor()

        complete_query = "DELETE FROM {}".format(table_name)
        c.execute(complete_query)
        conn.commit()
        conn.close()