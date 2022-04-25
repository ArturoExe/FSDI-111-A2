from multiprocessing.spawn import import_main_path
#Module File
from flask import g

import sqlite3 

DATABASE="user.db"


#Helper Function to connect to the database
def get_db():
    db=getattr(g,"_database",None)
    if not db:
        db=g._database=sqlite3.connect(DATABASE)
    return db