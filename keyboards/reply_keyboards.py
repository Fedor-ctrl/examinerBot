
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def choose_course():
    buttons = [
        [KeyboardButton(text='Представление компании Good-Avto')],
        [KeyboardButton(text='Слесарные работы')],
        [KeyboardButton(text='Шиномонтаж')],
        [KeyboardButton(text='Система кондиционирования')],
        [KeyboardButton(text='Общее устройство автомобиля')],
        [KeyboardButton(text='Электрика авто')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, one_time_keyboard=True, resize_keyboard=True)

def hello_slesarka():
    buttons = [
        [KeyboardButton(text='Осмотр автомобиля')],
        [KeyboardButton(text='Устройства ДВС')],
        [KeyboardButton(text='Топливная система')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, one_time_keyboard=True, resize_keyboard=True)

def kursi_po_shinke():
    buttons = [
        [KeyboardButton(text='Госты и Нормативы')],
        [KeyboardButton(text='Оборудование для шиномонтажа')],
        [KeyboardButton(text='Ремонт и шиномонтаж')],
        [KeyboardButton(text='Устройство колёс')],
        [KeyboardButton(text='Правка дисков')],
        [KeyboardButton(text='Тренинг')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, one_time_keyboard=True, resize_keyboard=True)

def kursi_po_kolesam():
    buttons = [
        [KeyboardButton(text='Уроки по дискам')],
        [KeyboardButton(text='Уроки по шинам')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, one_time_keyboard=True, resize_keyboard=True)

def kurs_po_shinke():
    buttons = [
        [KeyboardButton(text='Правка дисков')],
        [KeyboardButton(text='Устройство дисков')],
        [KeyboardButton(text='Оборудование для шиномонтажа')],
        [KeyboardButton(text='Шиномонтаж и ремонт')],
        [KeyboardButton(text='Балансировка колес')],
        [KeyboardButton(text='Устройство шин')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, one_time_keyboard=True, resize_keyboard=True)

def kurs_po_electrike():
    buttons = [
        [KeyboardButton(text='1 курс')],
        [KeyboardButton(text='2 курс')],
        [KeyboardButton(text='3 курс')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, one_time_keyboard=True, resize_keyboard=True)