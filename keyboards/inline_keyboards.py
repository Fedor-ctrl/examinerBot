from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardBuilder



def send_predstavlenie_kompanii():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Представление компании Good-Avto',
                             url='https://disk.yandex.ru/i/riwft4fi3EjetA',
                             callback_data='watch_video'),
        InlineKeyboardButton(text='Вернуться в меню',
                             callback_data='get_me_to_menu')
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def osmotr_avto():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Осмотр автомобиля',
                             url='https://disk.yandex.ru/i/Ab8ZqatvIkOpGA')
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def ustroystvo_avto():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Общее устройство автомобиля',
                             url='https://disk.yandex.ru/i/lPXoKCTEcMxePA')
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def usr_vo_avto():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Виды ДВС',
                             url='https://disk.yandex.ru/i/-ARy9zPYEb0ZZA'),
        InlineKeyboardButton(text='Впускная система',
                             url='https://disk.yandex.ru/i/kv8JXuk9bGUYgQ'),
        InlineKeyboardButton(text='Газораспределилтельный механизм',
                             url='https://disk.yandex.ru/i/JdH3kRwIPQDlrQ'),
        InlineKeyboardButton(text='Гидравлический конпенсатор',
                             url='https://disk.yandex.ru/i/vk4lbJeyyC2CIw'),
        InlineKeyboardButton(text='КШМ',
                             url='https://disk.yandex.ru/i/fdlqND6mRUGSyA'),
        InlineKeyboardButton(text='Рабочий цикл четырёхтактного бензинового двигателя',
                             url='https://disk.yandex.ru/i/urW26X108113iA'),
        InlineKeyboardButton(text='Типы и виды ГРМ',
                             url='https://disk.yandex.ru/i/tRnCEVve-jWU3g'),
        InlineKeyboardButton(text='Устройство ДВС. Часть 1',
                             url='https://disk.yandex.ru/i/lqxZYvfxqr8qxw'),
        InlineKeyboardButton(text='Устройство ДВС. Часть 2',
                             url='https://disk.yandex.ru/i/uaS6aoB65X5R9w'),
        InlineKeyboardButton(text='Устройство ДВС. Часть 3',
                             url='https://disk.yandex.ru/i/XU519tNDXo0HcQ'),
        InlineKeyboardButton(text='Вернуться в меню',
                             callback_data='get_me_to_menu'),
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def i_did_watch_the_video():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Да',
                             callback_data='i_did_watch_the_video')
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def pravka_diskov_uroki():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Правка дисков. Часть 1", callback_data="pravka_diskov_1",),
        InlineKeyboardButton(text="Правка дисков. Часть 2", callback_data="pravka_diskov_2"),
        InlineKeyboardButton(text="Правка дисков. Часть 3", callback_data="pravka_diskov_3"),
        InlineKeyboardButton(text="Правка дисков. Часть 4", callback_data="pravka_diskov_4"),
        InlineKeyboardButton(text="Правка дисков. Часть 5", callback_data="pravka_diskov_5"),
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def pravki_zanovo_1():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="pravka_diskov_1")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def pravki_zanovo_2():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="pravka_diskov_2")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def pravki_zanovo_3():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="pravka_diskov_3")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def pravki_zanovo_4():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="pravka_diskov_4")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def pravki_zanovo_5():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="pravka_diskov_5")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def urok_po_pravkam_1():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="pravka_diskov_2")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def urok_po_pravkam_2():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="pravka_diskov_3")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def urok_po_pravkam_3():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="pravka_diskov_4")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def urok_po_pravkam_4():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="pravka_diskov_5")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def treningi():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Тренинг общения по шиномонтажу", callback_data="treningi")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def trening_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="treningi"),
            ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def oborudovanie():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Балансировочный станок', callback_data="balancirovka"),
        InlineKeyboardButton(text='Станок для правки дисков', callback_data="stanok_pravok"),
        InlineKeyboardButton(text='Шиномонтажный станок', callback_data="stanok_shinka")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def balancirovka_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="balancirovka")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def stanok_dl_pravok_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="stanok_pravok")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def stanok_dl_shinke_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="stanok_shinka")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def stanok_dl_pravok():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="stanok_pravok")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def stanok_dl_shinki():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="stanok_shinka")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def shinshik():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='История шин', callback_data="history"),
        InlineKeyboardButton(text='Испытания в лаборатории', callback_data="trials"),
        InlineKeyboardButton(text='Как делают шины. Производство и устройство', callback_data='proizvodstvo'),
        InlineKeyboardButton(text='Колёса - шины', callback_data="kolesaishini"),
        InlineKeyboardButton(text='Левые и правые шины', callback_data="leftandright"),
        InlineKeyboardButton(text='Маркировка шин. Вариант 1', callback_data="markirovkadiskov"),
        InlineKeyboardButton(text='Маркировка шин. Вариант 2', callback_data="markirovkashin"),
        InlineKeyboardButton(text='Шины STUDDED или STUDABLE', callback_data="studorstudd")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def proizvodstvo_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="proizvodstvo")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def proizvodstvo_shin():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Следующий урок', callback_data="kolesaishini")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def kolesaishini_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="kolesaishini")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def kolesa_shini():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Следующий урок', callback_data="leftandright")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def leftandright_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="leftandright")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def left_right():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Следующий урок', callback_data="markirovkashin")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def markirovka_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="markirovkashin")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def shinkadisk_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="shinkadisk")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def shinka_disk():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Следующий урок', callback_data="studorstudd")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def studorstudd_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="studorstudd")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def istoriya_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="history")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def ispitaniya_shin():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий курс", callback_data="trials")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def ispitaniya_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="trials")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def diski():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='В чем отличие литья от ковки', callback_data="litorkovka"),
        InlineKeyboardButton(text='Все параметры дисков', callback_data="parametrdisk"),
        InlineKeyboardButton(text='Кольца для литых дисков', callback_data="kolcadldiskov"),
        InlineKeyboardButton(text='Шинка диск', callback_data="shinkadisk")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def litorkovka_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="litorkovka")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def parametri_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="parametrdisk")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def kolca_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="kolcadldiskov")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def markirovkads_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Пройти урок заново', callback_data="markirovkadiskov")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def remont_i_shinka():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Ремонт колеса-порез', callback_data="porez"),
        InlineKeyboardButton(text='Снятие и установка колеса на автомобиль', callback_data="snyatie"),
        InlineKeyboardButton(text='Сборка и разборка на шиномонтажном станке', callback_data="sborka"),
        InlineKeyboardButton(text='Ремонт прокола бескамерного колеса', callback_data="remont"),
        InlineKeyboardButton(text='Балансировка колеса', callback_data="balance"),
        InlineKeyboardButton(text='Допродажи',callback_data="prodaja")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def porez_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="porez")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def snyatie_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="snyatie")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def sborka_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="sborka")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def remont_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="remont")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def balance_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="balance")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def prodaja_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="prodaja")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def sborkakol_zanovo():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Пройти урок заново", callback_data="sborka")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def snyatie_i_ustanovka():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="snyatie")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def sborka_kolesa():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="sborka")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def remont_kolesa():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="balance")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def doprodaja():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="doprodaja")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def beskamernogo_kolesa():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="remont")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def parametri_diskov():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="parametrdisk")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def kolca():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="kolcadldiskov")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def markirovka():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Следующий урок", callback_data="markirovkadiskov")
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def sysvpr():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text="Система впрыска", url='https://disk.yandex.ru/i/ABLJQW-wF2FeGg')
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

def graphics_to_continue():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Подготовка фитинга',
                             callback_data='ac_fit_repair1',
                             url='https://drive.google.com/file/d/1NogaCLvGz6sVStTUu5_B3LIm_yavWGze/view?usp=sharing'),
        InlineKeyboardButton(text='Пайка фитинга к трубке',
                             callback_data='ac_fit_repair2',
                             url='https://drive.google.com/file/d/1NmceOQPeWG4Td9swpjn34OgVwt5Dob8L/view?usp=sharing'),
        InlineKeyboardButton(text='Вальцовка шланга',
                             callback_data='ac_fit_repair3',
                             url='https://drive.google.com/file/d/1NmbG3xsEbQm05VsoQoKqdJzbAuUFlT8F/view?usp=sharing'),
        InlineKeyboardButton(text='Как правильно хранить припой',
                             callback_data='ac_fit_repair4',
                             url='https://drive.google.com/file/d/1NlTUmZMxolauLSaNqHFnr5M-AXtEuY9l/view?usp=sharing'),
        InlineKeyboardButton(text='Как правильно подготовить трубку к пайке',
                             callback_data='ac_fit_repair5',
                             url='https://drive.google.com/file/d/1NkAjnr1ai-NhEw_ug0qPpg9__8GTqWVS/view?usp=sharing'),
        InlineKeyboardButton(text='Как правильно заправлять станцию фреоном',
                             callback_data='ac_fit_repair6',
                             url='https://drive.google.com/file/d/1NjroahmXIZz3FO2C0Q6T8ivhoizSEC_n/view?usp=sharing'),
        InlineKeyboardButton(text='Как правильно вставлять ерш в шланг',
                             callback_data='ac_fit_repair7',
                             url='https://drive.google.com/file/d/1Ni685gYyO04axXrc79YCvO_hZYLfTgSz/view?usp=sharing'),
        InlineKeyboardButton(text='Перейти к тестированию!',
                             callback_data='get_me_to_ac_exam')
    ]
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()

