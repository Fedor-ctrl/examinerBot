from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Отправить видео как делать полный осмотр, либо вернуться в меню:
def send_video_osmotr():
    kb_builder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(text='Полный осмотр авто(YouTube)', url='https://youtu.be/JbsrSAg_slg?si=exQj5KHRyWQOy8am'),
        InlineKeyboardButton(text='Вернуться в меню', callback_data='get_me_to_menu')
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



