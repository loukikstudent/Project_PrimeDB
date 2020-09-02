import sqlite3
import logging
from typing import List


def create_connection(db_name: str):
    """

        :type db_name: str
        :param db_name:
        """
    con = sqlite3.connect(db_name)
    c = con.cursor()
    logging.debug("Connection Created")
    return con, c


def add_table_prime_number(db_name: str):
    """

        :type db_name: str
        :param db_name:
        """
    con, c = create_connection(db_name)
    query = 'CREATE TABLE prime_number (ID int PRIMARY KEY NOT NULL,number int NOT NULL UNIQUE , carry int NOT NULL);'
    c.execute(query)
    con.close()
    logging.info("Prime Table Connected")


def add_table_lucas(db_name: str):
    """

        :type db_name: str
        :param db_name:
        """
    con, c = create_connection(db_name)
    query = 'CREATE TABLE lucas (ID int PRIMARY KEY NOT NULL,lucas_series int NOT NULL UNIQUE , carry int NOT NULL);'
    c.execute(query)
    con.close()
    logging.info("Lucas Table Created")


def add_table_lucas_lehmer(db_name: str):
    """

    :type db_name: str
    :param db_name:
    """
    con, c = create_connection(db_name)
    query = 'CREATE TABLE lucas_lehmer (ID int PRIMARY KEY NOT NULL ,lucas_lehmer_series int NOT NULL UNIQUE , carry int NOT NULL);'
    c.execute(query)
    con.close()
    logging.info("Lucas Lehmer Table Connected")


def check_or_create_table(db_name: str) -> bool:
    """

    :type db_name: str
    :param db_name:
    :return:
    """
    con, c = create_connection(db_name)
    query = f'select name from sqlite_master where type =\'table\';'
    result = c.execute(query).fetchall()
    con.close()
    if len(result) == 3:
        logging.info("Tables created/verified")
        return True
    else:
        logging.info("Creating Missing Tables")
        if len(result) == 0:
            add_table_prime_number(db_name)
            add_table_lucas(db_name)
            add_table_lucas_lehmer(db_name)
        elif 'prime_number' not in result:
            add_table_prime_number(db_name)
        elif 'lucas' not in result:
            add_table_lucas(db_name)
        elif 'lucas_lehmer' not in result:
            add_table_lucas_lehmer(db_name)
        return check_or_create_table(db_name)


def insert_into_table(db_name: str, table_name, number: int, carry: int) -> bool:
    """
    :type table_name: str
    :param db_name:
    :param table_name:
    :param number:
    :param carry:
    """
    con, c = create_connection(db_name)
    query = f'INSERT INTO {table_name} VALUES (NULL ,{number},{carry})'
    try:
        c.execute()
        logging.info("Values number : %d , carrd : %d inserted into %s", number, carry, table_name)
        return True
    except:
        logging.error("Could not insert into table: %s", table_name)
        con.close()
        return False


def view_lucas_lehmer_series_closest_to_number(db_name: str, number: int, ) -> List[int]:
    con, c = create_connection(db_name)
    query = f'select id,lucas_lehmer_series from lucas_lehmer where lucas_lehmer_series >=number order by lucas_lehmer_series ASC LIMIT 1'
    result = c.execute(query)
    return result[0]

if __name__ == '__main__':
    check_or_create_table('prime.sqlite3')

