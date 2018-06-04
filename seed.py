import csv
import mysql.connector
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == '__main__':
    dbcon = mysql.connector.connect(
        database='analysis',
        user='root',
        password='password',
        host='db'
    )

    dbcur = dbcon.cursor()

    # テーブルabilities
    sql = 'CREATE TABLE IF NOT EXISTS abilities ( ability_id int NOT NULL PRIMARY KEY, ' \
        'item varchar(255) NOT NULL, description varchar(255) NOT NULL)'
    dbcur.execute(sql)

    sql = 'INSERT IGNORE INTO abilities values(%d, '"'%s'"', '"'%s'"')'

    with open('csv/abilities.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        i = 0
        for row in reader:
            i += 1
            l = list(row)
            l.insert(0, i)
            dbcur.execute(sql % tuple(l))

    dbcon.commit()
