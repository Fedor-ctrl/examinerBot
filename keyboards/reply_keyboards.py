from aiogram.types import ReplyKeyboardMarkup, Message, KeyboardButton
from aiogram import Router
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from CarKnowlegdeTest import carTest

def choose_course():
    buttons = [
        [KeyboardButton(text='Общее устройство автомобиля')],
        [KeyboardButton(text='Слесарные работы')],
        [KeyboardButton(text='Система кондиционирования')],
        [KeyboardButton(text='Электрика авто')], [KeyboardButton(text='Шиномонтаж')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, one_time_keyboard=True, resize_keyboard=True)


def get_keyboard(question_index):
    builder = ReplyKeyboardBuilder()
    buttons = []
    for answer, _ in carTest.questions[question_index]["answers"]:
        print(answer)
        buttons.append(KeyboardButton(text=answer))
    builder.row(*buttons, width=1)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
