import csv
import inspect
import mysql.connector

if __name__ == '__main__':
    dbcon = mysql.connector.connect(
        database='analysis',
        user='root',
        password='password',
        host='db'
    )
    
    dbcur = dbcon.cursor()
    
    # テーブル作成
    sql = 'CREATE TABLE IF NOT EXISTS responses ( id int NOT NULL PRIMARY KEY,'
    for i in range(1,110):
        sql += 'q' + str(i) + ' int NOT NULL,'
    sql = sql[:-1] + ')'
    dbcur.execute(sql)

    sql = 'INSERT IGNORE INTO responses values('
    for i in range(110):
        sql += '%s,'
    sql = sql[:-1] + ')'

    # csvデータのインサート
    with open('responses.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        i = 1
        for row in reader:
            dbcur.execute(sql % tuple(row))
            dbcon.commit()
