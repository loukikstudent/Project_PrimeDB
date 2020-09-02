import sqlite3



if __name__ == '__main__':
    con = sqlite3.connect(f"prime(0-{(2**1023)}).db")
    c = con.cursor()
    ###check if the table exist

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
