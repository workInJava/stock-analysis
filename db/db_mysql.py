import mysql.connector
from db_config import mysql_config

m_config = mysql_config()


class db_mysql_detail():

    def __init__(self, name):
        self.__name = name
        self.__conn = self.build_conn(name)
        self.__cursor = self.__conn.cursor()

    @property
    def conn(self):
        return self.__conn


    def build_conn(self, name):
        try:
            config = m_config.get_config(name)
            con = mysql.connector.connect(**config)
            return con
        except mysql.connector.Error as err:
            print('Something wrong: %s' % format(err))

    def selectAll(self, sql, where=()):
        if not where:
            self.__cursor.execute(sql)
        else:
            self.__cursor.execute(sql, where)
        return self.__cursor.fetchall()

    def selectOne(self, sql, where=()):
        if not where:
            self.__cursor.execute(sql)
        else:
            self.__cursor.execute(sql, where)
        return self.__cursor.fetchone()


    def insertBatch(self, insert_sql, batch_data):
        self.__cursor.executemany(insert_sql, batch_data)
        self.__conn.commit()
        print(self.__cursor.rowcount, "记录插入成功。")

    def insertOne(self, insert_sql, data):
        self.__cursor.execute(insert_sql, data)
        self.__conn.commit()
        print(self.__cursor.rowcount, "记录插入成功。")

    def updateBatch(self, update_sql, batch_data):
        self.__cursor.executemany(update_sql, batch_data)
        self.__conn.commit()
        print(self.__cursor.rowcount, "记录更新成功。")

    def close(self):
        self.__cursor.close()
        self.__conn.close()