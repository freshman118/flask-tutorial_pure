import MySQLdb
from flask import g


def get_db():
    if "db" not in g:
        g.db = MySQLdb.connect("localhost", "root", "123456", "blog").cursor()

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db:
        db.close()


if __name__ == '__main__':
    pass
