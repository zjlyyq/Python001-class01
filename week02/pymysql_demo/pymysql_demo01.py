import pymysql
import pretty_errors
import json
from config.getdbinfo import getconfig

result = []
dbInfo = getconfig()
sqls = ['select version()']
class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        # super().__init__()
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls



    def run(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()


if __name__ == "__main__":
    db = ConnDB(dbInfo, sqls)
    db.run()
    print(result)
