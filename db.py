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

    # テーブルability
    sql = 'CREATE TABLE IF NOT EXISTS ability ( id int NOT NULL PRIMARY KEY, category int NOT NULL, ' \
        'title varchar(255) NOT NULL, description varchar(255) NOT NULL, number_of_quetions int, earn_point int )'
    dbcur.execute(sql)
    
    sql = 'INSERT IGNORE INTO ability values(%s, %s, '"'%s'"', '"'%s'"', %s, %s)'
    
    with open('csv/ability.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dbcur.execute(sql % tuple(row))

    # テーブルresponse
    sql = 'CREATE TABLE IF NOT EXISTS response ( id int NOT NULL PRIMARY KEY,'
    for i in range(1,110):
        sql += 'q' + str(i) + ' int NOT NULL,'
    sql = sql[:-1] + ')'
    dbcur.execute(sql)
    
    sql = 'INSERT IGNORE INTO response values('
    for i in range(110):
        sql += '%s,'
    sql = sql[:-1] + ')'
    
    with open('csv/response.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dbcur.execute(sql % tuple(row))

    # テーブルresult
    sql = 'CREATE TABLE IF NOT EXISTS result ( id int NOT NULL, ability int NOT NULL, point int NOT NULL,PRIMARY KEY(id,ability))'
    dbcur.execute(sql)
    
    sql = 'INSERT IGNORE INTO result values(%s, %s, %s)'
    
    with open('csv/result.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in range(1,20):
                dbcur.execute(sql % (row[0],i,row[i]))
    
    dbcon.commit()


