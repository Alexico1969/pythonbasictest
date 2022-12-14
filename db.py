import sqlite3

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
    return db

def create_tables():
    db = get_db()
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, group TEXT, nr INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS challenges (nr INTEGER, code TEXT, solutions TEXT)")
    db.commit()

def add_user(name, group):
    db = get_db()
    c = db.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?)", (name, group, 1))
    db.commit()

def get_user(name):
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM users WHERE name=?", (name,))
    return c.fetchone()

def update_user(name, nr):
    db = get_db()
    c = db.cursor()
    c.execute("UPDATE users SET nr=? WHERE name=?", (nr, name))
    db.commit()

def add_challenge(nr, code, solutions):
    db = get_db()
    c = db.cursor()
    c.execute("INSERT INTO challenges VALUES (?,?,?)", (nr, code, solutions))
    db.commit()

def get_challenge(nr):
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM challenges WHERE nr=?", (nr,))
    return c.fetchone()

def get_challenges():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM challenges")
    return c.fetchall()

def get_users():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM users")
    return c.fetchall()