# Здесь клавиатуры для ответов на тест по кондею:
def ac_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-1-a'),
        InlineKeyboardButton(text='b', callback_data='ac-1-b'),
        InlineKeyboardButton(text='c', callback_data='ac-1-c'),
        InlineKeyboardButton(text='d', callback_data='ac-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-2-a'),
        InlineKeyboardButton(text='b', callback_data='ac-2-b'),
        InlineKeyboardButton(text='c', callback_data='ac-2-c'),
        InlineKeyboardButton(text='d', callback_data='ac-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-3-a'),
        InlineKeyboardButton(text='b', callback_data='ac-3-b'),
        InlineKeyboardButton(text='c', callback_data='ac-3-c'),
        InlineKeyboardButton(text='d', callback_data='ac-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-4-a'),
        InlineKeyboardButton(text='b', callback_data='ac-4-b'),
        InlineKeyboardButton(text='c', callback_data='ac-4-c'),
        InlineKeyboardButton(text='d', callback_data='ac-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-5-a'),
        InlineKeyboardButton(text='b', callback_data='ac-5-b'),
        InlineKeyboardButton(text='c', callback_data='ac-5-c'),
        InlineKeyboardButton(text='d', callback_data='ac-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-6-a'),
        InlineKeyboardButton(text='b', callback_data='ac-6-b'),
        InlineKeyboardButton(text='c', callback_data='ac-6-c'),
        InlineKeyboardButton(text='d', callback_data='ac-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-7-a'),
        InlineKeyboardButton(text='b', callback_data='ac-7-b'),
        InlineKeyboardButton(text='c', callback_data='ac-7-c'),
        InlineKeyboardButton(text='d', callback_data='ac-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-8-a'),
        InlineKeyboardButton(text='b', callback_data='ac-8-b'),
        InlineKeyboardButton(text='c', callback_data='ac-8-c'),
        InlineKeyboardButton(text='d', callback_data='ac-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-9-a'),
        InlineKeyboardButton(text='b', callback_data='ac-9-b'),
        InlineKeyboardButton(text='c', callback_data='ac-9-c'),
        InlineKeyboardButton(text='d', callback_data='ac-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-10-a'),
        InlineKeyboardButton(text='b', callback_data='ac-10-b'),
        InlineKeyboardButton(text='c', callback_data='ac-10-c'),
        InlineKeyboardButton(text='d', callback_data='ac-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-11-a'),
        InlineKeyboardButton(text='b', callback_data='ac-11-b'),
        InlineKeyboardButton(text='c', callback_data='ac-11-c'),
        InlineKeyboardButton(text='d', callback_data='ac-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-12-a'),
        InlineKeyboardButton(text='b', callback_data='ac-12-b'),
        InlineKeyboardButton(text='c', callback_data='ac-12-c'),
        InlineKeyboardButton(text='d', callback_data='ac-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-13-a'),
        InlineKeyboardButton(text='b', callback_data='ac-13-b'),
        InlineKeyboardButton(text='c', callback_data='ac-13-c'),
        InlineKeyboardButton(text='d', callback_data='ac-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-14-a'),
        InlineKeyboardButton(text='b', callback_data='ac-14-b'),
        InlineKeyboardButton(text='c', callback_data='ac-14-c'),
        InlineKeyboardButton(text='d', callback_data='ac-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-15-a'),
        InlineKeyboardButton(text='b', callback_data='ac-15-b'),
        InlineKeyboardButton(text='c', callback_data='ac-15-c'),
        InlineKeyboardButton(text='d', callback_data='ac-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-16-a'),
        InlineKeyboardButton(text='b', callback_data='ac-16-b'),
        InlineKeyboardButton(text='c', callback_data='ac-16-c'),
        InlineKeyboardButton(text='d', callback_data='ac-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-17-a'),
        InlineKeyboardButton(text='b', callback_data='ac-17-b'),
        InlineKeyboardButton(text='c', callback_data='ac-17-c'),
        InlineKeyboardButton(text='d', callback_data='ac-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-18-a'),
        InlineKeyboardButton(text='b', callback_data='ac-18-b'),
        InlineKeyboardButton(text='c', callback_data='ac-18-c'),
        InlineKeyboardButton(text='d', callback_data='ac-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-19-a'),
        InlineKeyboardButton(text='b', callback_data='ac-19-b'),
        InlineKeyboardButton(text='c', callback_data='ac-19-c'),
        InlineKeyboardButton(text='d', callback_data='ac-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ac_20_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ac-20-a'),
        InlineKeyboardButton(text='b', callback_data='ac-20-b'),
        InlineKeyboardButton(text='c', callback_data='ac-20-c'),
        InlineKeyboardButton(text='d', callback_data='ac-20-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-1-a'),
        InlineKeyboardButton(text='b', callback_data='pr-1-b'),
        InlineKeyboardButton(text='c', callback_data='pr-1-c'),
        InlineKeyboardButton(text='d', callback_data='pr-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-2-a'),
        InlineKeyboardButton(text='b', callback_data='pr-2-b'),
        InlineKeyboardButton(text='c', callback_data='pr-2-c'),
        InlineKeyboardButton(text='d', callback_data='pr-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-3-a'),
        InlineKeyboardButton(text='b', callback_data='pr-3-b'),
        InlineKeyboardButton(text='c', callback_data='pr-3-c'),
        InlineKeyboardButton(text='d', callback_data='pr-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-4-a'),
        InlineKeyboardButton(text='b', callback_data='pr-4-b'),
        InlineKeyboardButton(text='c', callback_data='pr-4-c'),
        InlineKeyboardButton(text='d', callback_data='pr-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-5-a'),
        InlineKeyboardButton(text='b', callback_data='pr-5-b'),
        InlineKeyboardButton(text='c', callback_data='pr-5-c'),
        InlineKeyboardButton(text='d', callback_data='pr-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-6-a'),
        InlineKeyboardButton(text='b', callback_data='pr-6-b'),
        InlineKeyboardButton(text='c', callback_data='pr-6-c'),
        InlineKeyboardButton(text='d', callback_data='pr-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-7-a'),
        InlineKeyboardButton(text='b', callback_data='pr-7-b'),
        InlineKeyboardButton(text='c', callback_data='pr-7-c'),
        InlineKeyboardButton(text='d', callback_data='pr-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-8-a'),
        InlineKeyboardButton(text='b', callback_data='pr-8-b'),
        InlineKeyboardButton(text='c', callback_data='pr-8-c'),
        InlineKeyboardButton(text='d', callback_data='pr-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-9-a'),
        InlineKeyboardButton(text='b', callback_data='pr-9-b'),
        InlineKeyboardButton(text='c', callback_data='pr-9-c'),
        InlineKeyboardButton(text='d', callback_data='pr-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-10-a'),
        InlineKeyboardButton(text='b', callback_data='pr-10-b'),
        InlineKeyboardButton(text='c', callback_data='pr-10-c'),
        InlineKeyboardButton(text='d', callback_data='pr-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-11-a'),
        InlineKeyboardButton(text='b', callback_data='pr-11-b'),
        InlineKeyboardButton(text='c', callback_data='pr-11-c'),
        InlineKeyboardButton(text='d', callback_data='pr-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-12-a'),
        InlineKeyboardButton(text='b', callback_data='pr-12-b'),
        InlineKeyboardButton(text='c', callback_data='pr-12-c'),
        InlineKeyboardButton(text='d', callback_data='pr-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-13-a'),
        InlineKeyboardButton(text='b', callback_data='pr-13-b'),
        InlineKeyboardButton(text='c', callback_data='pr-13-c'),
        InlineKeyboardButton(text='d', callback_data='pr-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-14-a'),
        InlineKeyboardButton(text='b', callback_data='pr-14-b'),
        InlineKeyboardButton(text='c', callback_data='pr-14-c'),
        InlineKeyboardButton(text='d', callback_data='pr-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-15-a'),
        InlineKeyboardButton(text='b', callback_data='pr-15-b'),
        InlineKeyboardButton(text='c', callback_data='pr-15-c'),
        InlineKeyboardButton(text='d', callback_data='pr-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-16-a'),
        InlineKeyboardButton(text='b', callback_data='pr-16-b'),
        InlineKeyboardButton(text='c', callback_data='pr-16-c'),
        InlineKeyboardButton(text='d', callback_data='pr-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-17-a'),
        InlineKeyboardButton(text='b', callback_data='pr-17-b'),
        InlineKeyboardButton(text='c', callback_data='pr-17-c'),
        InlineKeyboardButton(text='d', callback_data='pr-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-18-a'),
        InlineKeyboardButton(text='b', callback_data='pr-18-b'),
        InlineKeyboardButton(text='c', callback_data='pr-18-c'),
        InlineKeyboardButton(text='d', callback_data='pr-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-19-a'),
        InlineKeyboardButton(text='b', callback_data='pr-19-b'),
        InlineKeyboardButton(text='c', callback_data='pr-19-c'),
        InlineKeyboardButton(text='d', callback_data='pr-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_20_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr-20-a'),
        InlineKeyboardButton(text='b', callback_data='pr-20-b'),
        InlineKeyboardButton(text='c', callback_data='pr-20-c'),
        InlineKeyboardButton(text='d', callback_data='pr-20-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def say_hello_electica():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Курс по электрике', callback_data='kurs_vtoroy')
           ]
    kb_builder.row(*buttons, width=6)
    return kb_builder.as_markup()

def get_multiple_buttons(buttons: list[tuple]) -> InlineKeyboardMarkup:
    """
    Создаёт инлайн-клавиатуру с несколькими кнопками.
    """
    keyboard = InlineKeyboardMarkup()
    for text, callback_data in buttons:
        keyboard.add(InlineKeyboardButton(text=text, callback_data=callback_data))
    return keyboard

