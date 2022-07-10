import sqlite3

DB_PATH = './todo.db'
NOT_STARTED = 'Not Started'
IN_PROGRESS = 'In Progress'
COMPLETED = 'Completed'


# Tutorial for sqlite python: https://www.sqlitetutorial.net/sqlite-python/

def add_to_list(task):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('insert into tasks(task, status) values(?,?)')
        conn.commit()
        return {"task": task, "status": NOT_STARTED}

    except Exception as error:
        print('Error: ', error)
        return None


def remove_from_list(task):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from tasks where task = ?')
        conn.commit()
        return {"task": task}

    except Exception as error:
        print('Error: ', error)
        return None


def update_status(task):
    pass
