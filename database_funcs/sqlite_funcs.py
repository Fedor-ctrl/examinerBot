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


path_to_db = r"C:\Users\PC\PycharmProjects\examinerBot\database_funcs\database.db"


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
    """
    Добавляет нового пользователя в базу данных.
    :param tg_id: Telegram ID пользователя.
    :param name: Имя пользователя.
    """
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        cursor.execute(
            '''
            INSERT INTO Users (tg_id, name, ac_exam_pass, car_exam_pass, another_exam_pass, pr_exam_pass, pr_exam_pass_1, pr_exam_pass_2, pr_exam_pass_3,
            pr_exam_pass_4, tr_exam_pass, ob_exam_pass, st_exam_pass, st_pr_exam_pass, id_exam_pass, is_exam_pass, pr_ds_exam_pass, kd_exam_pass, ot_exam_pass,
            mk_exam_pass, pz_exam_pass, sn_exam_pass, sb_exam_pass, rn_exam_pass, bc_exam_pass, pj_exam_pass, lt_exam_pass, pv_exam_pass, ki_exam_pass,
            lr_exam_pass, ms_exam_pass, sd_exam_pass, dd_exam_pass)
            VALUES (?, ?, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            ''',
            (tg_id, name)
        )
        connection.commit()
        print(f"Пользователь {name} добавлен в базу данных.")
    except sqlite3.IntegrityError:
        print("Пользователь уже существует.")
    except sqlite3.Error as e:
        print(f"Ошибка добавления пользователя: {e}")
    finally:
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


def check_user(tg_id: int) -> bool:
    """
    Проверяет, есть ли пользователь в базе данных.
    :param tg_id: Telegram ID пользователя.
    :return: True, если пользователя нет в базе (можно добавить), иначе False.
    """
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        cursor.execute('SELECT id FROM Users WHERE tg_id = ?', (tg_id,))
        user = cursor.fetchone()
        return user is None  # Возвращает True, если пользователь не найден
    except sqlite3.Error as e:
        print(f"Ошибка SQL: {e}")
        return False
    finally:
        connection.close()



def check_user_test(tg_id: int, test_column: str) -> bool:
    """
    Проверяет, проходил ли пользователь указанный тест.

    :param tg_id: Telegram ID пользователя.
    :param test_column: Название столбца для проверки.
    :return: True, если тест пройден, иначе False.
    """
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        cursor.execute(f'SELECT {test_column} FROM Users WHERE tg_id = ?', (tg_id,))
        user = cursor.fetchone()
        connection.close()

        if user is None or user[0] == 0:
            return False
        return True
    except sqlite3.Error as e:
        print(f"Ошибка SQL: {e}")
        connection.close()
        return False


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

    cursor.execute('SELECT tg_id, name, ac_exam_pass, car_exam_pass, pr_exam_pass, pr_exam_pass_1, pr_exam_pass_2, pr_exam_pass_3, pr_exam_pass_4,tr_exam_pass, ob_exam_pass,'
                   'st_exam_pass, st_pr_exam_pass, id_exam_pass, is_exam_pass, pr_ds_exam_pass, kd_exam_pass, ot_exam_pass, mk_exam_pass, pz_exam_pass, '
                   'sn_exam_pass, sb_exam_pass, rn_exam_pass, bc_exam_pass, pj_exam_pass, lt_exam_pass, pv_exam_pass, ki_exam_pass, lr_exam_pass, ms_exam_pass, '
                   'sd_exam_pas, dd_exam_pass from Users')
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

