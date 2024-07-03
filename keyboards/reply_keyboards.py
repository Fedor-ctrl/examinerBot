from aiogram.types import ReplyKeyboardMarkup, Message, KeyboardButton
from aiogram import Router
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def choose_course():
    buttons = [
        [KeyboardButton(text='Слесарные работы')],
        [KeyboardButton(text='Система кондиционирования')],
        [KeyboardButton(text='Электрика авто')],
        [KeyboardButton(text='Шиномонтаж')]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, one_time_keyboard=True, resize_keyboard=True)
