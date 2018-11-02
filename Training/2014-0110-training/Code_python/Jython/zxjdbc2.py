"""
Sample use of zxJDBC to read PostgreSQL database.

Requirement -- add the JDBC driver to your CLASSPATH.  For example,
in my case I added:

    postgresql-8.2-506.jdbc4.jar

"""

from com.ziclix.python.sql import zxJDBC

def test():
    d, u, p, v = (
        "jdbc:postgresql://thrush:5432/test",   # ... host, port, database
        "postgres",                             # user name
        "Flicker",                           # pass word
        "org.postgresql.Driver",                # driver
        )
    db = zxJDBC.connect(d, u, p, v, CHARSET='iso_1')
    cur = db.cursor()
    cur.execute('select * from plant_db')
    rows = cur.fetchall()
    s1 = '%s %s %s' % (
        'Name'.ljust(12),
        'Description'.ljust(24),
        'Rating'.ljust(10),
        )
    print s1
    s1 = '%s %s %s' % (
        '===='.ljust(12),
        '==========='.ljust(24),
        '======'.ljust(10),
        )
    print s1
    for row in rows:
        rating = str(row[2])
        print '%s %s %s' % (
            row[0].ljust(12), row[1].ljust(24), rating.ljust(10), )
    cur.close()
    db.close()

if __name__ == '__main__':
    test()