def get_finished_with_car(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set car_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_ac(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ac_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_pr(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_pr_1(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_exam_pass_1 = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_pr_2(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_exam_pass_2 = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_pr_3(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_exam_pass_3 = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_pr_4(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_exam_pass_4 = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_tr(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set tr_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_ob(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ob_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_st(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set st_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_st_pr(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set st_pr_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_id(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set id_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_is(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set is_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_pr_ds(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_ds_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_kd(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set kd_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_ot(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ot_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_mk(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set mk_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_pz(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pz_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_sn(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set sn_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_sb(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set sb_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_rn(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set rn_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_bc(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set bc_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_pj(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pj_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_lt(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set lt_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_pv(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pv_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_ki(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ki_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_lr(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set lr_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_ms(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set lr_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_sd(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set sd_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def get_finished_with_dd(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set dd_exam_pass = 1 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_car_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set car_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_ac_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ac_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_pr_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_pr_test_1(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_exam_pass_1 = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_pr_test_2(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_exam_pass_2 = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_pr_test_3(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_exam_pass_3 = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_pr_test_4(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_exam_pass_4 = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_tr_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set tr_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_ob_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ob_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_st_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set st_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_st_pr_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set st_pr_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_id_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set id_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_is_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set is_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_pr_ds_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pr_ds_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_kd_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set kd_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_ot_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ot_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_mk_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set mk_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_pz_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pz_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_sn_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set sn_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_sb_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set sb_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_rn_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set rn_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_bc_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set bc_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_pj_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pj_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_lt_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set lt_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_pv_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set pv_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_ki_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ki_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_lr_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set lr_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_ms_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set ms_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_sd_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set sd_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def change_opportunity_for_dd_test(tg_id):
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()
    cursor.execute('Update Users Set dd_exam_pass = 0 where tg_id = ?', (tg_id,))
    connection.commit()
    connection.close()

def update_test_status(tg_id: int, test_column: str, status: int):
    """
    Обновляет статус указанного теста для пользователя.
    :param tg_id: Telegram ID пользователя.
    :param test_column: Название столбца (например, pr_exam_pass).
    :param status: Новый статус теста (1 - пройден, 0 - не пройден).
    """
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    ALLOWED_COLUMNS = {'ac_exam_pass','car_exam_pass','pr_exam_pass', 'pr_exam_pass_1', 'pr_exam_pass_2', 'pr_exam_pass_3', 'pr_exam_pass_4', 'tr_exam_pass',
                       'ob_exam_pass', 'st_exam_pass', 'st_pr_exam_pass', 'id_exam_pass', 'is_exam_pass', 'pr_ds_exam_pass', 'kd_exam_pass', 'ot_exam_pass',
                       'mk_exam_pass', 'pz_exam_pass', 'sn_exam_pass', 'sb_exam_pass', 'rn_exam_pass', 'bc_exam_pass', 'pj_exam_pass', 'lt_exam_pass',
                       'pv_exam_pass', 'ki_exam_pass', 'lr_exam_pass', 'ms_exam_pass', 'sd_exam_pass', 'dd_exam_pass'}  # Допустимые столбцы

    try:
        # Проверка на допустимый столбец
        if test_column not in ALLOWED_COLUMNS:
            print(f"Ошибка: Недопустимый столбец {test_column}")
            return

        # Проверка наличия пользователя
        cursor.execute("SELECT tg_id FROM Users WHERE tg_id = ?", (tg_id,))
        if cursor.fetchone() is None:
            print(f"Ошибка: Пользователь с tg_id {tg_id} не найден.")
            return

        # Обновление статуса теста
        print(f"Обновление статуса: tg_id={tg_id}, column={test_column}, status={status}")
        cursor.execute(f'UPDATE Users SET {test_column} = ? WHERE tg_id = ?', (status, tg_id))
        connection.commit()

        # Проверка затронутых строк
        if cursor.rowcount == 0:
            print(f"Предупреждение: Обновление не выполнено для tg_id={tg_id}")
        else:
            print(f"Статус теста обновлён для пользователя {tg_id}: {test_column} = {status}")
    except sqlite3.Error as e:
        print(f"Ошибка обновления теста: {e}")
    finally:
        connection.close()


def update_table_users():
    """
    Обновляет таблицу Users, добавляя недостающие столбцы.
    """
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    required_columns = {
        'car_exam_pass': 'INTEGER DEFAULT 0',
        'another_exam_pass': 'INTEGER DEFAULT 0',
        'pr_exam_pass': 'INTEGER DEFAULT 0',
        'pr_exam_pass_1': 'INTEGER DEFAULT 0',
        'pr_exam_pass_2': 'INTEGER DEFAULT 0',
        'pr_exam_pass_3': 'INTEGER DEFAULT 0',
        'pr_exam_pass_4': 'INTEGER DEFAULT 0',
        'tr_exam_pass': 'INTEGER DEFAULT 0',
        'ob_exam_pass': 'INTEGER DEFAULT 0',
        'st_exam_pass': 'INTEGER DEFAULT 0',
        'st_pr_exam_pass': 'INTEGER DEFAULT 0',
        'id_exam_pass': 'INTEGER DEFAULT 0',
        'is_exam_pass': 'INTEGER DEFAULT 0',
        'pr_ds_exam_pass': 'INTEGER DEFAULT 0',
        'kd_exam_pass': 'INTEGER DEFAULT 0',
        'ot_exam_pass': 'INTEGER DEFAULT 0',
        'mk_exam_pass': 'INTEGER DEFAULT 0',
        'pz_exam_pass': 'INTEGER DEFAULT 0',
        'sn_exam_pass': 'INTEGER DEFAULT 0',
        'sb_exam_pass': 'INTEGER DEFAULT 0',
        'rn_exam_pass': 'INTEGER DEFAULT 0',
        'bc_exam_pass': 'INTEGER DEFAULT 0',
        'pj_exam_pass': 'INTEGER DEFAULT 0',
        'lt_exam_pass': 'INTEGER DEFAULT 0',
        'pv_exam_pass': 'INTEGER DEFAULT 0',
        'ki_exam_pass': 'INTEGER DEFAULT 0',
        'lr_exam_pass': 'INTEGER DEFAULT 0',
        'ms_exam_pass': 'INTEGER DEFAULT 0',
        'sd_exam_pass': 'INTEGER DEFAULT 0',
        'dd_exam_pass': 'INTEGER DEFAULT 0'
    }

    try:
        cursor.execute("PRAGMA table_info('Users')")
        existing_columns = [column[1] for column in cursor.fetchall()]

        for column_name, column_definition in required_columns.items():
            if column_name not in existing_columns:
                cursor.execute(f"ALTER TABLE Users ADD COLUMN {column_name} {column_definition}")
                print(f"Столбец {column_name} успешно добавлен!")

        connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка обновления таблицы: {e}")
    finally:
        connection.close()

def remove_duplicates():
    """
    Удаляет дублирующиеся строки из таблицы Users, оставляя только одну запись на каждую группу tg_id.
    """
    connection = sqlite3.connect(path_to_db)
    cursor = connection.cursor()

    try:
        # Удаление дубликатов, оставляя строки с минимальным ROWID
        cursor.execute('''
            DELETE FROM Users
            WHERE ROWID NOT IN (
                SELECT MIN(ROWID)
                FROM Users
                GROUP BY tg_id
            )
        ''')
        connection.commit()
        print("Дублирующие строки успешно удалены.")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении дубликатов: {e}")
    finally:
        connection.close()