def pr_1_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_1-1-a'),
        InlineKeyboardButton(text='b', callback_data='pr_1-1-b'),
        InlineKeyboardButton(text='c', callback_data='pr_1-1-c'),
        InlineKeyboardButton(text='d', callback_data='pr_1-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_1_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_1-2-a'),
        InlineKeyboardButton(text='b', callback_data='pr_1-2-b'),
        InlineKeyboardButton(text='c', callback_data='pr_1-2-c'),
        InlineKeyboardButton(text='d', callback_data='pr_1-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_1_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_1-3-a'),
        InlineKeyboardButton(text='b', callback_data='pr_1-3-b'),
        InlineKeyboardButton(text='c', callback_data='pr_1-3-c'),
        InlineKeyboardButton(text='d', callback_data='pr_1-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_1_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_1-4-a'),
        InlineKeyboardButton(text='b', callback_data='pr_1-4-b'),
        InlineKeyboardButton(text='c', callback_data='pr_1-4-c'),
        InlineKeyboardButton(text='d', callback_data='pr_1-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_1_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_1-5-a'),
        InlineKeyboardButton(text='b', callback_data='pr_1-5-b'),
        InlineKeyboardButton(text='c', callback_data='pr_1-5-c'),
        InlineKeyboardButton(text='d', callback_data='pr_1-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_2_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_2-1-a'),
        InlineKeyboardButton(text='b', callback_data='pr_2-1-b'),
        InlineKeyboardButton(text='c', callback_data='pr_2-1-c'),
        InlineKeyboardButton(text='d', callback_data='pr_2-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_2_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_2-2-a'),
        InlineKeyboardButton(text='b', callback_data='pr_2-2-b'),
        InlineKeyboardButton(text='c', callback_data='pr_2-2-c'),
        InlineKeyboardButton(text='d', callback_data='pr_2-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_2_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_2-3-a'),
        InlineKeyboardButton(text='b', callback_data='pr_2-3-b'),
        InlineKeyboardButton(text='c', callback_data='pr_2-3-c'),
        InlineKeyboardButton(text='d', callback_data='pr_2-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_2_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_2-4-a'),
        InlineKeyboardButton(text='b', callback_data='pr_2-4-b'),
        InlineKeyboardButton(text='c', callback_data='pr_2-4-c'),
        InlineKeyboardButton(text='d', callback_data='pr_2-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_2_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_2-5-a'),
        InlineKeyboardButton(text='b', callback_data='pr_2-5-b'),
        InlineKeyboardButton(text='c', callback_data='pr_2-5-c'),
        InlineKeyboardButton(text='d', callback_data='pr_2-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_2_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_2-6-a'),
        InlineKeyboardButton(text='b', callback_data='pr_2-6-b'),
        InlineKeyboardButton(text='c', callback_data='pr_2-6-c'),
        InlineKeyboardButton(text='d', callback_data='pr_2-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_2_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_2-7-a'),
        InlineKeyboardButton(text='b', callback_data='pr_2-7-b'),
        InlineKeyboardButton(text='c', callback_data='pr_2-7-c'),
        InlineKeyboardButton(text='d', callback_data='pr_2-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_3_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-1-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-1-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-1-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_3_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-2-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-2-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-2-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_3_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-3-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-3-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-3-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_3_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-4-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-4-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-4-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_3_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-5-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-5-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-5-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_3_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-6-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-6-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-6-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_3_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-7-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-7-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-7-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_3_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-8-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-8-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-8-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_3_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-9-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-9-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-9-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_3_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-10-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-10-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-10-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_3_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-11-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-11-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-11-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_3_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-12-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-12-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-12-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_3_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_3-13-a'),
        InlineKeyboardButton(text='b', callback_data='pr_3-13-b'),
        InlineKeyboardButton(text='c', callback_data='pr_3-13-c'),
        InlineKeyboardButton(text='d', callback_data='pr_3-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_4_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_4-1-a'),
        InlineKeyboardButton(text='b', callback_data='pr_4-1-b'),
        InlineKeyboardButton(text='c', callback_data='pr_4-1-c'),
        InlineKeyboardButton(text='d', callback_data='pr_4-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_4_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_4-2-a'),
        InlineKeyboardButton(text='b', callback_data='pr_4-2-b'),
        InlineKeyboardButton(text='c', callback_data='pr_4-2-c'),
        InlineKeyboardButton(text='d', callback_data='pr_4-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_4_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_4-3-a'),
        InlineKeyboardButton(text='b', callback_data='pr_4-3-b'),
        InlineKeyboardButton(text='c', callback_data='pr_4-3-c'),
        InlineKeyboardButton(text='d', callback_data='pr_4-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_4_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_4-4-a'),
        InlineKeyboardButton(text='b', callback_data='pr_4-4-b'),
        InlineKeyboardButton(text='c', callback_data='pr_4-4-c'),
        InlineKeyboardButton(text='d', callback_data='pr_4-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_4_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_4-5-a'),
        InlineKeyboardButton(text='b', callback_data='pr_4-5-b'),
        InlineKeyboardButton(text='c', callback_data='pr_4-5-c'),
        InlineKeyboardButton(text='d', callback_data='pr_4-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_4_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_4-6-a'),
        InlineKeyboardButton(text='b', callback_data='pr_4-6-b'),
        InlineKeyboardButton(text='c', callback_data='pr_4-6-c'),
        InlineKeyboardButton(text='d', callback_data='pr_4-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_4_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_4-7-a'),
        InlineKeyboardButton(text='b', callback_data='pr_4-7-b'),
        InlineKeyboardButton(text='c', callback_data='pr_4-7-c'),
        InlineKeyboardButton(text='d', callback_data='pr_4-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_4_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_4-8-a'),
        InlineKeyboardButton(text='b', callback_data='pr_4-8-b'),
        InlineKeyboardButton(text='c', callback_data='pr_4-8-c'),
        InlineKeyboardButton(text='d', callback_data='pr_4-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def tr_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-1-a'),
        InlineKeyboardButton(text='b', callback_data='tr-1-b'),
        InlineKeyboardButton(text='c', callback_data='tr-1-c'),
        InlineKeyboardButton(text='d', callback_data='tr-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-2-a'),
        InlineKeyboardButton(text='b', callback_data='tr-2-b'),
        InlineKeyboardButton(text='c', callback_data='tr-2-c'),
        InlineKeyboardButton(text='d', callback_data='tr-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-3-a'),
        InlineKeyboardButton(text='b', callback_data='tr-3-b'),
        InlineKeyboardButton(text='c', callback_data='tr-3-c'),
        InlineKeyboardButton(text='d', callback_data='tr-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-4-a'),
        InlineKeyboardButton(text='b', callback_data='tr-4-b'),
        InlineKeyboardButton(text='c', callback_data='tr-4-c'),
        InlineKeyboardButton(text='d', callback_data='tr-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-5-a'),
        InlineKeyboardButton(text='b', callback_data='tr-5-b'),
        InlineKeyboardButton(text='c', callback_data='tr-5-c'),
        InlineKeyboardButton(text='d', callback_data='tr-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-6-a'),
        InlineKeyboardButton(text='b', callback_data='tr-6-b'),
        InlineKeyboardButton(text='c', callback_data='tr-6-c'),
        InlineKeyboardButton(text='d', callback_data='tr-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-7-a'),
        InlineKeyboardButton(text='b', callback_data='tr-7-b'),
        InlineKeyboardButton(text='c', callback_data='tr-7-c'),
        InlineKeyboardButton(text='d', callback_data='tr-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-8-a'),
        InlineKeyboardButton(text='b', callback_data='tr-8-b'),
        InlineKeyboardButton(text='c', callback_data='tr-8-c'),
        InlineKeyboardButton(text='d', callback_data='tr-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-9-a'),
        InlineKeyboardButton(text='b', callback_data='tr-9-b'),
        InlineKeyboardButton(text='c', callback_data='tr-9-c'),
        InlineKeyboardButton(text='d', callback_data='tr-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-10-a'),
        InlineKeyboardButton(text='b', callback_data='tr-10-b'),
        InlineKeyboardButton(text='c', callback_data='tr-10-c'),
        InlineKeyboardButton(text='d', callback_data='tr-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-11-a'),
        InlineKeyboardButton(text='b', callback_data='tr-11-b'),
        InlineKeyboardButton(text='c', callback_data='tr-11-c'),
        InlineKeyboardButton(text='d', callback_data='tr-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-12-a'),
        InlineKeyboardButton(text='b', callback_data='tr-12-b'),
        InlineKeyboardButton(text='c', callback_data='tr-12-c'),
        InlineKeyboardButton(text='d', callback_data='tr-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-13-a'),
        InlineKeyboardButton(text='b', callback_data='tr-13-b'),
        InlineKeyboardButton(text='c', callback_data='tr-13-c'),
        InlineKeyboardButton(text='d', callback_data='tr-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-14-a'),
        InlineKeyboardButton(text='b', callback_data='tr-14-b'),
        InlineKeyboardButton(text='c', callback_data='tr-14-c'),
        InlineKeyboardButton(text='d', callback_data='tr-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-15-a'),
        InlineKeyboardButton(text='b', callback_data='tr-15-b'),
        InlineKeyboardButton(text='c', callback_data='tr-15-c'),
        InlineKeyboardButton(text='d', callback_data='tr-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-16-a'),
        InlineKeyboardButton(text='b', callback_data='tr-16-b'),
        InlineKeyboardButton(text='c', callback_data='tr-16-c'),
        InlineKeyboardButton(text='d', callback_data='tr-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-17-a'),
        InlineKeyboardButton(text='b', callback_data='tr-17-b'),
        InlineKeyboardButton(text='c', callback_data='tr-17-c'),
        InlineKeyboardButton(text='d', callback_data='tr-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-18-a'),
        InlineKeyboardButton(text='b', callback_data='tr-18-b'),
        InlineKeyboardButton(text='c', callback_data='tr-18-c'),
        InlineKeyboardButton(text='d', callback_data='tr-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-19-a'),
        InlineKeyboardButton(text='b', callback_data='tr-19-b'),
        InlineKeyboardButton(text='c', callback_data='tr-19-c'),
        InlineKeyboardButton(text='d', callback_data='tr-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def tr_20_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='tr-20-a'),
        InlineKeyboardButton(text='b', callback_data='tr-20-b'),
        InlineKeyboardButton(text='c', callback_data='tr-20-c'),
        InlineKeyboardButton(text='d', callback_data='tr-20-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ob_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-1-a'),
        InlineKeyboardButton(text='b', callback_data='ob-1-b'),
        InlineKeyboardButton(text='c', callback_data='ob-1-c'),
        InlineKeyboardButton(text='d', callback_data='ob-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-2-a'),
        InlineKeyboardButton(text='b', callback_data='ob-2-b'),
        InlineKeyboardButton(text='c', callback_data='ob-2-c'),
        InlineKeyboardButton(text='d', callback_data='ob-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ob_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-3-a'),
        InlineKeyboardButton(text='b', callback_data='ob-3-b'),
        InlineKeyboardButton(text='c', callback_data='ob-3-c'),
        InlineKeyboardButton(text='d', callback_data='ob-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-4-a'),
        InlineKeyboardButton(text='b', callback_data='ob-4-b'),
        InlineKeyboardButton(text='c', callback_data='ob-4-c'),
        InlineKeyboardButton(text='d', callback_data='ob-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-5-a'),
        InlineKeyboardButton(text='b', callback_data='ob-5-b'),
        InlineKeyboardButton(text='c', callback_data='ob-5-c'),
        InlineKeyboardButton(text='d', callback_data='ob-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-6-a'),
        InlineKeyboardButton(text='b', callback_data='ob-6-b'),
        InlineKeyboardButton(text='c', callback_data='ob-6-c'),
        InlineKeyboardButton(text='d', callback_data='ob-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-7-a'),
        InlineKeyboardButton(text='b', callback_data='ob-7-b'),
        InlineKeyboardButton(text='c', callback_data='ob-7-c'),
        InlineKeyboardButton(text='d', callback_data='ob-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-8-a'),
        InlineKeyboardButton(text='b', callback_data='ob-8-b'),
        InlineKeyboardButton(text='c', callback_data='ob-8-c'),
        InlineKeyboardButton(text='d', callback_data='ob-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-9-a'),
        InlineKeyboardButton(text='b', callback_data='ob-9-b'),
        InlineKeyboardButton(text='c', callback_data='ob-9-c'),
        InlineKeyboardButton(text='d', callback_data='ob-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-10-a'),
        InlineKeyboardButton(text='b', callback_data='ob-10-b'),
        InlineKeyboardButton(text='c', callback_data='ob-10-c'),
        InlineKeyboardButton(text='d', callback_data='ob-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-11-a'),
        InlineKeyboardButton(text='b', callback_data='ob-11-b'),
        InlineKeyboardButton(text='c', callback_data='ob-11-c'),
        InlineKeyboardButton(text='d', callback_data='ob-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_12_answer():
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-12-a'),
        InlineKeyboardButton(text='b', callback_data='ob-12-b'),
        InlineKeyboardButton(text='c', callback_data='ob-12-c'),
        InlineKeyboardButton(text='d', callback_data='ob-12-d')
    ]
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-13-a'),
        InlineKeyboardButton(text='b', callback_data='ob-13-b'),
        InlineKeyboardButton(text='c', callback_data='ob-13-c'),
        InlineKeyboardButton(text='d', callback_data='ob-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-14-a'),
        InlineKeyboardButton(text='b', callback_data='ob-14-b'),
        InlineKeyboardButton(text='c', callback_data='ob-14-c'),
        InlineKeyboardButton(text='d', callback_data='ob-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-15-a'),
        InlineKeyboardButton(text='b', callback_data='ob-15-b'),
        InlineKeyboardButton(text='c', callback_data='ob-15-c'),
        InlineKeyboardButton(text='d', callback_data='ob-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-16-a'),
        InlineKeyboardButton(text='b', callback_data='ob-16-b'),
        InlineKeyboardButton(text='c', callback_data='ob-16-c'),
        InlineKeyboardButton(text='d', callback_data='ob-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-17-a'),
        InlineKeyboardButton(text='b', callback_data='ob-17-b'),
        InlineKeyboardButton(text='c', callback_data='ob-17-c'),
        InlineKeyboardButton(text='d', callback_data='ob-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ob_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ob-18-a'),
        InlineKeyboardButton(text='b', callback_data='ob-18-b'),
        InlineKeyboardButton(text='c', callback_data='ob-18-c'),
        InlineKeyboardButton(text='d', callback_data='ob-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def st_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-1-a'),
        InlineKeyboardButton(text='b', callback_data='st-1-b'),
        InlineKeyboardButton(text='c', callback_data='st-1-c'),
        InlineKeyboardButton(text='d', callback_data='st-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-2-a'),
        InlineKeyboardButton(text='b', callback_data='st-2-b'),
        InlineKeyboardButton(text='c', callback_data='st-2-c'),
        InlineKeyboardButton(text='d', callback_data='st-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def st_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-3-a'),
        InlineKeyboardButton(text='b', callback_data='st-3-b'),
        InlineKeyboardButton(text='c', callback_data='st-3-c'),
        InlineKeyboardButton(text='d', callback_data='st-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-4-a'),
        InlineKeyboardButton(text='b', callback_data='st-4-b'),
        InlineKeyboardButton(text='c', callback_data='st-4-c'),
        InlineKeyboardButton(text='d', callback_data='st-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-5-a'),
        InlineKeyboardButton(text='b', callback_data='st-5-b'),
        InlineKeyboardButton(text='c', callback_data='st-5-c'),
        InlineKeyboardButton(text='d', callback_data='st-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-6-a'),
        InlineKeyboardButton(text='b', callback_data='st-6-b'),
        InlineKeyboardButton(text='c', callback_data='st-6-c'),
        InlineKeyboardButton(text='d', callback_data='st-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-7-a'),
        InlineKeyboardButton(text='b', callback_data='st-7-b'),
        InlineKeyboardButton(text='c', callback_data='st-7-c'),
        InlineKeyboardButton(text='d', callback_data='st-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-8-a'),
        InlineKeyboardButton(text='b', callback_data='st-8-b'),
        InlineKeyboardButton(text='c', callback_data='st-8-c'),
        InlineKeyboardButton(text='d', callback_data='st-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-9-a'),
        InlineKeyboardButton(text='b', callback_data='st-9-b'),
        InlineKeyboardButton(text='c', callback_data='st-9-c'),
        InlineKeyboardButton(text='d', callback_data='st-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-10-a'),
        InlineKeyboardButton(text='b', callback_data='st-10-b'),
        InlineKeyboardButton(text='c', callback_data='st-10-c'),
        InlineKeyboardButton(text='d', callback_data='st-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-11-a'),
        InlineKeyboardButton(text='b', callback_data='st-11-b'),
        InlineKeyboardButton(text='c', callback_data='st-11-c'),
        InlineKeyboardButton(text='d', callback_data='st-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_12_answer():
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-12-a'),
        InlineKeyboardButton(text='b', callback_data='st-12-b'),
        InlineKeyboardButton(text='c', callback_data='st-12-c'),
        InlineKeyboardButton(text='d', callback_data='st-12-d')
    ]
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-13-a'),
        InlineKeyboardButton(text='b', callback_data='st-13-b'),
        InlineKeyboardButton(text='c', callback_data='st-13-c'),
        InlineKeyboardButton(text='d', callback_data='st-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-14-a'),
        InlineKeyboardButton(text='b', callback_data='st-14-b'),
        InlineKeyboardButton(text='c', callback_data='st-14-c'),
        InlineKeyboardButton(text='d', callback_data='st-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-15-a'),
        InlineKeyboardButton(text='b', callback_data='st-15-b'),
        InlineKeyboardButton(text='c', callback_data='st-15-c'),
        InlineKeyboardButton(text='d', callback_data='st-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-16-a'),
        InlineKeyboardButton(text='b', callback_data='st-16-b'),
        InlineKeyboardButton(text='c', callback_data='st-16-c'),
        InlineKeyboardButton(text='d', callback_data='st-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-17-a'),
        InlineKeyboardButton(text='b', callback_data='st-17-b'),
        InlineKeyboardButton(text='c', callback_data='st-17-c'),
        InlineKeyboardButton(text='d', callback_data='st-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-18-a'),
        InlineKeyboardButton(text='b', callback_data='st-18-b'),
        InlineKeyboardButton(text='c', callback_data='st-18-c'),
        InlineKeyboardButton(text='d', callback_data='st-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def st_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st-19-a'),
        InlineKeyboardButton(text='b', callback_data='st-19-b'),
        InlineKeyboardButton(text='c', callback_data='st-19-c'),
        InlineKeyboardButton(text='d', callback_data='st-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def st_pr_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-1-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-1-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-1-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-2-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-2-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-2-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def st_pr_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-3-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-3-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-3-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-4-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-4-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-4-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-5-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-5-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-5-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-6-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-6-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-6-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-7-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-7-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-7-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-8-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-8-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-8-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-9-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-9-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-9-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-10-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-10-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-10-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-11-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-11-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-11-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_12_answer():
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-12-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-12-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-12-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-12-d')
    ]
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-13-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-13-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-13-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def st_pr_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='st_pr-14-a'),
        InlineKeyboardButton(text='b', callback_data='st_pr-14-b'),
        InlineKeyboardButton(text='c', callback_data='st_pr-14-c'),
        InlineKeyboardButton(text='d', callback_data='st_pr-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def id_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='id-1-a'),
        InlineKeyboardButton(text='b', callback_data='id-1-b'),
        InlineKeyboardButton(text='c', callback_data='id-1-c'),
        InlineKeyboardButton(text='d', callback_data='id-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def id_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='id-2-a'),
        InlineKeyboardButton(text='b', callback_data='id-2-b'),
        InlineKeyboardButton(text='c', callback_data='id-2-c'),
        InlineKeyboardButton(text='d', callback_data='id-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def id_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='id-3-a'),
        InlineKeyboardButton(text='b', callback_data='id-3-b'),
        InlineKeyboardButton(text='c', callback_data='id-3-c'),
        InlineKeyboardButton(text='d', callback_data='id-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def id_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='id-4-a'),
        InlineKeyboardButton(text='b', callback_data='id-4-b'),
        InlineKeyboardButton(text='c', callback_data='id-4-c'),
        InlineKeyboardButton(text='d', callback_data='id-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def id_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='id-5-a'),
        InlineKeyboardButton(text='b', callback_data='id-5-b'),
        InlineKeyboardButton(text='c', callback_data='id-5-c'),
        InlineKeyboardButton(text='d', callback_data='id-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def id_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='id-6-a'),
        InlineKeyboardButton(text='b', callback_data='id-6-b'),
        InlineKeyboardButton(text='c', callback_data='id-6-c'),
        InlineKeyboardButton(text='d', callback_data='id-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def id_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='id-7-a'),
        InlineKeyboardButton(text='b', callback_data='id-7-b'),
        InlineKeyboardButton(text='c', callback_data='id-7-c'),
        InlineKeyboardButton(text='d', callback_data='id-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def id_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='id-8-a'),
        InlineKeyboardButton(text='b', callback_data='id-8-b'),
        InlineKeyboardButton(text='c', callback_data='id-8-c'),
        InlineKeyboardButton(text='d', callback_data='id-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def id_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='id-9-a'),
        InlineKeyboardButton(text='b', callback_data='id-9-b'),
        InlineKeyboardButton(text='c', callback_data='id-9-c'),
        InlineKeyboardButton(text='d', callback_data='id-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def id_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='id-10-a'),
        InlineKeyboardButton(text='b', callback_data='id-10-b'),
        InlineKeyboardButton(text='c', callback_data='id-10-c'),
        InlineKeyboardButton(text='d', callback_data='id-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def is_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-1-a'),
        InlineKeyboardButton(text='b', callback_data='is-1-b'),
        InlineKeyboardButton(text='c', callback_data='is-1-c'),
        InlineKeyboardButton(text='d', callback_data='is-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-2-a'),
        InlineKeyboardButton(text='b', callback_data='is-2-b'),
        InlineKeyboardButton(text='c', callback_data='is-2-c'),
        InlineKeyboardButton(text='d', callback_data='is-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-3-a'),
        InlineKeyboardButton(text='b', callback_data='is-3-b'),
        InlineKeyboardButton(text='c', callback_data='is-3-c'),
        InlineKeyboardButton(text='d', callback_data='is-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-4-a'),
        InlineKeyboardButton(text='b', callback_data='is-4-b'),
        InlineKeyboardButton(text='c', callback_data='is-4-c'),
        InlineKeyboardButton(text='d', callback_data='is-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-5-a'),
        InlineKeyboardButton(text='b', callback_data='is-5-b'),
        InlineKeyboardButton(text='c', callback_data='is-5-c'),
        InlineKeyboardButton(text='d', callback_data='is-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-6-a'),
        InlineKeyboardButton(text='b', callback_data='is-6-b'),
        InlineKeyboardButton(text='c', callback_data='is-6-c'),
        InlineKeyboardButton(text='d', callback_data='is-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-7-a'),
        InlineKeyboardButton(text='b', callback_data='is-7-b'),
        InlineKeyboardButton(text='c', callback_data='is-7-c'),
        InlineKeyboardButton(text='d', callback_data='is-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-8-a'),
        InlineKeyboardButton(text='b', callback_data='is-8-b'),
        InlineKeyboardButton(text='c', callback_data='is-8-c'),
        InlineKeyboardButton(text='d', callback_data='is-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-9-a'),
        InlineKeyboardButton(text='b', callback_data='is-9-b'),
        InlineKeyboardButton(text='c', callback_data='is-9-c'),
        InlineKeyboardButton(text='d', callback_data='is-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-10-a'),
        InlineKeyboardButton(text='b', callback_data='is-10-b'),
        InlineKeyboardButton(text='c', callback_data='is-10-c'),
        InlineKeyboardButton(text='d', callback_data='is-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-11-a'),
        InlineKeyboardButton(text='b', callback_data='is-11-b'),
        InlineKeyboardButton(text='c', callback_data='is-11-c'),
        InlineKeyboardButton(text='d', callback_data='is-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-12-a'),
        InlineKeyboardButton(text='b', callback_data='is-12-b'),
        InlineKeyboardButton(text='c', callback_data='is-12-c'),
        InlineKeyboardButton(text='d', callback_data='is-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-13-a'),
        InlineKeyboardButton(text='b', callback_data='is-13-b'),
        InlineKeyboardButton(text='c', callback_data='is-13-c'),
        InlineKeyboardButton(text='d', callback_data='is-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-14-a'),
        InlineKeyboardButton(text='b', callback_data='is-14-b'),
        InlineKeyboardButton(text='c', callback_data='is-14-c'),
        InlineKeyboardButton(text='d', callback_data='is-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-15-a'),
        InlineKeyboardButton(text='b', callback_data='is-15-b'),
        InlineKeyboardButton(text='c', callback_data='is-15-c'),
        InlineKeyboardButton(text='d', callback_data='is-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-16-a'),
        InlineKeyboardButton(text='b', callback_data='is-16-b'),
        InlineKeyboardButton(text='c', callback_data='is-16-c'),
        InlineKeyboardButton(text='d', callback_data='is-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-17-a'),
        InlineKeyboardButton(text='b', callback_data='is-17-b'),
        InlineKeyboardButton(text='c', callback_data='is-17-c'),
        InlineKeyboardButton(text='d', callback_data='is-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-18-a'),
        InlineKeyboardButton(text='b', callback_data='is-18-b'),
        InlineKeyboardButton(text='c', callback_data='is-18-c'),
        InlineKeyboardButton(text='d', callback_data='is-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-19-a'),
        InlineKeyboardButton(text='b', callback_data='is-19-b'),
        InlineKeyboardButton(text='c', callback_data='is-19-c'),
        InlineKeyboardButton(text='d', callback_data='is-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def is_20_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='is-20-a'),
        InlineKeyboardButton(text='b', callback_data='is-20-b'),
        InlineKeyboardButton(text='c', callback_data='is-20-c'),
        InlineKeyboardButton(text='d', callback_data='is-20-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pr_ds_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-1-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-1-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-1-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-2-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-2-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-2-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-3-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-3-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-3-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-4-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-4-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-4-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-5-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-5-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-5-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-6-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-6-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-6-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-7-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-7-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-7-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-8-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-8-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-8-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-9-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-9-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-9-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-10-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-10-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-10-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-11-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-11-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-11-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-12-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-12-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-12-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-13-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-13-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-13-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-14-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-14-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-14-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-15-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-15-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-15-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-16-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-16-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-16-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-17-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-17-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-17-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-18-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-18-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-18-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-19-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-19-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-19-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pr_ds_20_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pr_ds-20-a'),
        InlineKeyboardButton(text='b', callback_data='pr_ds-20-b'),
        InlineKeyboardButton(text='c', callback_data='pr_ds-20-c'),
        InlineKeyboardButton(text='d', callback_data='pr_ds-20-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def kd_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='kd-1-a'),
        InlineKeyboardButton(text='b', callback_data='kd-1-b'),
        InlineKeyboardButton(text='c', callback_data='kd-1-c'),
        InlineKeyboardButton(text='d', callback_data='kd-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def kd_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='kd-2-a'),
        InlineKeyboardButton(text='b', callback_data='kd-2-b'),
        InlineKeyboardButton(text='c', callback_data='kd-2-c'),
        InlineKeyboardButton(text='d', callback_data='kd-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def kd_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='kd-3-a'),
        InlineKeyboardButton(text='b', callback_data='kd-3-b'),
        InlineKeyboardButton(text='c', callback_data='kd-3-c'),
        InlineKeyboardButton(text='d', callback_data='kd-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def kd_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='kd-4-a'),
        InlineKeyboardButton(text='b', callback_data='kd-4-b'),
        InlineKeyboardButton(text='c', callback_data='kd-4-c'),
        InlineKeyboardButton(text='d', callback_data='kd-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def kd_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='kd-5-a'),
        InlineKeyboardButton(text='b', callback_data='kd-5-b'),
        InlineKeyboardButton(text='c', callback_data='kd-5-c'),
        InlineKeyboardButton(text='d', callback_data='kd-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def kd_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='kd-6-a'),
        InlineKeyboardButton(text='b', callback_data='kd-6-b'),
        InlineKeyboardButton(text='c', callback_data='kd-6-c'),
        InlineKeyboardButton(text='d', callback_data='kd-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def kd_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='kd-7-a'),
        InlineKeyboardButton(text='b', callback_data='kd-7-b'),
        InlineKeyboardButton(text='c', callback_data='kd-7-c'),
        InlineKeyboardButton(text='d', callback_data='kd-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def kd_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='kd-8-a'),
        InlineKeyboardButton(text='b', callback_data='kd-8-b'),
        InlineKeyboardButton(text='c', callback_data='kd-8-c'),
        InlineKeyboardButton(text='d', callback_data='kd-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def kd_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='kd-9-a'),
        InlineKeyboardButton(text='b', callback_data='kd-9-b'),
        InlineKeyboardButton(text='c', callback_data='kd-9-c'),
        InlineKeyboardButton(text='d', callback_data='kd-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def kd_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='kd-10-a'),
        InlineKeyboardButton(text='b', callback_data='kd-10-b'),
        InlineKeyboardButton(text='c', callback_data='kd-10-c'),
        InlineKeyboardButton(text='d', callback_data='kd-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ot_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-1-a'),
        InlineKeyboardButton(text='b', callback_data='ot-1-b'),
        InlineKeyboardButton(text='c', callback_data='ot-1-c'),
        InlineKeyboardButton(text='d', callback_data='ot-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ot_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-2-a'),
        InlineKeyboardButton(text='b', callback_data='ot-2-b'),
        InlineKeyboardButton(text='c', callback_data='ot-2-c'),
        InlineKeyboardButton(text='d', callback_data='ot-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ot_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-3-a'),
        InlineKeyboardButton(text='b', callback_data='ot-3-b'),
        InlineKeyboardButton(text='c', callback_data='ot-3-c'),
        InlineKeyboardButton(text='d', callback_data='ot-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ot_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-4-a'),
        InlineKeyboardButton(text='b', callback_data='ot-4-b'),
        InlineKeyboardButton(text='c', callback_data='ot-4-c'),
        InlineKeyboardButton(text='d', callback_data='ot-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ot_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-5-a'),
        InlineKeyboardButton(text='b', callback_data='ot-5-b'),
        InlineKeyboardButton(text='c', callback_data='ot-5-c'),
        InlineKeyboardButton(text='d', callback_data='ot-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ot_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-6-a'),
        InlineKeyboardButton(text='b', callback_data='ot-6-b'),
        InlineKeyboardButton(text='c', callback_data='ot-6-c'),
        InlineKeyboardButton(text='d', callback_data='ot-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ot_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-7-a'),
        InlineKeyboardButton(text='b', callback_data='ot-7-b'),
        InlineKeyboardButton(text='c', callback_data='ot-7-c'),
        InlineKeyboardButton(text='d', callback_data='ot-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ot_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-8-a'),
        InlineKeyboardButton(text='b', callback_data='ot-8-b'),
        InlineKeyboardButton(text='c', callback_data='ot-8-c'),
        InlineKeyboardButton(text='d', callback_data='ot-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ot_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-9-a'),
        InlineKeyboardButton(text='b', callback_data='ot-9-b'),
        InlineKeyboardButton(text='c', callback_data='ot-9-c'),
        InlineKeyboardButton(text='d', callback_data='ot-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ot_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-10-a'),
        InlineKeyboardButton(text='b', callback_data='ot-10-b'),
        InlineKeyboardButton(text='c', callback_data='ot-10-c'),
        InlineKeyboardButton(text='d', callback_data='ot-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ot_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-11-a'),
        InlineKeyboardButton(text='b', callback_data='ot-11-b'),
        InlineKeyboardButton(text='c', callback_data='ot-11-c'),
        InlineKeyboardButton(text='d', callback_data='ot-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ot_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-12-a'),
        InlineKeyboardButton(text='b', callback_data='ot-12-b'),
        InlineKeyboardButton(text='c', callback_data='ot-12-c'),
        InlineKeyboardButton(text='d', callback_data='ot-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ot_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-13-a'),
        InlineKeyboardButton(text='b', callback_data='ot-13-b'),
        InlineKeyboardButton(text='c', callback_data='ot-13-c'),
        InlineKeyboardButton(text='d', callback_data='ot-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ot_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-14-a'),
        InlineKeyboardButton(text='b', callback_data='ot-14-b'),
        InlineKeyboardButton(text='c', callback_data='ot-14-c'),
        InlineKeyboardButton(text='d', callback_data='ot-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ot_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-15-a'),
        InlineKeyboardButton(text='b', callback_data='ot-15-b'),
        InlineKeyboardButton(text='c', callback_data='ot-15-c'),
        InlineKeyboardButton(text='d', callback_data='ot-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ot_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ot-16-a'),
        InlineKeyboardButton(text='b', callback_data='ot-16-b'),
        InlineKeyboardButton(text='c', callback_data='ot-16-c'),
        InlineKeyboardButton(text='d', callback_data='ot-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-1-a'),
        InlineKeyboardButton(text='b', callback_data='mk-1-b'),
        InlineKeyboardButton(text='c', callback_data='mk-1-c'),
        InlineKeyboardButton(text='d', callback_data='mk-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def mk_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-2-a'),
        InlineKeyboardButton(text='b', callback_data='mk-2-b'),
        InlineKeyboardButton(text='c', callback_data='mk-2-c'),
        InlineKeyboardButton(text='d', callback_data='mk-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def mk_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-3-a'),
        InlineKeyboardButton(text='b', callback_data='mk-3-b'),
        InlineKeyboardButton(text='c', callback_data='mk-3-c'),
        InlineKeyboardButton(text='d', callback_data='mk-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def mk_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-4-a'),
        InlineKeyboardButton(text='b', callback_data='mk-4-b'),
        InlineKeyboardButton(text='c', callback_data='mk-4-c'),
        InlineKeyboardButton(text='d', callback_data='mk-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def mk_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-5-a'),
        InlineKeyboardButton(text='b', callback_data='mk-5-b'),
        InlineKeyboardButton(text='c', callback_data='mk-5-c'),
        InlineKeyboardButton(text='d', callback_data='mk-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def mk_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-6-a'),
        InlineKeyboardButton(text='b', callback_data='mk-6-b'),
        InlineKeyboardButton(text='c', callback_data='mk-6-c'),
        InlineKeyboardButton(text='d', callback_data='mk-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def mk_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-7-a'),
        InlineKeyboardButton(text='b', callback_data='mk-7-b'),
        InlineKeyboardButton(text='c', callback_data='mk-7-c'),
        InlineKeyboardButton(text='d', callback_data='mk-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def mk_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-8-a'),
        InlineKeyboardButton(text='b', callback_data='mk-8-b'),
        InlineKeyboardButton(text='c', callback_data='mk-8-c'),
        InlineKeyboardButton(text='d', callback_data='mk-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def mk_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-9-a'),
        InlineKeyboardButton(text='b', callback_data='mk-9-b'),
        InlineKeyboardButton(text='c', callback_data='mk-9-c'),
        InlineKeyboardButton(text='d', callback_data='mk-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def mk_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-10-a'),
        InlineKeyboardButton(text='b', callback_data='mk-10-b'),
        InlineKeyboardButton(text='c', callback_data='mk-10-c'),
        InlineKeyboardButton(text='d', callback_data='mk-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-11-a'),
        InlineKeyboardButton(text='b', callback_data='mk-11-b'),
        InlineKeyboardButton(text='c', callback_data='mk-11-c'),
        InlineKeyboardButton(text='d', callback_data='mk-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-12-a'),
        InlineKeyboardButton(text='b', callback_data='mk-12-b'),
        InlineKeyboardButton(text='c', callback_data='mk-12-c'),
        InlineKeyboardButton(text='d', callback_data='mk-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-13-a'),
        InlineKeyboardButton(text='b', callback_data='mk-13-b'),
        InlineKeyboardButton(text='c', callback_data='mk-13-c'),
        InlineKeyboardButton(text='d', callback_data='mk-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-14-a'),
        InlineKeyboardButton(text='b', callback_data='mk-14-b'),
        InlineKeyboardButton(text='c', callback_data='mk-14-c'),
        InlineKeyboardButton(text='d', callback_data='mk-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-15-a'),
        InlineKeyboardButton(text='b', callback_data='mk-15-b'),
        InlineKeyboardButton(text='c', callback_data='mk-15-c'),
        InlineKeyboardButton(text='d', callback_data='mk-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-16-a'),
        InlineKeyboardButton(text='b', callback_data='mk-16-b'),
        InlineKeyboardButton(text='c', callback_data='mk-16-c'),
        InlineKeyboardButton(text='d', callback_data='mk-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-17-a'),
        InlineKeyboardButton(text='b', callback_data='mk-17-b'),
        InlineKeyboardButton(text='c', callback_data='mk-17-c'),
        InlineKeyboardButton(text='d', callback_data='mk-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-18-a'),
        InlineKeyboardButton(text='b', callback_data='mk-18-b'),
        InlineKeyboardButton(text='c', callback_data='mk-18-c'),
        InlineKeyboardButton(text='d', callback_data='mk-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-19-a'),
        InlineKeyboardButton(text='b', callback_data='mk-19-b'),
        InlineKeyboardButton(text='c', callback_data='mk-19-c'),
        InlineKeyboardButton(text='d', callback_data='mk-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def mk_20_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='mk-20-a'),
        InlineKeyboardButton(text='b', callback_data='mk-20-b'),
        InlineKeyboardButton(text='c', callback_data='mk-20-c'),
        InlineKeyboardButton(text='d', callback_data='mk-20-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def car_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='car-1-a'),
        InlineKeyboardButton(text='b', callback_data='car-1-b'),
        InlineKeyboardButton(text='c', callback_data='car-1-c'),
        InlineKeyboardButton(text='d', callback_data='car-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def car_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='car-2-a'),
        InlineKeyboardButton(text='b', callback_data='car-2-b'),
        InlineKeyboardButton(text='c', callback_data='car-2-c'),
        InlineKeyboardButton(text='d', callback_data='car-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def car_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='car-3-a'),
        InlineKeyboardButton(text='b', callback_data='car-3-b'),
        InlineKeyboardButton(text='c', callback_data='car-3-c'),
        InlineKeyboardButton(text='d', callback_data='car-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def car_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='car-4-a'),
        InlineKeyboardButton(text='b', callback_data='car-4-b'),
        InlineKeyboardButton(text='c', callback_data='car-4-c'),
        InlineKeyboardButton(text='d', callback_data='car-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def car_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='car-5-a'),
        InlineKeyboardButton(text='b', callback_data='car-5-b'),
        InlineKeyboardButton(text='c', callback_data='car-5-c'),
        InlineKeyboardButton(text='d', callback_data='car-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def car_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='car-6-a'),
        InlineKeyboardButton(text='b', callback_data='car-6-b'),
        InlineKeyboardButton(text='c', callback_data='car-6-c'),
        InlineKeyboardButton(text='d', callback_data='car-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def car_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='car-7-a'),
        InlineKeyboardButton(text='b', callback_data='car-7-b'),
        InlineKeyboardButton(text='c', callback_data='car-7-c'),
        InlineKeyboardButton(text='d', callback_data='car-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def car_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='car-8-a'),
        InlineKeyboardButton(text='b', callback_data='car-8-b'),
        InlineKeyboardButton(text='c', callback_data='car-8-c'),
        InlineKeyboardButton(text='d', callback_data='car-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def car_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='car-9-a'),
        InlineKeyboardButton(text='b', callback_data='car-9-b'),
        InlineKeyboardButton(text='c', callback_data='car-9-c'),
        InlineKeyboardButton(text='d', callback_data='car-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def car_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='car-10-a'),
        InlineKeyboardButton(text='b', callback_data='car-10-b'),
        InlineKeyboardButton(text='c', callback_data='car-10-c'),
        InlineKeyboardButton(text='d', callback_data='car-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-1-a'),
        InlineKeyboardButton(text='b', callback_data='pz-1-b'),
        InlineKeyboardButton(text='c', callback_data='pz-1-c'),
        InlineKeyboardButton(text='d', callback_data='pz-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pz_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-2-a'),
        InlineKeyboardButton(text='b', callback_data='pz-2-b'),
        InlineKeyboardButton(text='c', callback_data='pz-2-c'),
        InlineKeyboardButton(text='d', callback_data='pz-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pz_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-3-a'),
        InlineKeyboardButton(text='b', callback_data='pz-3-b'),
        InlineKeyboardButton(text='c', callback_data='pz-3-c'),
        InlineKeyboardButton(text='d', callback_data='pz-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pz_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-4-a'),
        InlineKeyboardButton(text='b', callback_data='pz-4-b'),
        InlineKeyboardButton(text='c', callback_data='pz-4-c'),
        InlineKeyboardButton(text='d', callback_data='pz-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pz_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-5-a'),
        InlineKeyboardButton(text='b', callback_data='pz-5-b'),
        InlineKeyboardButton(text='c', callback_data='pz-5-c'),
        InlineKeyboardButton(text='d', callback_data='pz-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pz_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-6-a'),
        InlineKeyboardButton(text='b', callback_data='pz-6-b'),
        InlineKeyboardButton(text='c', callback_data='pz-6-c'),
        InlineKeyboardButton(text='d', callback_data='pz-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pz_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-7-a'),
        InlineKeyboardButton(text='b', callback_data='pz-7-b'),
        InlineKeyboardButton(text='c', callback_data='pz-7-c'),
        InlineKeyboardButton(text='d', callback_data='pz-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pz_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-8-a'),
        InlineKeyboardButton(text='b', callback_data='pz-8-b'),
        InlineKeyboardButton(text='c', callback_data='pz-8-c'),
        InlineKeyboardButton(text='d', callback_data='pz-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pz_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-9-a'),
        InlineKeyboardButton(text='b', callback_data='pz-9-b'),
        InlineKeyboardButton(text='c', callback_data='pz-9-c'),
        InlineKeyboardButton(text='d', callback_data='pz-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pz_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-10-a'),
        InlineKeyboardButton(text='b', callback_data='pz-10-b'),
        InlineKeyboardButton(text='c', callback_data='pz-10-c'),
        InlineKeyboardButton(text='d', callback_data='pz-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-11-a'),
        InlineKeyboardButton(text='b', callback_data='pz-11-b'),
        InlineKeyboardButton(text='c', callback_data='pz-11-c'),
        InlineKeyboardButton(text='d', callback_data='pz-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-12-a'),
        InlineKeyboardButton(text='b', callback_data='pz-12-b'),
        InlineKeyboardButton(text='c', callback_data='pz-12-c'),
        InlineKeyboardButton(text='d', callback_data='pz-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-13-a'),
        InlineKeyboardButton(text='b', callback_data='pz-13-b'),
        InlineKeyboardButton(text='c', callback_data='pz-13-c'),
        InlineKeyboardButton(text='d', callback_data='pz-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-14-a'),
        InlineKeyboardButton(text='b', callback_data='pz-14-b'),
        InlineKeyboardButton(text='c', callback_data='pz-14-c'),
        InlineKeyboardButton(text='d', callback_data='pz-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-15-a'),
        InlineKeyboardButton(text='b', callback_data='pz-15-b'),
        InlineKeyboardButton(text='c', callback_data='pz-15-c'),
        InlineKeyboardButton(text='d', callback_data='pz-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-16-a'),
        InlineKeyboardButton(text='b', callback_data='pz-16-b'),
        InlineKeyboardButton(text='c', callback_data='pz-16-c'),
        InlineKeyboardButton(text='d', callback_data='pz-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-17-a'),
        InlineKeyboardButton(text='b', callback_data='pz-17-b'),
        InlineKeyboardButton(text='c', callback_data='pz-17-c'),
        InlineKeyboardButton(text='d', callback_data='pz-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-18-a'),
        InlineKeyboardButton(text='b', callback_data='pz-18-b'),
        InlineKeyboardButton(text='c', callback_data='pz-18-c'),
        InlineKeyboardButton(text='d', callback_data='pz-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-19-a'),
        InlineKeyboardButton(text='b', callback_data='pz-19-b'),
        InlineKeyboardButton(text='c', callback_data='pz-19-c'),
        InlineKeyboardButton(text='d', callback_data='pz-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pz_20_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pz-20-a'),
        InlineKeyboardButton(text='b', callback_data='pz-20-b'),
        InlineKeyboardButton(text='c', callback_data='pz-20-c'),
        InlineKeyboardButton(text='d', callback_data='pz-20-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-1-a'),
        InlineKeyboardButton(text='b', callback_data='sn-1-b'),
        InlineKeyboardButton(text='c', callback_data='sn-1-c'),
        InlineKeyboardButton(text='d', callback_data='sn-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sn_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-2-a'),
        InlineKeyboardButton(text='b', callback_data='sn-2-b'),
        InlineKeyboardButton(text='c', callback_data='sn-2-c'),
        InlineKeyboardButton(text='d', callback_data='sn-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sn_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-3-a'),
        InlineKeyboardButton(text='b', callback_data='sn-3-b'),
        InlineKeyboardButton(text='c', callback_data='sn-3-c'),
        InlineKeyboardButton(text='d', callback_data='sn-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sn_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-4-a'),
        InlineKeyboardButton(text='b', callback_data='sn-4-b'),
        InlineKeyboardButton(text='c', callback_data='sn-4-c'),
        InlineKeyboardButton(text='d', callback_data='sn-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sn_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-5-a'),
        InlineKeyboardButton(text='b', callback_data='sn-5-b'),
        InlineKeyboardButton(text='c', callback_data='sn-5-c'),
        InlineKeyboardButton(text='d', callback_data='sn-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sn_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-6-a'),
        InlineKeyboardButton(text='b', callback_data='sn-6-b'),
        InlineKeyboardButton(text='c', callback_data='sn-6-c'),
        InlineKeyboardButton(text='d', callback_data='sn-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sn_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-7-a'),
        InlineKeyboardButton(text='b', callback_data='sn-7-b'),
        InlineKeyboardButton(text='c', callback_data='sn-7-c'),
        InlineKeyboardButton(text='d', callback_data='sn-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sn_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-8-a'),
        InlineKeyboardButton(text='b', callback_data='sn-8-b'),
        InlineKeyboardButton(text='c', callback_data='sn-8-c'),
        InlineKeyboardButton(text='d', callback_data='sn-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sn_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-9-a'),
        InlineKeyboardButton(text='b', callback_data='sn-9-b'),
        InlineKeyboardButton(text='c', callback_data='sn-9-c'),
        InlineKeyboardButton(text='d', callback_data='sn-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sn_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-10-a'),
        InlineKeyboardButton(text='b', callback_data='sn-10-b'),
        InlineKeyboardButton(text='c', callback_data='sn-10-c'),
        InlineKeyboardButton(text='d', callback_data='sn-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-11-a'),
        InlineKeyboardButton(text='b', callback_data='sn-11-b'),
        InlineKeyboardButton(text='c', callback_data='sn-11-c'),
        InlineKeyboardButton(text='d', callback_data='sn-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-12-a'),
        InlineKeyboardButton(text='b', callback_data='sn-12-b'),
        InlineKeyboardButton(text='c', callback_data='sn-12-c'),
        InlineKeyboardButton(text='d', callback_data='sn-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-13-a'),
        InlineKeyboardButton(text='b', callback_data='sn-13-b'),
        InlineKeyboardButton(text='c', callback_data='sn-13-c'),
        InlineKeyboardButton(text='d', callback_data='sn-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-14-a'),
        InlineKeyboardButton(text='b', callback_data='sn-14-b'),
        InlineKeyboardButton(text='c', callback_data='sn-14-c'),
        InlineKeyboardButton(text='d', callback_data='sn-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-15-a'),
        InlineKeyboardButton(text='b', callback_data='sn-15-b'),
        InlineKeyboardButton(text='c', callback_data='sn-15-c'),
        InlineKeyboardButton(text='d', callback_data='sn-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-16-a'),
        InlineKeyboardButton(text='b', callback_data='sn-16-b'),
        InlineKeyboardButton(text='c', callback_data='sn-16-c'),
        InlineKeyboardButton(text='d', callback_data='sn-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-17-a'),
        InlineKeyboardButton(text='b', callback_data='sn-17-b'),
        InlineKeyboardButton(text='c', callback_data='sn-17-c'),
        InlineKeyboardButton(text='d', callback_data='sn-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-18-a'),
        InlineKeyboardButton(text='b', callback_data='sn-18-b'),
        InlineKeyboardButton(text='c', callback_data='sn-18-c'),
        InlineKeyboardButton(text='d', callback_data='sn-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-19-a'),
        InlineKeyboardButton(text='b', callback_data='sn-19-b'),
        InlineKeyboardButton(text='c', callback_data='sn-19-c'),
        InlineKeyboardButton(text='d', callback_data='sn-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sn_20_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sn-20-a'),
        InlineKeyboardButton(text='b', callback_data='sn-20-b'),
        InlineKeyboardButton(text='c', callback_data='sn-20-c'),
        InlineKeyboardButton(text='d', callback_data='sn-20-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-1-a'),
        InlineKeyboardButton(text='b', callback_data='sb-1-b'),
        InlineKeyboardButton(text='c', callback_data='sb-1-c'),
        InlineKeyboardButton(text='d', callback_data='sb-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sb_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-2-a'),
        InlineKeyboardButton(text='b', callback_data='sb-2-b'),
        InlineKeyboardButton(text='c', callback_data='sb-2-c'),
        InlineKeyboardButton(text='d', callback_data='sb-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sb_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-3-a'),
        InlineKeyboardButton(text='b', callback_data='sb-3-b'),
        InlineKeyboardButton(text='c', callback_data='sb-3-c'),
        InlineKeyboardButton(text='d', callback_data='sb-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sb_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-4-a'),
        InlineKeyboardButton(text='b', callback_data='sb-4-b'),
        InlineKeyboardButton(text='c', callback_data='sb-4-c'),
        InlineKeyboardButton(text='d', callback_data='sb-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sb_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-5-a'),
        InlineKeyboardButton(text='b', callback_data='sb-5-b'),
        InlineKeyboardButton(text='c', callback_data='sb-5-c'),
        InlineKeyboardButton(text='d', callback_data='sb-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sb_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-6-a'),
        InlineKeyboardButton(text='b', callback_data='sb-6-b'),
        InlineKeyboardButton(text='c', callback_data='sb-6-c'),
        InlineKeyboardButton(text='d', callback_data='sb-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sb_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-7-a'),
        InlineKeyboardButton(text='b', callback_data='sb-7-b'),
        InlineKeyboardButton(text='c', callback_data='sb-7-c'),
        InlineKeyboardButton(text='d', callback_data='sb-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sb_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-8-a'),
        InlineKeyboardButton(text='b', callback_data='sb-8-b'),
        InlineKeyboardButton(text='c', callback_data='sb-8-c'),
        InlineKeyboardButton(text='d', callback_data='sb-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sb_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-9-a'),
        InlineKeyboardButton(text='b', callback_data='sb-9-b'),
        InlineKeyboardButton(text='c', callback_data='sb-9-c'),
        InlineKeyboardButton(text='d', callback_data='sb-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sb_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-10-a'),
        InlineKeyboardButton(text='b', callback_data='sb-10-b'),
        InlineKeyboardButton(text='c', callback_data='sb-10-c'),
        InlineKeyboardButton(text='d', callback_data='sb-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-11-a'),
        InlineKeyboardButton(text='b', callback_data='sb-11-b'),
        InlineKeyboardButton(text='c', callback_data='sb-11-c'),
        InlineKeyboardButton(text='d', callback_data='sb-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-12-a'),
        InlineKeyboardButton(text='b', callback_data='sb-12-b'),
        InlineKeyboardButton(text='c', callback_data='sb-12-c'),
        InlineKeyboardButton(text='d', callback_data='sb-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-13-a'),
        InlineKeyboardButton(text='b', callback_data='sb-13-b'),
        InlineKeyboardButton(text='c', callback_data='sb-13-c'),
        InlineKeyboardButton(text='d', callback_data='sb-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-14-a'),
        InlineKeyboardButton(text='b', callback_data='sb-14-b'),
        InlineKeyboardButton(text='c', callback_data='sb-14-c'),
        InlineKeyboardButton(text='d', callback_data='sb-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-15-a'),
        InlineKeyboardButton(text='b', callback_data='sb-15-b'),
        InlineKeyboardButton(text='c', callback_data='sb-15-c'),
        InlineKeyboardButton(text='d', callback_data='sb-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-16-a'),
        InlineKeyboardButton(text='b', callback_data='sb-16-b'),
        InlineKeyboardButton(text='c', callback_data='sb-16-c'),
        InlineKeyboardButton(text='d', callback_data='sb-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-17-a'),
        InlineKeyboardButton(text='b', callback_data='sb-17-b'),
        InlineKeyboardButton(text='c', callback_data='sb-17-c'),
        InlineKeyboardButton(text='d', callback_data='sb-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-18-a'),
        InlineKeyboardButton(text='b', callback_data='sb-18-b'),
        InlineKeyboardButton(text='c', callback_data='sb-18-c'),
        InlineKeyboardButton(text='d', callback_data='sb-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-19-a'),
        InlineKeyboardButton(text='b', callback_data='sb-19-b'),
        InlineKeyboardButton(text='c', callback_data='sb-19-c'),
        InlineKeyboardButton(text='d', callback_data='sb-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sb_20_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sb-20-a'),
        InlineKeyboardButton(text='b', callback_data='sb-20-b'),
        InlineKeyboardButton(text='c', callback_data='sb-20-c'),
        InlineKeyboardButton(text='d', callback_data='sb-20-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def rn_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-1-a'),
        InlineKeyboardButton(text='b', callback_data='rn-1-b'),
        InlineKeyboardButton(text='c', callback_data='rn-1-c'),
        InlineKeyboardButton(text='d', callback_data='rn-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def rn_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-2-a'),
        InlineKeyboardButton(text='b', callback_data='rn-2-b'),
        InlineKeyboardButton(text='c', callback_data='rn-2-c'),
        InlineKeyboardButton(text='d', callback_data='rn-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def rn_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-3-a'),
        InlineKeyboardButton(text='b', callback_data='rn-3-b'),
        InlineKeyboardButton(text='c', callback_data='rn-3-c'),
        InlineKeyboardButton(text='d', callback_data='rn-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def rn_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-4-a'),
        InlineKeyboardButton(text='b', callback_data='rn-4-b'),
        InlineKeyboardButton(text='c', callback_data='rn-4-c'),
        InlineKeyboardButton(text='d', callback_data='rn-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def rn_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-5-a'),
        InlineKeyboardButton(text='b', callback_data='rn-5-b'),
        InlineKeyboardButton(text='c', callback_data='rn-5-c'),
        InlineKeyboardButton(text='d', callback_data='rn-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def rn_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-6-a'),
        InlineKeyboardButton(text='b', callback_data='rn-6-b'),
        InlineKeyboardButton(text='c', callback_data='rn-6-c'),
        InlineKeyboardButton(text='d', callback_data='rn-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def rn_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-7-a'),
        InlineKeyboardButton(text='b', callback_data='rn-7-b'),
        InlineKeyboardButton(text='c', callback_data='rn-7-c'),
        InlineKeyboardButton(text='d', callback_data='rn-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def rn_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-8-a'),
        InlineKeyboardButton(text='b', callback_data='rn-8-b'),
        InlineKeyboardButton(text='c', callback_data='rn-8-c'),
        InlineKeyboardButton(text='d', callback_data='rn-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def rn_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-9-a'),
        InlineKeyboardButton(text='b', callback_data='rn-9-b'),
        InlineKeyboardButton(text='c', callback_data='rn-9-c'),
        InlineKeyboardButton(text='d', callback_data='rn-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def rn_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-10-a'),
        InlineKeyboardButton(text='b', callback_data='rn-10-b'),
        InlineKeyboardButton(text='c', callback_data='rn-10-c'),
        InlineKeyboardButton(text='d', callback_data='rn-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def rn_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-11-a'),
        InlineKeyboardButton(text='b', callback_data='rn-11-b'),
        InlineKeyboardButton(text='c', callback_data='rn-11-c'),
        InlineKeyboardButton(text='d', callback_data='rn-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def rn_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-12-a'),
        InlineKeyboardButton(text='b', callback_data='rn-12-b'),
        InlineKeyboardButton(text='c', callback_data='rn-12-c'),
        InlineKeyboardButton(text='d', callback_data='rn-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def rn_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-13-a'),
        InlineKeyboardButton(text='b', callback_data='rn-13-b'),
        InlineKeyboardButton(text='c', callback_data='rn-13-c'),
        InlineKeyboardButton(text='d', callback_data='rn-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def rn_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-14-a'),
        InlineKeyboardButton(text='b', callback_data='rn-14-b'),
        InlineKeyboardButton(text='c', callback_data='rn-14-c'),
        InlineKeyboardButton(text='d', callback_data='rn-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def rn_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-15-a'),
        InlineKeyboardButton(text='b', callback_data='rn-15-b'),
        InlineKeyboardButton(text='c', callback_data='rn-15-c'),
        InlineKeyboardButton(text='d', callback_data='rn-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def rn_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-16-a'),
        InlineKeyboardButton(text='b', callback_data='rn-16-b'),
        InlineKeyboardButton(text='c', callback_data='rn-16-c'),
        InlineKeyboardButton(text='d', callback_data='rn-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def rn_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-17-a'),
        InlineKeyboardButton(text='b', callback_data='rn-17-b'),
        InlineKeyboardButton(text='c', callback_data='rn-17-c'),
        InlineKeyboardButton(text='d', callback_data='rn-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def rn_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-18-a'),
        InlineKeyboardButton(text='b', callback_data='rn-18-b'),
        InlineKeyboardButton(text='c', callback_data='rn-18-c'),
        InlineKeyboardButton(text='d', callback_data='rn-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def rn_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='rn-19-a'),
        InlineKeyboardButton(text='b', callback_data='rn-19-b'),
        InlineKeyboardButton(text='c', callback_data='rn-19-c'),
        InlineKeyboardButton(text='d', callback_data='rn-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def bc_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-1-a'),
        InlineKeyboardButton(text='b', callback_data='bc-1-b'),
        InlineKeyboardButton(text='c', callback_data='bc-1-c'),
        InlineKeyboardButton(text='d', callback_data='bc-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def bc_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-2-a'),
        InlineKeyboardButton(text='b', callback_data='bc-2-b'),
        InlineKeyboardButton(text='c', callback_data='bc-2-c'),
        InlineKeyboardButton(text='d', callback_data='bc-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def bc_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-3-a'),
        InlineKeyboardButton(text='b', callback_data='bc-3-b'),
        InlineKeyboardButton(text='c', callback_data='bc-3-c'),
        InlineKeyboardButton(text='d', callback_data='bc-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def bc_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-4-a'),
        InlineKeyboardButton(text='b', callback_data='bc-4-b'),
        InlineKeyboardButton(text='c', callback_data='bc-4-c'),
        InlineKeyboardButton(text='d', callback_data='bc-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def bc_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-5-a'),
        InlineKeyboardButton(text='b', callback_data='bc-5-b'),
        InlineKeyboardButton(text='c', callback_data='bc-5-c'),
        InlineKeyboardButton(text='d', callback_data='bc-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def bc_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-6-a'),
        InlineKeyboardButton(text='b', callback_data='bc-6-b'),
        InlineKeyboardButton(text='c', callback_data='bc-6-c'),
        InlineKeyboardButton(text='d', callback_data='bc-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def bc_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-7-a'),
        InlineKeyboardButton(text='b', callback_data='bc-7-b'),
        InlineKeyboardButton(text='c', callback_data='bc-7-c'),
        InlineKeyboardButton(text='d', callback_data='bc-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def bc_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-8-a'),
        InlineKeyboardButton(text='b', callback_data='bc-8-b'),
        InlineKeyboardButton(text='c', callback_data='bc-8-c'),
        InlineKeyboardButton(text='d', callback_data='bc-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def bc_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-9-a'),
        InlineKeyboardButton(text='b', callback_data='bc-9-b'),
        InlineKeyboardButton(text='c', callback_data='bc-9-c'),
        InlineKeyboardButton(text='d', callback_data='bc-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def bc_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-10-a'),
        InlineKeyboardButton(text='b', callback_data='bc-10-b'),
        InlineKeyboardButton(text='c', callback_data='bc-10-c'),
        InlineKeyboardButton(text='d', callback_data='bc-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def bc_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-11-a'),
        InlineKeyboardButton(text='b', callback_data='bc-11-b'),
        InlineKeyboardButton(text='c', callback_data='bc-11-c'),
        InlineKeyboardButton(text='d', callback_data='bc-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def bc_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-12-a'),
        InlineKeyboardButton(text='b', callback_data='bc-12-b'),
        InlineKeyboardButton(text='c', callback_data='bc-12-c'),
        InlineKeyboardButton(text='d', callback_data='bc-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def bc_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-13-a'),
        InlineKeyboardButton(text='b', callback_data='bc-13-b'),
        InlineKeyboardButton(text='c', callback_data='bc-13-c'),
        InlineKeyboardButton(text='d', callback_data='bc-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def bc_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-14-a'),
        InlineKeyboardButton(text='b', callback_data='bc-14-b'),
        InlineKeyboardButton(text='c', callback_data='bc-14-c'),
        InlineKeyboardButton(text='d', callback_data='bc-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def bc_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-15-a'),
        InlineKeyboardButton(text='b', callback_data='bc-15-b'),
        InlineKeyboardButton(text='c', callback_data='bc-15-c'),
        InlineKeyboardButton(text='d', callback_data='bc-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def bc_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-16-a'),
        InlineKeyboardButton(text='b', callback_data='bc-16-b'),
        InlineKeyboardButton(text='c', callback_data='bc-16-c'),
        InlineKeyboardButton(text='d', callback_data='bc-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def bc_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-17-a'),
        InlineKeyboardButton(text='b', callback_data='bc-17-b'),
        InlineKeyboardButton(text='c', callback_data='bc-17-c'),
        InlineKeyboardButton(text='d', callback_data='bc-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def bc_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='bc-18-a'),
        InlineKeyboardButton(text='b', callback_data='bc-18-b'),
        InlineKeyboardButton(text='c', callback_data='bc-18-c'),
        InlineKeyboardButton(text='d', callback_data='bc-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-1-a'),
        InlineKeyboardButton(text='b', callback_data='pj-1-b'),
        InlineKeyboardButton(text='c', callback_data='pj-1-c'),
        InlineKeyboardButton(text='d', callback_data='pj-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pj_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-2-a'),
        InlineKeyboardButton(text='b', callback_data='pj-2-b'),
        InlineKeyboardButton(text='c', callback_data='pj-2-c'),
        InlineKeyboardButton(text='d', callback_data='pj-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pj_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-3-a'),
        InlineKeyboardButton(text='b', callback_data='pj-3-b'),
        InlineKeyboardButton(text='c', callback_data='pj-3-c'),
        InlineKeyboardButton(text='d', callback_data='pj-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pj_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-4-a'),
        InlineKeyboardButton(text='b', callback_data='pj-4-b'),
        InlineKeyboardButton(text='c', callback_data='pj-4-c'),
        InlineKeyboardButton(text='d', callback_data='pj-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pj_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-5-a'),
        InlineKeyboardButton(text='b', callback_data='pj-5-b'),
        InlineKeyboardButton(text='c', callback_data='pj-5-c'),
        InlineKeyboardButton(text='d', callback_data='pj-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pj_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-6-a'),
        InlineKeyboardButton(text='b', callback_data='pj-6-b'),
        InlineKeyboardButton(text='c', callback_data='pj-6-c'),
        InlineKeyboardButton(text='d', callback_data='pj-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pj_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-7-a'),
        InlineKeyboardButton(text='b', callback_data='pj-7-b'),
        InlineKeyboardButton(text='c', callback_data='pj-7-c'),
        InlineKeyboardButton(text='d', callback_data='pj-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pj_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-8-a'),
        InlineKeyboardButton(text='b', callback_data='pj-8-b'),
        InlineKeyboardButton(text='c', callback_data='pj-8-c'),
        InlineKeyboardButton(text='d', callback_data='pj-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pj_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-9-a'),
        InlineKeyboardButton(text='b', callback_data='pj-9-b'),
        InlineKeyboardButton(text='c', callback_data='pj-9-c'),
        InlineKeyboardButton(text='d', callback_data='pj-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pj_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-10-a'),
        InlineKeyboardButton(text='b', callback_data='pj-10-b'),
        InlineKeyboardButton(text='c', callback_data='pj-10-c'),
        InlineKeyboardButton(text='d', callback_data='pj-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_11_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-11-a'),
        InlineKeyboardButton(text='b', callback_data='pj-11-b'),
        InlineKeyboardButton(text='c', callback_data='pj-11-c'),
        InlineKeyboardButton(text='d', callback_data='pj-11-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_12_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-12-a'),
        InlineKeyboardButton(text='b', callback_data='pj-12-b'),
        InlineKeyboardButton(text='c', callback_data='pj-12-c'),
        InlineKeyboardButton(text='d', callback_data='pj-12-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_13_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-13-a'),
        InlineKeyboardButton(text='b', callback_data='pj-13-b'),
        InlineKeyboardButton(text='c', callback_data='pj-13-c'),
        InlineKeyboardButton(text='d', callback_data='pj-13-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_14_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-14-a'),
        InlineKeyboardButton(text='b', callback_data='pj-14-b'),
        InlineKeyboardButton(text='c', callback_data='pj-14-c'),
        InlineKeyboardButton(text='d', callback_data='pj-14-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_15_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-15-a'),
        InlineKeyboardButton(text='b', callback_data='pj-15-b'),
        InlineKeyboardButton(text='c', callback_data='pj-15-c'),
        InlineKeyboardButton(text='d', callback_data='pj-15-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_16_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-16-a'),
        InlineKeyboardButton(text='b', callback_data='pj-16-b'),
        InlineKeyboardButton(text='c', callback_data='pj-16-c'),
        InlineKeyboardButton(text='d', callback_data='pj-16-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_17_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-17-a'),
        InlineKeyboardButton(text='b', callback_data='pj-17-b'),
        InlineKeyboardButton(text='c', callback_data='pj-17-c'),
        InlineKeyboardButton(text='d', callback_data='pj-17-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_18_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-18-a'),
        InlineKeyboardButton(text='b', callback_data='pj-18-b'),
        InlineKeyboardButton(text='c', callback_data='pj-18-c'),
        InlineKeyboardButton(text='d', callback_data='pj-18-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_19_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-19-a'),
        InlineKeyboardButton(text='b', callback_data='pj-19-b'),
        InlineKeyboardButton(text='c', callback_data='pj-19-c'),
        InlineKeyboardButton(text='d', callback_data='pj-19-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pj_20_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pj-20-a'),
        InlineKeyboardButton(text='b', callback_data='pj-20-b'),
        InlineKeyboardButton(text='c', callback_data='pj-20-c'),
        InlineKeyboardButton(text='d', callback_data='pj-20-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def lt_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lt-1-a'),
        InlineKeyboardButton(text='b', callback_data='lt-1-b'),
        InlineKeyboardButton(text='c', callback_data='lt-1-c'),
        InlineKeyboardButton(text='d', callback_data='lt-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lt_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lt-2-a'),
        InlineKeyboardButton(text='b', callback_data='lt-2-b'),
        InlineKeyboardButton(text='c', callback_data='lt-2-c'),
        InlineKeyboardButton(text='d', callback_data='lt-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lt_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lt-3-a'),
        InlineKeyboardButton(text='b', callback_data='lt-3-b'),
        InlineKeyboardButton(text='c', callback_data='lt-3-c'),
        InlineKeyboardButton(text='d', callback_data='lt-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lt_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lt-4-a'),
        InlineKeyboardButton(text='b', callback_data='lt-4-b'),
        InlineKeyboardButton(text='c', callback_data='lt-4-c'),
        InlineKeyboardButton(text='d', callback_data='lt-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lt_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lt-5-a'),
        InlineKeyboardButton(text='b', callback_data='lt-5-b'),
        InlineKeyboardButton(text='c', callback_data='lt-5-c'),
        InlineKeyboardButton(text='d', callback_data='lt-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lt_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lt-6-a'),
        InlineKeyboardButton(text='b', callback_data='lt-6-b'),
        InlineKeyboardButton(text='c', callback_data='lt-6-c'),
        InlineKeyboardButton(text='d', callback_data='lt-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lt_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lt-7-a'),
        InlineKeyboardButton(text='b', callback_data='lt-7-b'),
        InlineKeyboardButton(text='c', callback_data='lt-7-c'),
        InlineKeyboardButton(text='d', callback_data='lt-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lt_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lt-8-a'),
        InlineKeyboardButton(text='b', callback_data='lt-8-b'),
        InlineKeyboardButton(text='c', callback_data='lt-8-c'),
        InlineKeyboardButton(text='d', callback_data='lt-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lt_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lt-9-a'),
        InlineKeyboardButton(text='b', callback_data='lt-9-b'),
        InlineKeyboardButton(text='c', callback_data='lt-9-c'),
        InlineKeyboardButton(text='d', callback_data='lt-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lt_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lt-10-a'),
        InlineKeyboardButton(text='b', callback_data='lt-10-b'),
        InlineKeyboardButton(text='c', callback_data='lt-10-c'),
        InlineKeyboardButton(text='d', callback_data='lt-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def pv_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pv-1-a'),
        InlineKeyboardButton(text='b', callback_data='pv-1-b'),
        InlineKeyboardButton(text='c', callback_data='pv-1-c'),
        InlineKeyboardButton(text='d', callback_data='pv-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pv_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pv-2-a'),
        InlineKeyboardButton(text='b', callback_data='pv-2-b'),
        InlineKeyboardButton(text='c', callback_data='pv-2-c'),
        InlineKeyboardButton(text='d', callback_data='pv-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pv_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pv-3-a'),
        InlineKeyboardButton(text='b', callback_data='pv-3-b'),
        InlineKeyboardButton(text='c', callback_data='pv-3-c'),
        InlineKeyboardButton(text='d', callback_data='pv-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pv_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pv-4-a'),
        InlineKeyboardButton(text='b', callback_data='pv-4-b'),
        InlineKeyboardButton(text='c', callback_data='pv-4-c'),
        InlineKeyboardButton(text='d', callback_data='pv-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pv_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pv-5-a'),
        InlineKeyboardButton(text='b', callback_data='pv-5-b'),
        InlineKeyboardButton(text='c', callback_data='pv-5-c'),
        InlineKeyboardButton(text='d', callback_data='pv-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pv_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pv-6-a'),
        InlineKeyboardButton(text='b', callback_data='pv-6-b'),
        InlineKeyboardButton(text='c', callback_data='pv-6-c'),
        InlineKeyboardButton(text='d', callback_data='pv-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pv_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pv-7-a'),
        InlineKeyboardButton(text='b', callback_data='pv-7-b'),
        InlineKeyboardButton(text='c', callback_data='pv-7-c'),
        InlineKeyboardButton(text='d', callback_data='pv-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pv_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pv-8-a'),
        InlineKeyboardButton(text='b', callback_data='pv-8-b'),
        InlineKeyboardButton(text='c', callback_data='pv-8-c'),
        InlineKeyboardButton(text='d', callback_data='pv-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pv_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pv-9-a'),
        InlineKeyboardButton(text='b', callback_data='pv-9-b'),
        InlineKeyboardButton(text='c', callback_data='pv-9-c'),
        InlineKeyboardButton(text='d', callback_data='pv-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def pv_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='pv-10-a'),
        InlineKeyboardButton(text='b', callback_data='pv-10-b'),
        InlineKeyboardButton(text='c', callback_data='pv-10-c'),
        InlineKeyboardButton(text='d', callback_data='pv-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ki_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ki-1-a'),
        InlineKeyboardButton(text='b', callback_data='ki-1-b'),
        InlineKeyboardButton(text='c', callback_data='ki-1-c'),
        InlineKeyboardButton(text='d', callback_data='ki-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ki_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ki-2-a'),
        InlineKeyboardButton(text='b', callback_data='ki-2-b'),
        InlineKeyboardButton(text='c', callback_data='ki-2-c'),
        InlineKeyboardButton(text='d', callback_data='ki-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ki_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ki-3-a'),
        InlineKeyboardButton(text='b', callback_data='ki-3-b'),
        InlineKeyboardButton(text='c', callback_data='ki-3-c'),
        InlineKeyboardButton(text='d', callback_data='ki-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ki_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ki-4-a'),
        InlineKeyboardButton(text='b', callback_data='ki-4-b'),
        InlineKeyboardButton(text='c', callback_data='ki-4-c'),
        InlineKeyboardButton(text='d', callback_data='ki-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ki_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ki-5-a'),
        InlineKeyboardButton(text='b', callback_data='ki-5-b'),
        InlineKeyboardButton(text='c', callback_data='ki-5-c'),
        InlineKeyboardButton(text='d', callback_data='ki-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ki_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ki-6-a'),
        InlineKeyboardButton(text='b', callback_data='ki-6-b'),
        InlineKeyboardButton(text='c', callback_data='ki-6-c'),
        InlineKeyboardButton(text='d', callback_data='ki-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ki_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ki-7-a'),
        InlineKeyboardButton(text='b', callback_data='ki-7-b'),
        InlineKeyboardButton(text='c', callback_data='ki-7-c'),
        InlineKeyboardButton(text='d', callback_data='ki-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ki_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ki-8-a'),
        InlineKeyboardButton(text='b', callback_data='ki-8-b'),
        InlineKeyboardButton(text='c', callback_data='ki-8-c'),
        InlineKeyboardButton(text='d', callback_data='ki-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ki_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ki-9-a'),
        InlineKeyboardButton(text='b', callback_data='ki-9-b'),
        InlineKeyboardButton(text='c', callback_data='ki-9-c'),
        InlineKeyboardButton(text='d', callback_data='ki-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ki_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ki-10-a'),
        InlineKeyboardButton(text='b', callback_data='ki-10-b'),
        InlineKeyboardButton(text='c', callback_data='ki-10-c'),
        InlineKeyboardButton(text='d', callback_data='ki-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def lr_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lr-1-a'),
        InlineKeyboardButton(text='b', callback_data='lr-1-b'),
        InlineKeyboardButton(text='c', callback_data='lr-1-c'),
        InlineKeyboardButton(text='d', callback_data='lr-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lr_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lr-2-a'),
        InlineKeyboardButton(text='b', callback_data='lr-2-b'),
        InlineKeyboardButton(text='c', callback_data='lr-2-c'),
        InlineKeyboardButton(text='d', callback_data='lr-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lr_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lr-3-a'),
        InlineKeyboardButton(text='b', callback_data='lr-3-b'),
        InlineKeyboardButton(text='c', callback_data='lr-3-c'),
        InlineKeyboardButton(text='d', callback_data='lr-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lr_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lr-4-a'),
        InlineKeyboardButton(text='b', callback_data='lr-4-b'),
        InlineKeyboardButton(text='c', callback_data='lr-4-c'),
        InlineKeyboardButton(text='d', callback_data='lr-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lr_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lr-5-a'),
        InlineKeyboardButton(text='b', callback_data='lr-5-b'),
        InlineKeyboardButton(text='c', callback_data='lr-5-c'),
        InlineKeyboardButton(text='d', callback_data='lr-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lr_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lr-6-a'),
        InlineKeyboardButton(text='b', callback_data='lr-6-b'),
        InlineKeyboardButton(text='c', callback_data='lr-6-c'),
        InlineKeyboardButton(text='d', callback_data='lr-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lr_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lr-7-a'),
        InlineKeyboardButton(text='b', callback_data='lr-7-b'),
        InlineKeyboardButton(text='c', callback_data='lr-7-c'),
        InlineKeyboardButton(text='d', callback_data='lr-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lr_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lr-8-a'),
        InlineKeyboardButton(text='b', callback_data='lr-8-b'),
        InlineKeyboardButton(text='c', callback_data='lr-8-c'),
        InlineKeyboardButton(text='d', callback_data='lr-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lr_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lr-9-a'),
        InlineKeyboardButton(text='b', callback_data='lr-9-b'),
        InlineKeyboardButton(text='c', callback_data='lr-9-c'),
        InlineKeyboardButton(text='d', callback_data='lr-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def lr_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='lr-10-a'),
        InlineKeyboardButton(text='b', callback_data='lr-10-b'),
        InlineKeyboardButton(text='c', callback_data='lr-10-c'),
        InlineKeyboardButton(text='d', callback_data='lr-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def ms_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ms-1-a'),
        InlineKeyboardButton(text='b', callback_data='ms-1-b'),
        InlineKeyboardButton(text='c', callback_data='ms-1-c'),
        InlineKeyboardButton(text='d', callback_data='ms-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ms_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ms-2-a'),
        InlineKeyboardButton(text='b', callback_data='ms-2-b'),
        InlineKeyboardButton(text='c', callback_data='ms-2-c'),
        InlineKeyboardButton(text='d', callback_data='ms-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ms_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ms-3-a'),
        InlineKeyboardButton(text='b', callback_data='ms-3-b'),
        InlineKeyboardButton(text='c', callback_data='ms-3-c'),
        InlineKeyboardButton(text='d', callback_data='ms-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ms_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ms-4-a'),
        InlineKeyboardButton(text='b', callback_data='ms-4-b'),
        InlineKeyboardButton(text='c', callback_data='ms-4-c'),
        InlineKeyboardButton(text='d', callback_data='ms-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ms_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ms-5-a'),
        InlineKeyboardButton(text='b', callback_data='ms-5-b'),
        InlineKeyboardButton(text='c', callback_data='ms-5-c'),
        InlineKeyboardButton(text='d', callback_data='ms-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ms_6_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ms-6-a'),
        InlineKeyboardButton(text='b', callback_data='ms-6-b'),
        InlineKeyboardButton(text='c', callback_data='ms-6-c'),
        InlineKeyboardButton(text='d', callback_data='ms-6-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ms_7_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ms-7-a'),
        InlineKeyboardButton(text='b', callback_data='ms-7-b'),
        InlineKeyboardButton(text='c', callback_data='ms-7-c'),
        InlineKeyboardButton(text='d', callback_data='ms-7-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ms_8_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ms-8-a'),
        InlineKeyboardButton(text='b', callback_data='ms-8-b'),
        InlineKeyboardButton(text='c', callback_data='ms-8-c'),
        InlineKeyboardButton(text='d', callback_data='ms-8-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ms_9_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ms-9-a'),
        InlineKeyboardButton(text='b', callback_data='ms-9-b'),
        InlineKeyboardButton(text='c', callback_data='ms-9-c'),
        InlineKeyboardButton(text='d', callback_data='ms-9-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def ms_10_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='ms-10-a'),
        InlineKeyboardButton(text='b', callback_data='ms-10-b'),
        InlineKeyboardButton(text='c', callback_data='ms-10-c'),
        InlineKeyboardButton(text='d', callback_data='ms-10-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()

def sd_1_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sd-1-a'),
        InlineKeyboardButton(text='b', callback_data='sd-1-b'),
        InlineKeyboardButton(text='c', callback_data='sd-1-c'),
        InlineKeyboardButton(text='d', callback_data='sd-1-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sd_2_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sd-2-a'),
        InlineKeyboardButton(text='b', callback_data='sd-2-b'),
        InlineKeyboardButton(text='c', callback_data='sd-2-c'),
        InlineKeyboardButton(text='d', callback_data='sd-2-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sd_3_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sd-3-a'),
        InlineKeyboardButton(text='b', callback_data='sd-3-b'),
        InlineKeyboardButton(text='c', callback_data='sd-3-c'),
        InlineKeyboardButton(text='d', callback_data='sd-3-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sd_4_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sd-4-a'),
        InlineKeyboardButton(text='b', callback_data='sd-4-b'),
        InlineKeyboardButton(text='c', callback_data='sd-4-c'),
        InlineKeyboardButton(text='d', callback_data='sd-4-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()


def sd_5_answer():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='a', callback_data='sd-5-a'),
        InlineKeyboardButton(text='b', callback_data='sd-5-b'),
        InlineKeyboardButton(text='c', callback_data='sd-5-c'),
        InlineKeyboardButton(text='d', callback_data='sd-5-d')
    ]
    kb_builder.row(*buttons, width=4)
    return kb_builder.as_markup()