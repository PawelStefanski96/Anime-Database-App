import psycopg2
import config
import sys


def insert_pg(data1,data2):
    thedata = (data1,data2) # -> tuple
    sql = ("""insert into test_table values (%s,%s);""" % thedata)

    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        conn.commit()
        cur.close()
        print ('Success.')
    except:
        print('WEO WEO')
    finally:
        if conn is not None:
            conn.close()

print(insert_pg(12,'ABC'))