import mysql.connector

if __name__ == '__main__':
    dbcon = mysql.connector.connect(
        database='analysis',
        user='root',
        password='password',
        host='db'
    )

    dbcur = dbcon.cursor()

    sql = 'DROP TABLE abilities'
    dbcur.execute(sql)
