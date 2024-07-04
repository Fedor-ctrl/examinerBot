import sqlite3

# Создаем таблицу Users
# connection = sqlite3.connect(path_to_db)
# cursor = connection.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY,
# tg_id INTEGER NOT NULL,
# name TEXT NOT NULL,
# ac_exam_pass INTEGER NOT NULL
# )
# ''')


path_to_db = "C:\\Users\IT\PycharmProjects\examinerBot\database_funcs\database.db"

#connection = sqlite3.connect(path_to_db)
#cursor = connection.cursor()
#cursor.execute('''
#CREATE TABLE IF NOT EXISTS Users (
#id INTEGER PRIMARY KEY,
#tg_id INTEGER NOT NULL,
#name TEXT NOT NULL,
#ac_exam_pass INTEGER NOT NULL
#)
#''')

def adding_users(tg_id: int, name: str):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Users (tg_id, name, ac_exam_pass) VALUES (?, ?, ?)', (tg_id, name, 0))
    connection.commit()
    connection.close()


# def adding_users_phone(tg_id: int, phone_num: str):
#     connection = sqlite3.connect(path_to_db)
#     cursor = connection.cursor()
#     if phone_num.startswith('+'):
#         phone_num = int(phone_num[1::])
#
#     cursor.execute('UPDATE Users SET phone_num = ? WHERE tg_id = ?', (phone_num, tg_id))
#     connection.commit()
#     connection.close()


def check_user(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('SELECT name from Users where tg_id = ?', (tg_id,))
    user = cursor.fetchone()
    connection.commit()
    connection.close()
    if user is None:
        return True
    else:
        return False


def check_user_ac(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    cursor.execute('SELECT ac_exam_pass from Users where tg_id = ?', (tg_id,))
    user = cursor.fetchone()
    print(user)
    connection.commit()
    connection.close()
    if user == (0,) or user is None:
        return False
    else:
        return True


# def check_sub(tg_id):
#     connection = sqlite3.connect(path_to_db)
#     cursor = connection.cursor()
#
#     cursor.execute('SELECT sub from Users where tg_id = ?', (tg_id,))
#     result = cursor.fetchone()
#     connection.commit()
#     connection.close()
#     if result is None or result == (0,):
#         return False
#     else:
#         return True


def import_users():
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    cursor.execute('SELECT tg_id, name, ac_exam_pass from Users')
    users = cursor.fetchall()

    connection.commit()
    connection.close()

    return users


def is_phone_num_exist(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    cursor.execute('SELECT phone_num from Users where tg_id = ?', (tg_id,))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    if result is None or result == (1,):
        return False
    else:
        return True


def get_phone_num(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    cursor.execute('SELECT phone_num from Users where tg_id = ?', (tg_id,))
    result = cursor.fetchone()
    connection.commit()
    connection.close()
    for elem in result:
        return str(elem)


def get_finished_with_ac(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ac_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()


def change_opportunity_for_ac_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ac_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()



