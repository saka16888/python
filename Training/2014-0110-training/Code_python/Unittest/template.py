import sqlite3
import unit_tests_lib

def test01():
    db_name = 'data1.db'
    connection = sqlite3.connect(db_name)
    rows = unit_tests_lib.fetch_rows(connection)
    print 'rows:', rows
    if len(rows) == 4:
        print 'test -- ok'
    else:
        print 'test -- bad'
    connection.close()

# -----------------------------------------------------------

def make_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MyTestCase))
    return suite


def main():
    suite = make_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    main()
