import mysql.connector

if __name__ == '__main__':
    dbcon = mysql.connector.connect(
        database='analysis',
        user='root',
        password='password',
        host='db'
    )
    
    dbcur = dbcon.cursor()

    # テーブルability
    sql = 'DROP TABLE ability'
    dbcur.execute(sql)
    
    # テーブルresponse
    sql = 'DROP TABLE response'
    dbcur.execute(sql)
    
    # テーブルresult
    sql = 'DROP TABLE result'
    dbcur.execute(sql)
    
    dbcon.commit()


