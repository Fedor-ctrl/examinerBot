import time
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram import Router, F, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import asyncio
from aiogram.types import InputMediaPhoto

from keyboards import inline_keyboards, reply_keyboards
from database_funcs import sqlite_funcs

admin_id = 1004684045
admin_id1 = 853884484

router = Router()

storage = MemoryStorage()

dict_to_check_progress = {}
users = {}
users_car_test = dict()


@router.message(CommandStart())
async def say_hello(message: Message):
    await message.answer(text='Приветствую в боте академии Good-Avto!\n\nВыберите курс для прохождения:',
                         reply_markup=reply_keyboards.choose_course())


@router.message(Command('menu'))
async def command_menu(message: Message):
    await message.answer(text='Это главное меню!',
                         reply_markup=reply_keyboards.choose_course())


@router.message(Command('help'))
async def command_menu(message: Message):
    await message.answer(text='Это бот академии Good-Avto\n\n'
                              'Только для сотрудников СТО\n'                              
                              'Расти и развивайся вместе с нами!\n'
                              '/menu',
                         reply_markup=reply_keyboards.choose_course())
@router.message(F.text == 'Оборудование для шиномонтажа')
async def oborudovanie(message: Message):
    await message.answer(text='Добро пожаловать на курс по ремонту и шиномонтажу!\n\n',
                         reply_markup=inline_keyboards.oborudovanie())

@router.message(F.text == 'Госты и Нормативы')
async def send_gosts_and_normatives(message: Message):
    try:
        # Список URL изображений
        image_urls = [
            "https://disk.yandex.ru/i/Hx9ai90xBTFsEA",
            "https://disk.yandex.ru/i/t_612KAiWIk9mg",
            "https://disk.yandex.ru/i/48u2SFNTgmaK0g",
            "https://disk.yandex.ru/i/hzKdVc9MIvf2wg",
            "https://disk.yandex.ru/i/uEi-HPccKOCVUQ"
        ]

        # Создаем список объектов InputMediaPhoto
        media = [InputMediaPhoto(media=url, caption=f"Изображение {i+1}") for i, url in enumerate(image_urls)]

        # Отправляем альбом
        await message.answer_media_group(media=media)
    except Exception as e:
        await message.answer("Произошла ошибка при отправке изображений.")
        print(f"Ошибка отправки изображений: {e}")

@router.message(F.text == 'Тренинг')
async def treningi(message: Message):
    await message.answer(text='Добро пожаловать на уроки по тренингу!\n\n',
                         reply_markup=inline_keyboards.treningi())

@router.message(F.text == 'Система питания')
async def treningi(message: Message):
    await message.answer(text='Добро пожаловать на курс по системам питания!\n\n',
                         reply_markup=inline_keyboards.sysvpr())

@router.message(F.text == 'Представление компании Good-Avto')
async def send_predstavlenie_kompanii(message: Message):
    await message.answer(
        text='Для того, что бы посмотреть презентацию о компании Good-Avto, перейдите по ссылке ниже.\n\n',
        reply_markup=inline_keyboards.send_predstavlenie_kompanii())

@router.message(F.text == 'Общее устройство автомобиля')
async def say_hello_ac(message: Message):
    await message.answer(text='Добрый день! Направляю видео по устройству авто:\n\n',
                         reply_markup=inline_keyboards.usr_vo_avto())
    time.sleep(10)
    await message.answer(
        text='Посмотрели видео и готовы пройти тест?',
        reply_markup=inline_keyboards.i_did_watch_the_video())

@router.message(F.text == 'Система кондиционирования')
async def say_hello_ac(message: Message):
    await message.answer(text='Приветствую на курсе по системам кондиционирования автомобиля!\n\n'
                              'Ниже представлены видеоматериалы по работам.\n\n'
                              'Ознакомьтесь со всеми:',
                         reply_markup=inline_keyboards.graphics_to_continue())

@router.message(F.text == 'Уроки по шинам')
async def send_block_po_shinshiku(message: Message):
    await message.answer(text='Приветствую в блоке по устройству шин!\n\n'
                              'Выберете курс для прохождения:',
                         reply_markup=inline_keyboards.shinshik())

@router.callback_query(F.data == 'get_me_to_menu')
async def redirect_to_menu(callback: CallbackQuery):
    await callback.message.answer(text='Это главное меню!', reply_markup=reply_keyboards.choose_course())

@router.message(F.text == 'Электрика авто')
async def say_hello_electricity(message: Message):
    await message.answer(text='Приветствую на курсе по электрике автомобиля!. Этот курс еще не доступен\n\n'
                              'возвращайтесь позже, скоро он появится тут для ознакомления',
                         reply_markup=reply_keyboards.choose_course())

@router.message(F.text == 'Слесарные работы')
async def say_hello_slesarka(message: Message):
    await message.answer(text='Приветствую на курсе по слесарным работам автомобиля!. Этот курс еще не доступен\n\n'
                              'возвращайтесь позже, скоро он появится тут для ознакомления',
                         reply_markup=reply_keyboards.choose_course())

@router.message(F.text == 'Шиномонтаж')
async def send_block_po_shinke(message: Message):
    await message.answer(text='Приветствую в блоке по шиномонтажу!\n\n'
                              'Выберете курс для прохождения:',
                         reply_markup=reply_keyboards.kursi_po_shinke())

@router.message(F.text == 'Устройство колёс')
async def send_block_po_kolesam(message: Message):
    await message.answer(text='Приветствую в блоке по устройству колёс!\n\n'
                              'Выберете курс для прохождения:',
                         reply_markup=reply_keyboards.kursi_po_kolesam())

@router.message(F.text == 'Уроки по дискам')
async def send_block_po_diskam(message: Message):
    await message.answer(text='Приветствую в блоке по устройству дисков!\n\n'
                              'Выберете курс для прохождения:',
                         reply_markup=inline_keyboards.diski())

@router.message(F.text == 'Правка дисков')
async def send_test_po_pravkam(message: Message):
    await message.answer(text='Приветствую на уроке по правкам дисков!\n\n',
                         reply_markup=inline_keyboards.pravka_diskov_uroki())

@router.callback_query(F.data == 'kurs_vtoroy')
async def kurs_vtoroy(callback: CallbackQuery):
      await callback.message.answer(text='Добро пожаловать на 1 курс по электрике!\n\n'
                                             'Выберите видео из курса',
                          reply_markup=reply_keyboards.kurs_po_electrike())

@router.callback_query(F.data == 'i_did_watch_the_video')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='car_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по полному осмотру автомобиля!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что включает в себя система охлаждения двигателя?\n\n
a) Карданную передачу.\n
b) Радиатор, вентилятор, помпу.\n
c) Топливный бак.\n
d) Сцепление и коробку передач.''',
                                      reply_markup=inline_keyboards.car_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'car-1-a')
@router.callback_query(F.data == 'car-1-b')
@router.callback_query(F.data == 'car-1-c')
@router.callback_query(F.data == 'car-1-d')
async def car_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'car-1-a': False,
        'car-1-b': True,
        'car-1-c': False,
        'car-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какой тип двигателя упоминается в видео?\n\n
a) Электрический.\n
b) Гибридный.\n
c) Двигатель внутреннего сгорания.\n
d) Газовый.''',
                                      reply_markup=inline_keyboards.car_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'car-2-a')
@router.callback_query(F.data == 'car-2-b')
@router.callback_query(F.data == 'car-2-c')
@router.callback_query(F.data == 'car-2-d')
async def car_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'car-2-a': False,
        'car-2-b': False,
        'car-2-c': True,
        'car-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Что такое трансмиссия?\n\n
a) Устройство для охлаждения двигателя.\n
b) Устройство, передающее крутящий момент от ДВС колесам.\n
c) Система управления автомобилем.\n
d) Элемент кузова автомобиля.''',
                                      reply_markup=inline_keyboards.car_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'car-3-a')
@router.callback_query(F.data == 'car-3-b')
@router.callback_query(F.data == 'car-3-c')
@router.callback_query(F.data == 'car-3-d')
async def car_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'car-3-a': False,
        'car-3-b': True,
        'car-3-c': False,
        'car-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Какая подвеска установлена на передней оси автомобиля в этом видео?\n\n
a) Независимая типа Макферсон.\n
b) Зависимая.\n
c) Рычажно-пружинная.\n
d) Полунезависимая.''',
                               reply_markup=inline_keyboards.car_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'car-4-a')
@router.callback_query(F.data == 'car-4-b')
@router.callback_query(F.data == 'car-4-c')
@router.callback_query(F.data == 'car-4-d')
async def car_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'car-4-a': True,
        'car-4-b': False,
        'car-4-c': False,
        'car-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Как называется система, которая используется для передачи крутящего момента от двигателя к колесам?\n\n
a) Ходовая часть.\n
b) Трансмиссия.\n
c) Подвеска.\n
d) Электрооборудование.''',
                                      reply_markup=inline_keyboards.car_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'car-5-a')
@router.callback_query(F.data == 'car-5-b')
@router.callback_query(F.data == 'car-5-c')
@router.callback_query(F.data == 'car-5-d')
async def car_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'car-5-a': False,
        'car-5-b': True,
        'car-5-c': False,
        'car-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Из чего состоит ходовая часть автомобиля?\n\n
a) Из колес и подвески.\n
b) Из мотора и трансмиссии.\n
c) Из кузова и подвески.\n
d) Из электронных систем управления.''',
                                      reply_markup=inline_keyboards.car_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'car-6-a')
@router.callback_query(F.data == 'car-6-b')
@router.callback_query(F.data == 'car-6-c')
@router.callback_query(F.data == 'car-6-d')
async def car_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'car-6-a': True,
        'car-6-b': False,
        'car-6-c': False,
        'car-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Сколько тактов включает один рабочий цикл 4-цилиндрового двигателя внутреннего сгорания?\n\n
a) 2.\n
b) 3.\n
c) 4.\n
d) 5.''',
                                      reply_markup=inline_keyboards.car_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'car-7-a')
@router.callback_query(F.data == 'car-7-b')
@router.callback_query(F.data == 'car-7-c')
@router.callback_query(F.data == 'car-7-d')
async def car_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'car-7-a': False,
        'car-7-b': False,
        'car-7-c': True,
        'car-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какую роль выполняет сцепление в переднеприводной трансмиссии?\n\n
a) Охлаждает двигатель.\n
b) Управляет направлением движения.\n
c) Передает крутящий момент от двигателя на коробку передач.\n
d) Поддерживает устойчивость автомобиля.''',
                                      reply_markup=inline_keyboards.car_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'car-8-a')
@router.callback_query(F.data == 'car-8-b')
@router.callback_query(F.data == 'car-8-c')
@router.callback_query(F.data == 'car-8-d')
async def car_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'car-8-a': False,
        'car-8-b': False,
        'car-8-c': True,
        'car-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Какая часть автомобиля принимает на себя нагрузки, возникающие при его движении?\n\n
a) Система управления.\n
b)Ходовая часть.\n
c) Несущая система.\n
d) Трансмиссия.''',
                                      reply_markup=inline_keyboards.car_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'car-9-a')
@router.callback_query(F.data == 'car-9-b')
@router.callback_query(F.data == 'car-9-c')
@router.callback_query(F.data == 'car-9-d')
async def car_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'car-9-a': False,
        'car-9-b': True,
        'car-9-c': False,
        'car-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Какая часть трансмиссии отвечает за временное разъединение двигателя и трансмиссии?\n\n
a) Главная передача.\n
b) Дифференциал.\n
c) Раздаточная коробка.\n
d) Сцепление.''',
                                      reply_markup=inline_keyboards.car_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'car-10-a')
@router.callback_query(F.data == 'car-10-b')
@router.callback_query(F.data == 'car-10-c')
@router.callback_query(F.data == 'car-10-d')
async def car_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'car-10-a': False,
        'car-10-b': False,
        'car-10-c': False,
        'car-10-d': True,
    }

    if dict_to_check_progress[callback.from_user.id] == 10:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 10:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='car_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 9 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 11

        if user_score >= 9:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/10.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=reply_keyboards.choose_course()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/10.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 9 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.usr_vo_avto()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_car_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_car(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()


@router.callback_query(F.data == 'get_me_to_ac_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        test_type = callback.data.split('_')[-1]
        # Проверяем прохождение теста
        if sqlite_funcs.check_user_test(callback.from_user.id, test_column=f'{test_type}_pass'):
            await callback.answer(text=f'Вы уже проходили тест по {test_type.replace("_","")}!', show_alert=True)
        else:
            # Добавляем пользователя, если его нет в базе
            if not sqlite_funcs.check_user(callback.from_user.id):
                sqlite_funcs.adding_users(tg_id=callback.from_user.id, name=callback.from_user.first_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id,
                                    text=f'Юзер начал проходить тест по кондиционеру: {callback.from_user.first_name}')
            await bot.send_message(chat_id=admin_id1,
                                    text=f'Юзер начал проходить тест по кондиционеру: {callback.from_user.first_name}')

            # Инициализация прогресса пользователя
            dict_to_check_progress[callback.from_user.id] = 1
            users[callback.from_user.id] = 0

            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!",
                )

        await callback.message.answer(text='''1. Какие основные функции выполняет автокондиционер в автомобиле?\n\n
a) Охлаждение воздуха в салоне.\n
b) Увлажнение воздуха.\n
c) Очистка воздуха от пыли.\n
d) Подогрев воздуха.''',
                                      reply_markup=inline_keyboards.ac_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'ac-1-a')
@router.callback_query(F.data == 'ac-1-b')
@router.callback_query(F.data == 'ac-1-c')
@router.callback_query(F.data == 'ac-1-d')
async def ac_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-1-a': True,
        'ac-1-b': False,
        'ac-1-c': False,
        'ac-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какие компоненты являются частью автокондиционера?\n\n
a) Компрессор.\n
b) Испаритель.\n
c) Конденсатор.\n
d) Все вышеперечисленные.''',
                                      reply_markup=inline_keyboards.ac_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-2-a')
@router.callback_query(F.data == 'ac-2-b')
@router.callback_query(F.data == 'ac-2-c')
@router.callback_query(F.data == 'ac-2-d')
async def ac_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-2-a': False,
        'ac-2-b': False,
        'ac-2-c': False,
        'ac-2-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Что происходит в испарителе автокондиционера?\n\n
a) Происходит сжатие хладагента.\n
b) Хладагент переходит из жидкого состояния в газообразное.\n
c) Происходит охлаждение воздуха.\n
d) Хладагент конденсируется.''',
                                      reply_markup=inline_keyboards.ac_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-3-a')
@router.callback_query(F.data == 'ac-3-b')
@router.callback_query(F.data == 'ac-3-c')
@router.callback_query(F.data == 'ac-3-d')
async def ac_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-3-a': False,
        'ac-3-b': True,
        'ac-3-c': False,
        'ac-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Какой тип хладагента обычно используется в автомобильных кондиционерах?\n\n
a) R22.\n
b) R134a.\n
c) R1234yf.\n
d) R404a.''',
                               reply_markup=inline_keyboards.ac_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-4-a')
@router.callback_query(F.data == 'ac-4-b')
@router.callback_query(F.data == 'ac-4-c')
@router.callback_query(F.data == 'ac-4-d')
async def ac_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-4-b': True,
        'ac-4-c': True,
        'ac-4-a': False,
        'ac-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Как можно выявить утечку хладагента в системе автокондиционирования?\n\n
a) Путем визуального осмотра системы.\n
b) С помощью специального прибора для детекции утечек.\n
c) С помощью УФ-лампы.\n
d) Все вышеперечисленное.''',
                                      reply_markup=inline_keyboards.ac_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-5-a')
@router.callback_query(F.data == 'ac-5-b')
@router.callback_query(F.data == 'ac-5-c')
@router.callback_query(F.data == 'ac-5-d')
async def ac_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-5-a': False,
        'ac-5-b': False,
        'ac-5-c': False,
        'ac-5-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Как можно изменить направление потока воздуха в салоне с помощью автокондиционера?\n\n
a) Путем переключения работы кондиционера.\n
b) Изменением направления потока воздуха.\n
c) Регулировкой скорости вентилятора.\n
d) Настройкой температуры.''',
                                      reply_markup=inline_keyboards.ac_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-6-a')
@router.callback_query(F.data == 'ac-6-b')
@router.callback_query(F.data == 'ac-6-c')
@router.callback_query(F.data == 'ac-6-d')
async def ac_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-6-a': True,
        'ac-6-b': True,
        'ac-6-c': False,
        'ac-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Какова функция компрессора в системе кондиционирования?\n\n
a) Охлаждение сжатого воздуха.\n
b) Нагрев воздуха в салоне.\n
c) Сжатие и циркуляция хладагента.\n
d) Подача воздуха в салон.''', reply_markup=inline_keyboards.ac_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-7-a')
@router.callback_query(F.data == 'ac-7-b')
@router.callback_query(F.data == 'ac-7-c')
@router.callback_query(F.data == 'ac-7-d')
async def ac_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-7-a': False,
        'ac-7-b': False,
        'ac-7-c': True,
        'ac-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какие меры предосторожности следует соблюдать при работе с автокондиционером?\n\n
a) Работать в защитных очках и перчатках.\n
b) Не разбирать систему автокондиционирования без подключения специальной станции.\n
c) Следить за уровнем хладагента в системе.\n
d) Все вышеперечисленное.''', reply_markup=inline_keyboards.ac_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-8-a')
@router.callback_query(F.data == 'ac-8-b')
@router.callback_query(F.data == 'ac-8-c')
@router.callback_query(F.data == 'ac-8-d')
async def ac_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-8-a': False,
        'ac-8-b': False,
        'ac-8-c': False,
        'ac-8-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Каким инструментом можно обрезать трубку перед заменой участка?\n\n
a) Зубило.\n
b) Болгарка.\n
c) Труборез.\n
d) Нажовка.''', reply_markup=inline_keyboards.ac_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-9-a')
@router.callback_query(F.data == 'ac-9-b')
@router.callback_query(F.data == 'ac-9-c')
@router.callback_query(F.data == 'ac-9-d')
async def ac_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-9-a': False,
        'ac-9-b': False,
        'ac-9-c': True,
        'ac-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Какие основные шаги необходимо выполнить непосредственно перед пайкой участка на трубке системы кондиционирования?\n\n
a) Очистить трубку от окислов и загрязнений, обеспечить правильное соединение участков.\n
b) Демонтировать все резиновые уплотнения и датчики.\n
c) Подготовить паяльник, припой и другие материалы, необходимые для пайки.\n
d) Все вышеперечисленные.''', reply_markup=inline_keyboards.ac_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-10-a')
@router.callback_query(F.data == 'ac-10-b')
@router.callback_query(F.data == 'ac-10-c')
@router.callback_query(F.data == 'ac-10-d')
async def ac_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-10-a': False,
        'ac-10-b': False,
        'ac-10-c': False,
        'ac-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Какой шаг предшествует заправке автокондиционера новым хладагентом?\n\n
a) Проверка уровня масла в двигателе.\n
b) Проверка цвета антифриза.\n
c) Проверка системы на наличие утечек.\n
d) Проверка давления в шинах.''', reply_markup=inline_keyboards.ac_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-11-a')
@router.callback_query(F.data == 'ac-11-b')
@router.callback_query(F.data == 'ac-11-c')
@router.callback_query(F.data == 'ac-11-d')
async def ac_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-11-a': False,
        'ac-11-b': False,
        'ac-11-c': True,
        'ac-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Каким образом происходит пайка участка на трубке системы кондиционирования?\n\n
a) Трубки соединяются и нагреваются феном, после чего на соединение наносится припой.\n
b) Паяльник вставляется внутрь трубки для пайки, после чего происходит нагрев и соединение трубок.\n
c) Трубки нагреваются горелкой, после чего на соединение наносится припой.\n
d) Трубки соединяются и обжимаются специальным инструментом, не требующим нагрева.''',
                                      reply_markup=inline_keyboards.ac_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-12-a')
@router.callback_query(F.data == 'ac-12-b')
@router.callback_query(F.data == 'ac-12-c')
@router.callback_query(F.data == 'ac-12-d')
async def ac_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-12-a': False,
        'ac-12-b': False,
        'ac-12-c': True,
        'ac-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Какие методы ремонта трубок существуют?\n\n
а) Замена на шланг\n
b) Вставка\n
c) Ремонт фланца\n
d) Все вышеперечисленные''',
                                      reply_markup=inline_keyboards.ac_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-13-a')
@router.callback_query(F.data == 'ac-13-b')
@router.callback_query(F.data == 'ac-13-c')
@router.callback_query(F.data == 'ac-13-d')
async def ac_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-13-a': False,
        'ac-13-b': False,
        'ac-13-c': False,
        'ac-13-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Какая должна быть температура воздуха из кондиционера после его заправки?\n\n
a) 10 градусов Цельсия.\n
b) 18 градусов Цельсия.\n
c) 25 градусов Цельсия.\n
d) 30 градусов Цельсия.''',
                                      reply_markup=inline_keyboards.ac_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-14-a')
@router.callback_query(F.data == 'ac-14-b')
@router.callback_query(F.data == 'ac-14-c')
@router.callback_query(F.data == 'ac-14-d')
async def ac_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-14-a': True,
        'ac-14-b': False,
        'ac-14-c': False,
        'ac-14-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Сколько занимает процедура диагностирования автокондиционера?\n\n
a) От 1 до 2 дней.\n
b) 23 часа.\n
c) 30–60 минут.\n
d) Не более 5 минут.''',
                                      reply_markup=inline_keyboards.ac_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-15-a')
@router.callback_query(F.data == 'ac-15-b')
@router.callback_query(F.data == 'ac-15-c')
@router.callback_query(F.data == 'ac-15-d')
async def ac_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-15-a': False,
        'ac-15-b': False,
        'ac-15-c': True,
        'ac-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Сколько масла должно быть в системе автокондиционирования?\n\n
a) 50-100 мл.\n
b) 130-250 мл.\n
c) 300 мл.\n
d) 400 мл.''',
                                      reply_markup=inline_keyboards.ac_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-16-a')
@router.callback_query(F.data == 'ac-16-b')
@router.callback_query(F.data == 'ac-16-c')
@router.callback_query(F.data == 'ac-16-d')
async def ac_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-16-a': False,
        'ac-16-b': True,
        'ac-16-c': False,
        'ac-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Что происходит с хладагентом в рабочем цикле автокондиционера, выбрать верное утверждение?\n\n
a) Сжимается и испаряется.\n
b) Испаряется и конденсируется.\n
c) Охлаждается и снова сжимается.\n
d) Нагревается и замерзает.''',
                                      reply_markup=inline_keyboards.ac_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-17-a')
@router.callback_query(F.data == 'ac-17-b')
@router.callback_query(F.data == 'ac-17-c')
@router.callback_query(F.data == 'ac-17-d')
async def ac_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-17-a': False,
        'ac-17-b': True,
        'ac-17-c': False,
        'ac-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Для определения утечек хладагента используется:\n\n
a) Молькотлитель.\n
b) Детектор лжи.\n
c) Клаксон.\n
d) Детектор утечки.''',
                                      reply_markup=inline_keyboards.ac_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-18-a')
@router.callback_query(F.data == 'ac-18-b')
@router.callback_query(F.data == 'ac-18-c')
@router.callback_query(F.data == 'ac-18-d')
async def ac_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-18-a': False,
        'ac-18-b': False,
        'ac-18-c': False,
        'ac-18-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Можно ли смешивать данные масла PAG и POE?\n\n
a) Можно.\n
b) Нельзя.\n
c) Можно, если добавить краску.\n
d) Всегда смешивал и ничего.''',
                                      reply_markup=inline_keyboards.ac_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-19-a')
@router.callback_query(F.data == 'ac-19-b')
@router.callback_query(F.data == 'ac-19-c')
@router.callback_query(F.data == 'ac-19-d')
async def ac_19_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-19-a': False,
        'ac-19-b': True,
        'ac-19-c': False,
        'ac-19-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''20. Какие могут быть основные причины повреждений трубок системы кондиционирования автомобиля?\n\n
a) Механические повреждения, коррозия, неправильная эксплуатация.\n
b) Перегрев двигателя, низкий уровень масла.\n
c) Неправильная работа выхлопной системы.\n
d) Все вышеперечисленное.''',
                                      reply_markup=inline_keyboards.ac_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-20-a')
@router.callback_query(F.data == 'ac-20-b')
@router.callback_query(F.data == 'ac-20-c')
@router.callback_query(F.data == 'ac-20-d')
async def ac_20_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ac-20-a': True,
        'ac-20-b': False,
        'ac-20-c': False,
        'ac-20-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 20:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 21:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='ac_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 21

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/20.\n"
            f"Приступить к другим курсам.",
            reply_markup=reply_keyboards.choose_course()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/20.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.graphics_to_continue()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_ac_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_ac(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.message(F.text == 'ПСП')
async def show_users(message: Message):
    users_to_show = sqlite_funcs.import_users()
    await message.answer(text='Вот список юзеров:\n')
    for elem in users_to_show:
        await message.answer(f'{elem}')


@router.message(F.text.startswith('Измени тест по кондею у юзера:'))
async def change_opportunity_ac(message: Message):
    sqlite_funcs.change_opportunity_for_ac_test(message.text[28::])
    await message.answer(text='Обнулили тест для данного Юзера')

@router.message(F.text.startswith('Измени тест по правкам у юзера:'))
async def change_opportunity_pr(message: Message):
    sqlite_funcs.change_opportunity_for_pr_test(message.text[28::])
    await message.answer(text='Обнулили тест для данного Юзера')

@router.message(F.text)
async def any_text(message: Message):
    await message.answer(text='Я вас не понимаю...\n\nВывожу главное меню:',
                         reply_markup=reply_keyboards.choose_course())

@router.callback_query(F.data == "pravka_diskov_1")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Правка дисков. Часть 1](https://disk.yandex.ru/i/dZ537pX0FSGMIA)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_pr_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "pravka_diskov_2")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Правка дисков. Часть 2](https://disk.yandex.ru/i/ggLRRmeRRbxuhw)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_pr_1_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "pravka_diskov_3")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Правка дисков. Часть 3](https://disk.yandex.ru/i/1g95Hat0WIUMLg)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_pr_2_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "pravka_diskov_4")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Правка дисков. Часть 4](https://disk.yandex.ru/i/PP5tHXcjL3LaUw)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_pr_3_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "pravka_diskov_5")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Правка дисков. Часть 5](https://disk.yandex.ru/i/Yz_iQmuzaxHedg)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_pr_4_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "treningi")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Тренинг с сотрудниками](https://disk.yandex.ru/i/nNrJiNdWusCe1g)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_tr_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "balancirovka")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Балансировачный станок](https://disk.yandex.ru/i/i-_n6fPi_KQgZA)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_ob_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "stanok_shinka")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Станок для шиномонтажа](https://disk.yandex.ru/i/s4xQF9oAUi-8eA)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_st_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "stanok_pravok")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Станок для правок](https://disk.yandex.ru/i/l9kja_XkpjjUug)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_st_pr_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "history")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [История шин](https://disk.yandex.ru/i/kRvD6KKITyvqhQ)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_id_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "trials")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Испытания в лаборатории](https://disk.yandex.ru/i/1zbpDgRI6SUp1w)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_is_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "parametrdisk")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Параметры дисков](https://disk.yandex.ru/i/HKOugMR8SWlW-g)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_pr_ds_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "kolcadldiskov")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Кольца для литых дисков](https://disk.yandex.ru/i/AgiCt32KOMp19w)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_kd_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "porez")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Ремонт колеса-порез](https://disk.yandex.ru/i/LtELuRV2FthLEA)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_pz_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "snyatie")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Снятие и установка колеса на автомобиль](https://disk.yandex.ru/i/xJ9rv2NCq2nTnQ)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_sn_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "sborka")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Сборка и разборка на шиномонтажном станке](https://disk.yandex.ru/i/zweKsS49uuolbw)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_sb_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "remont")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Ремонт прокола бескамерного колеса](https://disk.yandex.ru/i/wR-t1_LWRFtkNQ)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_rn_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "balance")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Балансировка колеса](https://disk.yandex.ru/i/ISJfgmSwdm6_wQ)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_bc_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "prodaja")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Допродажи](https://disk.yandex.ru/i/Y4zvqgsb-f0iTg)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_pj_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "litorkovka")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [В чем отличие Литья от Ковки](https://disk.yandex.ru/i/KSnJrN5IOfVN3w)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_ot_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "proizvodstvo")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Как делают шины. Производство и устройство](https://disk.yandex.ru/i/B5Z6F0YPLeTGCQ)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_lt_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "kolesaishini")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Колеса - шины](https://disk.yandex.ru/i/uC7SIi2O17XpIw)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_ki_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "leftandright")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Левые и правы шины. Асимметричные и направленные. Разница](https://disk.yandex.ru/i/cnFRCaHmOCZJRA)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_lr_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "markirovkadiskov")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Маркировка шин. Часть 1](https://disk.yandex.ru/i/ibO6kdhD2FzyWA)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_mk_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "markirovkashin")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Маркировка шин. Часть 2](https://disk.yandex.ru/i/ZijIN5UhHUurWA)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_ms_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "shinkadisk")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Шинка диск](https://disk.yandex.ru/i/P1pCq81OGAy0Sw)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_sd_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == "studorstudd")
async def combined_action(callback: CallbackQuery):
    # Отправляем ссылку
    await callback.message.answer(
        "Перейдите по ссылке: [Шинка STUDDED ИЛИ STUDABLE в чем отличия шиповки](https://disk.yandex.ru/i/ZQHR56jymSJj7A)",
        parse_mode="Markdown"
    )
    await asyncio.sleep(5)  # Задержка
    # Спрашиваем о тесте
    await callback.message.answer(
        "Хотите пройти тест?",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Да, начать тест", callback_data="get_me_to_dd_exam")]
            ]
        )
    )
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_pr_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='pr_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по правкам!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Какая цель правки колесного диска?\n\n
a) Улучшение внешнего вида диска.\n
b) Устранение механических повреждений для восстановления геометрии диска.\n
c) Увеличение прочности материала диска.\n
d) Уменьшение веса диска.''',
                                      reply_markup=inline_keyboards.pr_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'pr-1-a')
@router.callback_query(F.data == 'pr-1-b')
@router.callback_query(F.data == 'pr-1-c')
@router.callback_query(F.data == 'pr-1-d')
async def pr_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-1-a': True,
        'pr-1-b': False,
        'pr-1-c': False,
        'pr-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какие признаки могут указывать на необходимость правки диска?\n\n
a) Наличие видимых трещин и деформаций.\n
b) Появление ржавчины.\n
c) Увеличение толщины диска.\n
d) Сильный блеск поверхности.''',
                                      reply_markup=inline_keyboards.pr_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-2-a')
@router.callback_query(F.data == 'pr-2-b')
@router.callback_query(F.data == 'pr-2-c')
@router.callback_query(F.data == 'pr-2-d')
async def pr_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-2-a': False,
        'pr-2-b': True,
        'pr-2-c': False,
        'pr-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Что важно учитывать при выборе инструмента для правки диска?\n\n
a) Размер инструмента и его соответствие повреждениям.\n
b) Тип материала, из которого сделан диск.\n
c) Сила и продолжительность воздействия.\n
d) Цвет инструмента.''',
                                      reply_markup=inline_keyboards.pr_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-3-a')
@router.callback_query(F.data == 'pr-3-b')
@router.callback_query(F.data == 'pr-3-c')
@router.callback_query(F.data == 'pr-3-d')
async def pr_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-3-a': False,
        'pr-3-b': False,
        'pr-3-c': True,
        'pr-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Что происходит, если при правке диска не учитывать возможные трещины?\n\n
a) Трещины могут увеличиться и привести к разрушению диска.\n
b) Трещины быстро заживают под давлением.\n
c) Диск становится легче и прочнее.\n
d) Повреждения становятся менее заметными.''',
                               reply_markup=inline_keyboards.pr_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-4-a')
@router.callback_query(F.data == 'pr-4-b')
@router.callback_query(F.data == 'pr-4-c')
@router.callback_query(F.data == 'pr-4-d')
async def pr_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-4-b': True,
        'pr-4-c': False,
        'pr-4-a': False,
        'pr-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Как важно соблюдать равномерное давление при правке диска?\n\n
a) Это не имеет значения, главное — визуальная корректировка.\n
b) Равномерное давление важно для предотвращения дополнительных повреждений и деформаций.\n
c) Это важно только при правке алюминиевых дисков.\n
d) Давление следует уменьшать в центре повреждения.''',
                                      reply_markup=inline_keyboards.pr_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-5-a')
@router.callback_query(F.data == 'pr-5-b')
@router.callback_query(F.data == 'pr-5-c')
@router.callback_query(F.data == 'pr-5-d')
async def pr_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-5-a': False,
        'pr-5-b': True,
        'pr-5-c': False,
        'pr-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Каковы последствия неправильной правки колесного диска?\n\n
a) Диск может стать более подверженным деформации в будущем.\n
b) Диск будет значительно легче.\n
c) Диск может приобрести дополнительные повреждения, но это не опасно.\n
d) Все повреждения будут устранены без последствий.''',
                                      reply_markup=inline_keyboards.pr_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-6-a')
@router.callback_query(F.data == 'pr-6-b')
@router.callback_query(F.data == 'pr-6-c')
@router.callback_query(F.data == 'pr-6-d')
async def pr_6_note(callback: CallbackQuery, bot: Bot):
    correct_answers = {
        'pr-6-a': True,
        'pr-6-b': False,
        'pr-6-c': False,
        'pr-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Какая из следующих процедур является первым шагом в правке диска?\n\n
a) Обработка краской для улучшения внешнего вида.\n
b) Очистка привалочной поверхности от грязи и загрязнений.\n
c) Установка нового колеса на автомобиль.\n
d) Проверка баланса колеса.''',
                                      reply_markup=inline_keyboards.pr_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-7-a')
@router.callback_query(F.data == 'pr-7-b')
@router.callback_query(F.data == 'pr-7-c')
@router.callback_query(F.data == 'pr-7-d')
async def pr_7_note(callback: CallbackQuery, bot: Bot):
    correct_answers = {
        'pr-7-a': False,
        'pr-7-b': True,
        'pr-7-c': False,
        'pr-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какие инструменты часто используют для правки поврежденных дисков?\n\n
a) Набор сверл.\n
b) Правочный станок и молоток.\n
c) Напильник и шлифовальная машинка.\n
d) Дрель и гайковерт.''',
                                      reply_markup=inline_keyboards.pr_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-8-a')
@router.callback_query(F.data == 'pr-8-b')
@router.callback_query(F.data == 'pr-8-c')
@router.callback_query(F.data == 'pr-8-d')
async def pr_8_note(callback: CallbackQuery, bot: Bot):
    correct_answers = {
        'pr-8-a': False,
        'pr-8-b': True,
        'pr-8-c': False,
        'pr-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Какую роль играет разметка повреждений при правке диска?\n\n
a) Помогает точнее определить участки, требующие коррекции.\n
b) Уменьшает вероятность повреждения края диска.\n
c) Способствует лучшему сцеплению.\n
d) Обеспечивает долговечность колеса.''',
                                      reply_markup=inline_keyboards.pr_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-9-a')
@router.callback_query(F.data == 'pr-9-b')
@router.callback_query(F.data == 'pr-9-c')
@router.callback_query(F.data == 'pr-9-d')
async def pr_9_note(callback: CallbackQuery, bot: Bot):
    correct_answers = {
        'pr-9-a': True,
        'pr-9-b': False,
        'pr-9-c': False,
        'pr-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Как часто следует проверять баланс колеса после правки?\n\n
a) Только если колесо имеет значительные повреждения.\n
b) После каждой правки, чтобы избежать вибрации при движении.\n
c) Балансировка не требуется после правки.\n
d) Балансировка проводится только в случае смены шины.''',
                                      reply_markup=inline_keyboards.pr_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-10-a')
@router.callback_query(F.data == 'pr-10-b')
@router.callback_query(F.data == 'pr-10-c')
@router.callback_query(F.data == 'pr-10-d')
async def pr_10_note(callback: CallbackQuery, bot: Bot):
    correct_answers = {
        'pr-10-a': False,
        'pr-10-b': True,
        'pr-10-c': False,
        'pr-10-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Почему важно устранять повреждения на внутренней поверхности диска?\n\n
a) Это улучшает внешний вид колеса.\n
b) Внутренние повреждения могут привести к дополнительным нагрузкам и повреждениям во время движения.\n
c) Внешняя поверхность важнее, чем внутренняя.\n
d) Повреждения внутри диска не влияют на его работу.''',
                                      reply_markup=inline_keyboards.pr_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-11-a')
@router.callback_query(F.data == 'pr-11-b')
@router.callback_query(F.data == 'pr-11-c')
@router.callback_query(F.data == 'pr-11-d')
async def pr_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-11-a': False,
        'pr-11-b': True,
        'pr-11-c': False,
        'pr-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Что может случиться, если при правке не учесть состояние краев диска?\n\n
a) Диск может потерять форму и стать неустойчивым.\n
b) Это может вызвать повреждения шины при установке.\n
c) Повреждения могут привести к ухудшению сцепления с дорогой.\n
d) Установить шину будет невозможно.''',
                                      reply_markup=inline_keyboards.pr_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-12-a')
@router.callback_query(F.data == 'pr-12-b')
@router.callback_query(F.data == 'pr-12-c')
@router.callback_query(F.data == 'pr-12-d')
async def pr_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-12-a': False,
        'pr-12-b': True,
        'pr-12-c': False,
        'pr-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Какую роль играет использование разных цветов восковых мелков при разметке повреждений?\n\n
а) Это помогает выделить повреждения и ускоряет процесс правки.\n
b) Мелки необходимы для окраски поверхности диска.\n
c) Используются только для эстетической обработки.\n
d) Это нужно для уменьшения шума при правке.''',
                                      reply_markup=inline_keyboards.pr_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-13-a')
@router.callback_query(F.data == 'pr-13-b')
@router.callback_query(F.data == 'pr-13-c')
@router.callback_query(F.data == 'pr-13-d')
async def pr_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-13-a': True,
        'pr-13-b': False,
        'pr-13-c': False,
        'pr-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Каковы основные этапы правки поврежденного диска?\n\n
a) Снятие напряжения, корректировка формы и окончательная проверка.\n
b) Покраска, шлифовка и балансировка.\n
c) Установка нового покрытия.\n
d) Измерение диаметра и установка на машину.''',
                                      reply_markup=inline_keyboards.pr_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-14-a')
@router.callback_query(F.data == 'pr-14-b')
@router.callback_query(F.data == 'pr-14-c')
@router.callback_query(F.data == 'pr-14-d')
async def pr_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-14-a': True,
        'pr-14-b': False,
        'pr-14-c': False,
        'pr-14-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Что может повлиять на скорость и качество правки диска?\n\n
a) Тип повреждения и материал диска.\n
b) Количество использованных инструментов.\n
c) Сила давления на инструмент.\n
d) Цвет диска.''',
                                      reply_markup=inline_keyboards.pr_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-15-a')
@router.callback_query(F.data == 'pr-15-b')
@router.callback_query(F.data == 'pr-15-c')
@router.callback_query(F.data == 'pr-15-d')
async def pr_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-15-a': True,
        'pr-15-b': False,
        'pr-15-c': False,
        'pr-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Как важно проверять диск на больших оборотах после правки?\n\n
a) Это не нужно делать, достаточно визуальной проверки.\n
b) Это помогает выявить вибрацию и недочеты в правке.\n
c) Проверка на больших оборотах ускоряет процесс.\n
d) Это важно только для крупных повреждений.''',
                                      reply_markup=inline_keyboards.pr_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-16-a')
@router.callback_query(F.data == 'pr-16-b')
@router.callback_query(F.data == 'pr-16-c')
@router.callback_query(F.data == 'pr-16-d')
async def pr_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-16-a': False,
        'pr-16-b': True,
        'pr-16-c': False,
        'pr-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Что следует делать, если на диске были выявлены глубокие трещины?\n\n
a) Прекратить правку и заменить диск.\n
b) Применить дополнительные методы правки для восстановления.\n
c) Пропустить повреждение, так как оно незначительное.\n
d) Игнорировать, так как трещины не влияют на функциональность.''',
                                      reply_markup=inline_keyboards.pr_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-17-a')
@router.callback_query(F.data == 'pr-17-b')
@router.callback_query(F.data == 'pr-17-c')
@router.callback_query(F.data == 'pr-17-d')
async def pr_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-17-a': True,
        'pr-17-b': False,
        'pr-17-c': False,
        'pr-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Какие повреждения диска нельзя исправить с помощью правки:\n\n
a) Мелкие царапины и вмятины.\n
b) Глубокие трещины и деформации, нарушающие структуру диска.\n
c) Несоосность колес.\n
d) Повреждения из-за коррозии.''',
                                      reply_markup=inline_keyboards.pr_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-18-a')
@router.callback_query(F.data == 'pr-18-b')
@router.callback_query(F.data == 'pr-18-c')
@router.callback_query(F.data == 'pr-18-d')
async def pr_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-18-a': False,
        'pr-18-b': True,
        'pr-18-c': False,
        'pr-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Что важно помнить при правке литых дисков?\n\n
a) Литые диски легче править, чем стальные.\n
b) Литые диски могут быть более подвержены трещинам и разрушению при неаккуратной правке.\n
c) Литые диски всегда можно исправить  без риска повреждений.\n
d) Литые диски не требуют особого внимания при правке.''',
                                      reply_markup=inline_keyboards.pr_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-19-a')
@router.callback_query(F.data == 'pr-19-b')
@router.callback_query(F.data == 'pr-19-c')
@router.callback_query(F.data == 'pr-19-d')
async def pr_19_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr-19-a': False,
        'pr-19-b': True,
        'pr-19-c': False,
        'pr-19-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''20. Почему важно правильно снимать напряжение с диска при его правке?\n\n
a) Это позволяет избежать перегрева материала.\n
b) Это предотвращает появление трещин и разрушение диска.\n
c) Это помогает сделать диск легче.\n
d) Это улучшает внешний вид и блеск поверхности.''',
                                      reply_markup=inline_keyboards.pr_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr-20-a')
@router.callback_query(F.data == 'pr-20-b')
@router.callback_query(F.data == 'pr-20-c')
@router.callback_query(F.data == 'pr-20-d')
async def pr_20_note(callback: CallbackQuery, bot: Bot):


    correct_answers = {
        'pr-20-a': False,
        'pr-20-b': True,
        'pr-20-c': False,
        'pr-20-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 20:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 20:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='pr_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 21

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/20.\n"
            f"Теперь вы можете перейти к следующему уроку.",
            reply_markup=inline_keyboards.urok_po_pravkam_1()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/20.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.pravki_zanovo_1()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_pr_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_pr(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_pr_1_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='pr_exam_pass_1'):
            await callback.answer(text='Вы уже проходили тест по правкам!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. На сколько положений возможно двигать мост по горизонтали?\n\n
a) 2 положения.\n
b) 3 положения.\n
c) 4 положения.\n
d) 5 положений.''',
                                      reply_markup=inline_keyboards.pr_1_1_answer())
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'pr_1-1-a')
@router.callback_query(F.data == 'pr_1-1-b')
@router.callback_query(F.data == 'pr_1-1-c')
@router.callback_query(F.data == 'pr_1-1-d')
async def pr_1_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_1-1-a': False,
        'pr_1-1-b': False,
        'pr_1-1-c': True,
        'pr_1-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Для чего нужен дополнительный упор под цилиндр?\n\n
a) Для стабилизации оснастки.\n
b) Для усиления давления на диск.\n
c) Для крепления цилиндра и усиления воздействия на повреждение.\n
d) Для предотвращения смещения моста.''',
                                      reply_markup=inline_keyboards.pr_1_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_1-2-a')
@router.callback_query(F.data == 'pr_1-2-b')
@router.callback_query(F.data == 'pr_1-2-c')
@router.callback_query(F.data == 'pr_1-2-d')
async def pr_1_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_1-2-a': False,
        'pr_1-2-b': False,
        'pr_1-2-c': True,
        'pr_1-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Для чего нужен верхний дополнительный цилиндр?\n\n
a) Для увеличения мощности правки.\n
b) Для равномерного распределения давления на диск.\n
c) Для работы с крупными повреждениями.\n
d) Для установки дополнительного оборудования.''',
                                      reply_markup=inline_keyboards.pr_1_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_1-3-a')
@router.callback_query(F.data == 'pr_1-3-b')
@router.callback_query(F.data == 'pr_1-3-c')
@router.callback_query(F.data == 'pr_1-3-d')
async def pr_1_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_1-3-a': False,
        'pr_1-3-b': True,
        'pr_1-3-c': False,
        'pr_1-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Какой принцип закраины исполнен на данном диске?\n\n
a) Внешняя закраина с полочкой, похожая на внутреннюю.\n
b) Внешняя закраина с округлым краем.\n
c) Внутренняя закраина с полочкой.\n
d) Внешняя закраина с прямым краем.''',
                               reply_markup=inline_keyboards.pr_1_4_answer(), chat_id=callback.from_user.id)
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_1-4-a')
@router.callback_query(F.data == 'pr_1-4-b')
@router.callback_query(F.data == 'pr_1-4-c')
@router.callback_query(F.data == 'pr_1-4-d')
async def pr_1_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_1-4-a': True,
        'pr_1-4-b': False,
        'pr_1-4-c': False,
        'pr_1-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Какие возможности открываются при использовании моста?\n\n
a) Возможность работы с дисками разных размеров.\n
b) Установка дополнительных цилиндров и упоров для усиления воздействия и точности правки.\n
c) Увеличение давления на диск.\n
d) Уменьшение времени правки.''',
                                      reply_markup=inline_keyboards.pr_1_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_1-5-a')
@router.callback_query(F.data == 'pr_1-5-b')
@router.callback_query(F.data == 'pr_1-5-c')
@router.callback_query(F.data == 'pr_1-5-d')
async def pr_1_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_1-5-a': False,
        'pr_1-5-b': True,
        'pr_1-5-c': False,
        'pr_1-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 5:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='pr_exam_pass_1',  # Убедитесь, что столбец существует
                status=1 if user_score >= 4 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 6

        if user_score >= 4:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/5.\n"
            f"Теперь вы можете перейти к следующему уроку.",
            reply_markup=inline_keyboards.urok_po_pravkam_2())

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/5.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 4 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.pravki_zanovo_2()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_pr_test_1(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_pr_1(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_pr_2_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='pr_exam_pass_2'):
            await callback.answer(text='Вы уже проходили тест по правкам!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Какой диаметр и ширина диска, о котором идет речь в видео?\n\n
a) Диаметр 17, ширина 8.\n
b) Диаметр 15, ширина 7,5.\n
c) Диаметр 16, ширина 7.\n
d) Диаметр 15, ширина 8.''',
                                      reply_markup=inline_keyboards.pr_2_1_answer())
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'pr_2-1-a')
@router.callback_query(F.data == 'pr_2-1-b')
@router.callback_query(F.data == 'pr_2-1-c')
@router.callback_query(F.data == 'pr_2-1-d')
async def pr_2_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_2-1-a': False,
        'pr_2-1-b': True,
        'pr_2-1-c': False,
        'pr_2-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какая закраина на диске в этом видео?\n\n
a) Гладкая закраина.\n
b) Закраина с волнами.\n
c) Сложная закраина.\n
d) Закраина с углублением.''',
                                      reply_markup=inline_keyboards.pr_2_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_2-2-a')
@router.callback_query(F.data == 'pr_2-2-b')
@router.callback_query(F.data == 'pr_2-2-c')
@router.callback_query(F.data == 'pr_2-2-d')
async def pr_2_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_2-2-a': True,
        'pr_2-2-b': False,
        'pr_2-2-c': False,
        'pr_2-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Для чего нужно выбирать правильный угол при работе с диском?\n\n
a) Чтобы ускорить процесс правки.\n
b) Чтобы избежать повреждения диска и контролировать процесс правки.\n
c) Чтобы уменьшить нагрузку на оборудование.\n
d) Чтобы увеличить давление на диск.''',
                                      reply_markup=inline_keyboards.pr_2_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_2-3-a')
@router.callback_query(F.data == 'pr_2-3-b')
@router.callback_query(F.data == 'pr_2-3-c')
@router.callback_query(F.data == 'pr_2-3-d')
async def pr_2_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_2-3-a': False,
        'pr_2-3-b': True,
        'pr_2-3-c': False,
        'pr_2-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Для чего применяется технология с грузиками?\n\n
a) Для улучшения сцепления с дорогой.\n
b) Для предотвращения скольжения диска в процессе правки.\n
c) Для минимизации повреждения краски диска в процессе правки .\n
d) Для балансировки диска во время работы.''',
                               reply_markup=inline_keyboards.pr_2_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_2-4-a')
@router.callback_query(F.data == 'pr_2-4-b')
@router.callback_query(F.data == 'pr_2-4-c')
@router.callback_query(F.data == 'pr_2-4-d')
async def pr_2_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_2-4-a': False,
        'pr_2-4-b': False,
        'pr_2-4-c': True,
        'pr_2-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Какая особенность работы с грузиками?\n\n
a) Грузики могут сильно нагреваться.\n
b) Грузики могут скользить по поверхности диска.\n
c) Грузики используют для изменения диаметра диска.\n
d) Грузики не влияют на процесс правки.''',
                                      reply_markup=inline_keyboards.pr_2_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_2-5-a')
@router.callback_query(F.data == 'pr_2-5-b')
@router.callback_query(F.data == 'pr_2-5-c')
@router.callback_query(F.data == 'pr_2-5-d')
async def pr_2_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_2-5-a': False,
        'pr_2-5-b': True,
        'pr_2-5-c': False,
        'pr_2-5-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Что произойдет, если дать более маленькую точку опоры, перевернув грузик?\n\n
    a) Грузик будет двигаться быстрее.\n
    b) Увеличится точность правки.\n
    c) Уменьшится эффект скольжения за счет маленькой точки упора.\n
    d) Точность правки снизится.''',
                                      reply_markup=inline_keyboards.pr_2_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_2-6-a')
@router.callback_query(F.data == 'pr_2-6-b')
@router.callback_query(F.data == 'pr_2-6-c')
@router.callback_query(F.data == 'pr_2-6-d')
async def pr_2_6_note(callback: CallbackQuery, bot: Bot):
    correct_answers = {
        'pr_2-6-a': False,
        'pr_2-6-b': False,
        'pr_2-6-c': True,
        'pr_2-6-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. За счет чего можно изменить угол цилиндра?\n\n
        a) За счет изменения давления в цилиндре.\n
        b) За счет использования различных типов грузиков.\n
        c) За счет использования переходников и удлинителей.\n
        d) За счет изменения скорости вращения цилиндра.''',
                                      reply_markup=inline_keyboards.pr_2_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_2-7-a')
@router.callback_query(F.data == 'pr_2-7-b')
@router.callback_query(F.data == 'pr_2-7-c')
@router.callback_query(F.data == 'pr_2-7-d')
async def pr_2_7_note(callback: CallbackQuery, bot: Bot):
    correct_answers = {
        'pr_2-7-a': False,
        'pr_2-7-b': False,
        'pr_2-7-c': True,
        'pr_2-7-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 7:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 7:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='pr_exam_pass_2',  # Убедитесь, что столбец существует
                status=1 if user_score >= 6 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 8

        if user_score >= 6:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/7.\n"
            f"Теперь вы можете перейти к следующему уроку.",
                reply_markup=inline_keyboards.urok_po_pravkam_3()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/7.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 6 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.pravki_zanovo_2()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_pr_test_2(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_pr_2(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_pr_3_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='pr_exam_pass_3'):
            await callback.answer(text='Вы уже проходили тест по правкам!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Для чего нужно сначала аккуратно прощупывать диск?\n\n
a) Для того, чтобы определить толщину металла.\n
b) Для того, чтобы не лопнул диск.\n
c) Для оценки повреждений и выявления деформации.\n
d) Для того, чтобы определить место повреждения.''',
                                      reply_markup=inline_keyboards.pr_3_1_answer())
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'pr_3-1-a')
@router.callback_query(F.data == 'pr_3-1-b')
@router.callback_query(F.data == 'pr_3-1-c')
@router.callback_query(F.data == 'pr_3-1-d')
async def pr_3_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-1-a': False,
        'pr_3-1-b': True,
        'pr_3-1-c': False,
        'pr_3-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Для чего нужно ставить широкий ограничитель?\n\n
a) Для предотвращения перегрева диска.\n
b) Для того, чтобы равномерно распределить усилия при выравнивании.\n
c) Для фиксации внешней формы диска.\n
d) Для защиты окружающих деталей от повреждений.''',
                                      reply_markup=inline_keyboards.pr_3_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-2-a')
@router.callback_query(F.data == 'pr_3-2-b')
@router.callback_query(F.data == 'pr_3-2-c')
@router.callback_query(F.data == 'pr_3-2-d')
async def pr_3_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-2-a': False,
        'pr_3-2-b': True,
        'pr_3-2-c': False,
        'pr_3-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Для чего правочную площадку в данном видео ставят немного на искосок?\n\n
a) Чтобы избежать деформации самого инструмента.\n
b) Для более точного выравнивания центральной части диска.\n
c) Чтобы уменьшить усилия на определенных участках.\n
d) Чтобы обеспечить устойчивость всей конструкции.''',
                                      reply_markup=inline_keyboards.pr_3_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-3-a')
@router.callback_query(F.data == 'pr_3-3-b')
@router.callback_query(F.data == 'pr_3-3-c')
@router.callback_query(F.data == 'pr_3-3-d')
async def pr_3_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-3-a': False,
        'pr_3-3-b': True,
        'pr_3-3-c': False,
        'pr_3-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. В какой момент достаточно выдавливать диск под широкой проставкой?\n\n
a) Когда диск полностью исправлен.\n
b) Когда деформация становится минимальной и можно зафиксировать нужную форму.\n
c) Когда деформация и щель между упором становятся минимальными.\n
d) Когда диск больше не имеет видимых повреждений.''',
                               reply_markup=inline_keyboards.pr_3_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pr_3-4-a')
@router.callback_query(F.data == 'pr_3-4-b')
@router.callback_query(F.data == 'pr_3-4-c')
@router.callback_query(F.data == 'pr_3-4-d')
async def pr_3_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-4-a': False,
        'pr_3-4-b': False,
        'pr_3-4-c': True,
        'pr_3-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. В каком месте фиксируется деформация восьмерки?\n\n
a) В центре диска.\n
b) На краях диска, где происходит основная нагрузка.\n
c) В местах, где имеются трещины.\n
d) В области закраины.''',
                                      reply_markup=inline_keyboards.pr_3_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-5-a')
@router.callback_query(F.data == 'pr_3-5-b')
@router.callback_query(F.data == 'pr_3-5-c')
@router.callback_query(F.data == 'pr_3-5-d')
async def pr_3_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-5-a': False,
        'pr_3-5-b': True,
        'pr_3-5-c': False,
        'pr_3-5-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. В каком случае нужно ставить распор при выравнивании восьмерки?\n\n
    a) Когда диск полностью исправлен.\n
    b) Когда необходимо обеспечить дополнительную фиксацию и предотвратить возможные перегибы.\n
    c) Когда диск уже почти выровнен.\n
    d) Когда диск требует дополнительного охлаждения.''',
                                      reply_markup=inline_keyboards.pr_3_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-6-a')
@router.callback_query(F.data == 'pr_3-6-b')
@router.callback_query(F.data == 'pr_3-6-c')
@router.callback_query(F.data == 'pr_3-6-d')
async def pr_3_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-6-a': False,
        'pr_3-6-b': True,
        'pr_3-6-c': False,
        'pr_3-6-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Куда следует давить при выравнивании эллипса?\n\n
        a) В центр диска.\n
        b) На края.\n
        c) На внутреннюю полку диска.\n
        d) На внешний контур.''',
                                      reply_markup=inline_keyboards.pr_3_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-7-a')
@router.callback_query(F.data == 'pr_3-7-b')
@router.callback_query(F.data == 'pr_3-7-c')
@router.callback_query(F.data == 'pr_3-7-d')
async def pr_3_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-7-a': False,
        'pr_3-7-b': False,
        'pr_3-7-c': True,
        'pr_3-7-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какое кодовое слово спрятано в этом видео?\n\n
            a) Молния.\n
            b) Шина.\n
            c) Монтажка.\n
            d) Спица.''',
                                      reply_markup=inline_keyboards.pr_3_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-8-a')
@router.callback_query(F.data == 'pr_3-8-b')
@router.callback_query(F.data == 'pr_3-8-c')
@router.callback_query(F.data == 'pr_3-8-d')
async def pr_3_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-8-a': False,
        'pr_3-8-b': False,
        'pr_3-8-c': True,
        'pr_3-8-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Куда следует давить при выравнивании восьмерки?\n\n
                a) В центр диска.\n
                b) На участок, где происходит максимальная\n 
                деформация.\n
                c) Под углом на внешнюю полку диска.\n
                d) Внутри диска.''',
                                      reply_markup=inline_keyboards.pr_3_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-9-a')
@router.callback_query(F.data == 'pr_3-9-b')
@router.callback_query(F.data == 'pr_3-9-c')
@router.callback_query(F.data == 'pr_3-9-d')
async def pr_3_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-9-a': False,
        'pr_3-9-b': False,
        'pr_3-9-c': True,
        'pr_3-9-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. В какой последовательности необходимо устранять деформацию диска?\n\n
                    a) Сначала исправлять краю, потом центр.\n
                    b) Исправлять центр, потом края.\n
                    c) Поочередно устранять деформации, начиная с самых заметных.\n
                    d) Сначала устранять восьмерку, потом эллипс.''',
                                      reply_markup=inline_keyboards.pr_3_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-10-a')
@router.callback_query(F.data == 'pr_3-10-b')
@router.callback_query(F.data == 'pr_3-10-c')
@router.callback_query(F.data == 'pr_3-10-d')
async def pr_3_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-10-a': False,
        'pr_3-10-b': False,
        'pr_3-10-c': True,
        'pr_3-10-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Как следует выравнивать наружную закраину?\n\n
                        a) Выдавливать изнутри.\n
                        b) Постепенно придавливать снаружи,\n 
                        контролируя силу воздействия, используя упор.\n
                        c) Сильно давить с обеих сторон.\n
                        d) Давить только снаружи с использованием\n
                         широкого ограничителя.''',
                                      reply_markup=inline_keyboards.pr_3_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-11-a')
@router.callback_query(F.data == 'pr_3-11-b')
@router.callback_query(F.data == 'pr_3-11-c')
@router.callback_query(F.data == 'pr_3-11-d')
async def pr_3_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-11-a': False,
        'pr_3-11-b': True,
        'pr_3-11-c': False,
        'pr_3-11-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12.	Каким образом происходит выравнивание спицы?\n\n
                            a) С использованием гибки.\n
                            b) С использованием двух цилиндров.\n
                            c) Плавным выдавливанием из центра.\n
                            d) Путем воздействия на края.''',
                                      reply_markup=inline_keyboards.pr_3_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-12-a')
@router.callback_query(F.data == 'pr_3-12-b')
@router.callback_query(F.data == 'pr_3-12-c')
@router.callback_query(F.data == 'pr_3-12-d')
async def pr_3_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-12-a': False,
        'pr_3-12-b': True,
        'pr_3-12-c': False,
        'pr_3-12-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. В каких пределах получилось выровнять диск в этом видео?\n\n
                                a) На 50%.\n
                                b) На 90%.\n
                                c) На 100%.\n
                                d) На 75%.''',
                                      reply_markup=inline_keyboards.pr_3_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_3-13-a')
@router.callback_query(F.data == 'pr_3-13-b')
@router.callback_query(F.data == 'pr_3-13-c')
@router.callback_query(F.data == 'pr_3-13-d')
async def pr_3_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_3-13-a': False,
        'pr_3-13-b': True,
        'pr_3-13-c': False,
        'pr_3-13-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 13:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 13:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='pr_exam_pass_3',  # Убедитесь, что столбец существует
                status=1 if user_score >= 12 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 14

        if user_score >= 12:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/13.\n"
            f"Теперь вы можете перейти к следующему уроку.",
            reply_markup=inline_keyboards.urok_po_pravkam_4()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/13.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 12 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.pravki_zanovo_3()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_pr_test_3(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_pr_3(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_pr_4_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='pr_exam_pass_4'):
            await callback.answer(text='Вы уже проходили тест по правкам!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что произошло с диском в этом видео?\n\n
a) Диск выдержал правку без повреждений.\n
b) Диск лопнул при правке возле спицы.\n
c) Диск полностью восстановлен до заводского состояния.\n
d) Диск потерял свою форму из-за нагрева.''',
                                      reply_markup=inline_keyboards.pr_4_1_answer())
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'pr_4-1-a')
@router.callback_query(F.data == 'pr_4-1-b')
@router.callback_query(F.data == 'pr_4-1-c')
@router.callback_query(F.data == 'pr_4-1-d')
async def pr_4_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_4-1-a': False,
        'pr_4-1-b': True,
        'pr_4-1-c': False,
        'pr_4-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Что обычно происходит с диском при правке, если он деформирован возле спицы?\n\n
a) Диск выравнивается без проблем.\n
b) Диск часто лопается из-за повышенной нагрузки.\n
c) Диск легко восстанавливается после нагрева.\n
d) Деформация устраняется, но появляются новые вмятины.''',
                                      reply_markup=inline_keyboards.pr_4_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_4-2-a')
@router.callback_query(F.data == 'pr_4-2-b')
@router.callback_query(F.data == 'pr_4-2-c')
@router.callback_query(F.data == 'pr_4-2-d')
async def pr_4_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_4-2-a': False,
        'pr_4-2-b': True,
        'pr_4-2-c': False,
        'pr_4-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Для чего нужен дополнительный распор при правке закраины?\n\n
a) Для повышения точности нагрева.\n
b) Для упрощения удаления краски.\n
c) Для предотвращения разрыва диска в опасных зонах.\n
d) Для ускорения процесса правки.''',
                                      reply_markup=inline_keyboards.pr_4_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_4-3-a')
@router.callback_query(F.data == 'pr_4-3-b')
@router.callback_query(F.data == 'pr_4-3-c')
@router.callback_query(F.data == 'pr_4-3-d')
async def pr_4_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_4-3-a': False,
        'pr_4-3-b': False,
        'pr_4-3-c': True,
        'pr_4-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Какое кодовое слово спрятано в видео?\n\n
a) Монтажка.\n
b) Латка.\n
c) Краска.\n
d) Распор.''',
                               reply_markup=inline_keyboards.pr_4_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pr_4-4-a')
@router.callback_query(F.data == 'pr_4-4-b')
@router.callback_query(F.data == 'pr_4-4-c')
@router.callback_query(F.data == 'pr_4-4-d')
async def pr_4_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_4-4-a': False,
        'pr_4-4-b': True,
        'pr_4-4-c': False,
        'pr_4-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Почему в видео рекомендовано править диск с использованием нагрева?\n\n
a) Для ускорения процесса восстановления.\n
b) Чтобы улучшить внешний вид диска.\n
c) Чтобы снизить вероятность разрыва при правке.\n
d) Для равномерного распределения нагрузки.''',
                                      reply_markup=inline_keyboards.pr_4_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_4-5-a')
@router.callback_query(F.data == 'pr_4-5-b')
@router.callback_query(F.data == 'pr_4-5-c')
@router.callback_query(F.data == 'pr_4-5-d')
async def pr_4_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_4-5-a': False,
        'pr_4-5-b': False,
        'pr_4-5-c': True,
        'pr_4-5-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Что произойдет, если диск править без распора в месте повреждения возле спицы?\n\n
    a) Диск лопнет из-за концентрации напряжения.\n
    b) Диск сохранит свою форму, но появится вибрация.\n
    c) Диск изменит цвет и начнет терять прочность.\n
    d) Ничего критичного, процесс пройдет без проблем.''',
                                      reply_markup=inline_keyboards.pr_4_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_4-6-a')
@router.callback_query(F.data == 'pr_4-6-b')
@router.callback_query(F.data == 'pr_4-6-c')
@router.callback_query(F.data == 'pr_4-6-d')
async def pr_4_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_4-6-a': True,
        'pr_4-6-b': False,
        'pr_4-6-c': False,
        'pr_4-6-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Каким образом можно снизить вероятность повреждения диска при правке?\n\n
        a) Использовать большую силу давления.\n
        b) Применять распор и равномерное давление.\n
        c) Увеличивать угол изгиба без ограничителей.\n
        d) Проводить правку без предварительного нагрева.''',
                                      reply_markup=inline_keyboards.pr_4_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_4-7-a')
@router.callback_query(F.data == 'pr_4-7-b')
@router.callback_query(F.data == 'pr_4-7-c')
@router.callback_query(F.data == 'pr_4-7-d')
async def pr_4_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_4-7-a': False,
        'pr_4-7-b': True,
        'pr_4-7-c': False,
        'pr_4-7-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какое ключевое отличие правки диска с нагревом от правки на холодную?\n\n
            a) Нагрев позволяет избежать использования дополнительных инструментов.\n
            b) На холодную диск деформируется сильнее.\n
            c) Нагрев снижает риск разрыва металла.\n
            d) На холодную диск легче выравнивать.''',
                                      reply_markup=inline_keyboards.pr_4_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_4-8-a')
@router.callback_query(F.data == 'pr_4-8-b')
@router.callback_query(F.data == 'pr_4-8-c')
@router.callback_query(F.data == 'pr_4-8-d')
async def pr_4_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_4-8-a': False,
        'pr_4-8-b': False,
        'pr_4-8-c': True,
        'pr_4-8-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 8:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 8:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='pr_exam_pass_4',  # Убедитесь, что столбец существует
                status=1 if user_score >= 7 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 9

        if user_score >= 7:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/8.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.remont_i_shinka()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/8.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 7 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.pravki_zanovo_5()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_pr_test_4(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_pr_4(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_tr_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='tr_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по тренингу!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что является первым шагом в обработке клиентского запроса?\n\n
a) Предложение стандартного решения.\n
b) Анализ потребностей клиента.\n
c) Завершение диалога.\n
d) Передача задачи другому сотруднику.''',
                                      reply_markup=inline_keyboards.tr_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'tr-1-a')
@router.callback_query(F.data == 'tr-1-b')
@router.callback_query(F.data == 'tr-1-c')
@router.callback_query(F.data == 'tr-1-d')
async def tr_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-1-a': False,
        'tr-1-b': True,
        'tr-1-c': False,
        'tr-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какой тон следует использовать при общении с клиентом?\n\n
a) Нейтральный и профессиональный .\n
b) Резкий и формальный.\n
c) Дружелюбный, но снисходительный.\n
d) Эмоционально насыщенный.''',
                                      reply_markup=inline_keyboards.tr_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-2-a')
@router.callback_query(F.data == 'tr-2-b')
@router.callback_query(F.data == 'tr-2-c')
@router.callback_query(F.data == 'tr-2-d')
async def tr_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-2-a': True,
        'tr-2-b': False,
        'tr-2-c': False,
        'tr-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Эмоционально насыщенный?\n\n
a) Извиниться и сразу предложить компенсацию.\n
b) Выслушать, уточнить детали и предложить решение.\n
c) Попросить клиента подождать до выяснения обстоятельств.\n
d) Передать вопрос руководителю.''',
                                      reply_markup=inline_keyboards.tr_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-3-a')
@router.callback_query(F.data == 'tr-3-b')
@router.callback_query(F.data == 'tr-3-c')
@router.callback_query(F.data == 'tr-3-d')
async def tr_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-3-a': False,
        'tr-3-b': True,
        'tr-3-c': False,
        'tr-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Как правильно завершить разговор с клиентом?\n\n
a) Сказать: “До свидания”.\n
b) Подвести итог, поблагодарить за обращение и попрощаться.\n
c) Пожелать удачи.\n
d) Спросить, нужен ли клиенту ещё какой-то товар.''',
                               reply_markup=inline_keyboards.tr_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-4-a')
@router.callback_query(F.data == 'tr-4-b')
@router.callback_query(F.data == 'tr-4-c')
@router.callback_query(F.data == 'tr-4-d')
async def tr_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-4-a': False,
        'tr-4-b': True,
        'tr-4-c': False,
        'tr-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Какова главная цель активного слушания?\n\n
a) Запомнить как можно больше деталей.\n
b) Понять истинные потребности клиента.\n
c) Проявить сочувствие.\n
d) Сократить время диалога.''',
                                      reply_markup=inline_keyboards.tr_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-5-a')
@router.callback_query(F.data == 'tr-5-b')
@router.callback_query(F.data == 'tr-5-c')
@router.callback_query(F.data == 'tr-5-d')
async def tr_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-5-a': False,
        'tr-5-b': True,
        'tr-5-c': False,
        'tr-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Что делать, если клиент просит невозможное?\n\n
a) Объяснить, почему это невозможно, и предложить альтернативу.\n
b) Сразу отказать.\n
c) Согласиться, но не выполнять.\n
d) Перевести запрос на другого сотрудника.''',
                                      reply_markup=inline_keyboards.tr_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-6-a')
@router.callback_query(F.data == 'tr-6-b')
@router.callback_query(F.data == 'tr-6-c')
@router.callback_query(F.data == 'tr-6-d')
async def tr_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-6-a': True,
        'tr-6-b': False,
        'tr-6-c': False,
        'tr-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Что важно учитывать при приоритизации запросов клиентов?\n\n
a) Срочность и важность запроса.\n
b) Личное мнение сотрудника.\n
c) Уровень знания клиента.\n
d) Очередность поступления.''',
                                      reply_markup=inline_keyboards.tr_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-7-a')
@router.callback_query(F.data == 'tr-7-b')
@router.callback_query(F.data == 'tr-7-c')
@router.callback_query(F.data == 'tr-7-d')
async def tr_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-7-a': True,
        'tr-7-b': False,
        'tr-7-c': False,
        'tr-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Как реагировать на агрессивного клиента?\n\n
a) Ответить тем же тоном.\n
b) Сохранить спокойствие, выслушать и предложить решение.\n
c) Прекратить разговор.\n
d) Перевести звонок на другого сотрудника.''',
                                      reply_markup=inline_keyboards.tr_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-8-a')
@router.callback_query(F.data == 'tr-8-b')
@router.callback_query(F.data == 'tr-8-c')
@router.callback_query(F.data == 'tr-8-d')
async def tr_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-8-a': False,
        'tr-8-b': True,
        'tr-8-c': False,
        'tr-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Если клиент просит уточнить детали, но у вас нет информации, что делать?\n\n
a) Сказать, что информация недоступна.\n
b) Уточнить у коллег или найти информацию самостоятельно.\n
c) Попросить клиента перезвонить позже.\n
d) Сказать, что этим занимается другой отдел.''',
                                      reply_markup=inline_keyboards.tr_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-9-a')
@router.callback_query(F.data == 'tr-9-b')
@router.callback_query(F.data == 'tr-9-c')
@router.callback_query(F.data == 'tr-9-d')
async def tr_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-9-a': False,
        'tr-9-b': True,
        'tr-9-c': False,
        'tr-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Как убедиться, что клиент доволен результатом?\n\n
a) Попросить его написать отзыв.\n
b) Задать прямой вопрос о его удовлетворённости .\n
c) Предположить, что он доволен, если нет претензий.\n
d) Проверить его тон голоса.''',
                                      reply_markup=inline_keyboards.tr_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-10-a')
@router.callback_query(F.data == 'tr-10-b')
@router.callback_query(F.data == 'tr-10-c')
@router.callback_query(F.data == 'tr-10-d')
async def tr_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-10-a': False,
        'tr-10-b': True,
        'tr-10-c': False,
        'tr-10-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Что лучше всего помогает избегать конфликтов с клиентами?\n\n
a) Избегать общения с недовольными клиентами.\n
b) Использовать активное слушание и вежливый тон.\n
c) Предлагать скидки.\n
d) Быстро завершать разговоры.''',
                                      reply_markup=inline_keyboards.tr_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-11-a')
@router.callback_query(F.data == 'tr-11-b')
@router.callback_query(F.data == 'tr-11-c')
@router.callback_query(F.data == 'tr-11-d')
async def tr_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-11-a': False,
        'tr-11-b': True,
        'tr-11-c': False,
        'tr-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Если клиент предлагает улучшение, что вы должны сделать?\n\n
a) Проигнорировать предложение.\n
b) Поблагодарить и передать идею руководству.\n
c) Оценить предложение и ответить отказом.\n
d) Сказать клиенту, что это не относится к его компетенции.''',
                                      reply_markup=inline_keyboards.tr_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-12-a')
@router.callback_query(F.data == 'tr-12-b')
@router.callback_query(F.data == 'tr-12-c')
@router.callback_query(F.data == 'tr-12-d')
async def tr_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-12-a': False,
        'tr-12-b': True,
        'tr-12-c': False,
        'tr-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Какую информацию важно узнать при встрече с клиентом?\n\n
а) Имя клиента и какой запрос.\n
b) Только номер телефона клиента.\n
c) Только конечное решение.\n
d) Все детали, включая ненужные.''',
                                      reply_markup=inline_keyboards.tr_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-13-a')
@router.callback_query(F.data == 'tr-13-b')
@router.callback_query(F.data == 'tr-13-c')
@router.callback_query(F.data == 'tr-13-d')
async def tr_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-13-a': True,
        'tr-13-b': False,
        'tr-13-c': False,
        'tr-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Что делать, если клиент недоволен решением?\n\n
a) Сказать, что ничего больше нельзя сделать.\n
b) Уточнить, чем он недоволен, и предложить альтернативу.\n
c) Игнорировать его.\n
d) Передать жалобу в другой отдел.''',
                                      reply_markup=inline_keyboards.tr_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-14-a')
@router.callback_query(F.data == 'tr-14-b')
@router.callback_query(F.data == 'tr-14-c')
@router.callback_query(F.data == 'tr-14-d')
async def tr_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-14-a': False,
        'tr-14-b': True,
        'tr-14-c': False,
        'tr-14-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Как определить, правильно ли понято обращение клиента?\n\n
a) Перефразировать запрос и уточнить у клиента.\n
b) Спросить коллег.\n
c) Предположить, что всё правильно.\n
d) Сразу переходить к решению.''',
                                      reply_markup=inline_keyboards.tr_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-15-a')
@router.callback_query(F.data == 'tr-15-b')
@router.callback_query(F.data == 'tr-15-c')
@router.callback_query(F.data == 'tr-15-d')
async def tr_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-15-a': True,
        'tr-15-b': False,
        'tr-15-c': False,
        'tr-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Какой метод лучше всего подходит для предотвращения недоразумений?\n\n
a) Использование шаблонов ответов.\n
b) Перепроверка информации у клиента.\n
c) Быстрое завершение разговора.\n
d) Оставление вопроса открытым.''',
                                      reply_markup=inline_keyboards.tr_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-16-a')
@router.callback_query(F.data == 'tr-16-b')
@router.callback_query(F.data == 'tr-16-c')
@router.callback_query(F.data == 'tr-16-d')
async def tr_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-16-a': False,
        'tr-16-b': True,
        'tr-16-c': False,
        'tr-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Если клиент хочет жаловаться, что вы должны сделать?\n\n
a) Направить его к руководству.\n
b) Выслушать и зафиксировать жалобу.\n
c) Сказать, что жалобы не принимаются.\n
d) Предложить ему заполнить анкету.''',
                                      reply_markup=inline_keyboards.tr_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-17-a')
@router.callback_query(F.data == 'tr-17-b')
@router.callback_query(F.data == 'tr-17-c')
@router.callback_query(F.data == 'tr-17-d')
async def tr_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-17-a': False,
        'tr-17-b': True,
        'tr-17-c': False,
        'tr-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Что делать, если клиент благодарит за качественную работу:\n\n
a) Поблагодарить в ответ и завершить разговор.\n
b) Сказать, что это не ваша заслуга.\n
c) Игнорировать благодарность.\n
d) Предложить дополнительные услуги.''',
                                      reply_markup=inline_keyboards.tr_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-18-a')
@router.callback_query(F.data == 'tr-18-b')
@router.callback_query(F.data == 'tr-18-c')
@router.callback_query(F.data == 'tr-18-d')
async def tr_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-18-a': True,
        'tr-18-b': False,
        'tr-18-c': False,
        'tr-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Какое из следующих утверждений о работе с клиентами верное?\n\n
a) Все клиенты должны быть удовлетворены любым способом.\n
b) Клиенты всегда правы.\n
c) Важно найти баланс между интересами клиента и компании.\n
d) Запросы клиентов всегда требуют немедленного решения.''',
                                      reply_markup=inline_keyboards.tr_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-19-a')
@router.callback_query(F.data == 'tr-19-b')
@router.callback_query(F.data == 'tr-19-c')
@router.callback_query(F.data == 'tr-19-d')
async def tr_19_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-19-a': False,
        'tr-19-b': False,
        'tr-19-c': True,
        'tr-19-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''20. Что лучше всего способствует улучшению сервиса.\n
a) Постоянное обучение сотрудников.\n
b) Жёсткое соблюдение стандартов.\n
c) Минимизация времени на общение.\n
d) Максимум времени на общение.''',
                                      reply_markup=inline_keyboards.tr_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'tr-20-a')
@router.callback_query(F.data == 'tr-20-b')
@router.callback_query(F.data == 'tr-20-c')
@router.callback_query(F.data == 'tr-20-d')
async def tr_20_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'tr-20-a': True,
        'tr-20-b': False,
        'tr-20-c': False,
        'tr-20-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 20:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 20:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='tr_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 21

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/20.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=reply_keyboards.kursi_po_kolesam()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/20.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.treningi()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_tr_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_tr(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_ob_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='ob_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по Балансировочному станку!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Какие типы колес можно балансировать на станке Galaxy?\n\n
a) Только легковые автомобили.\n
b) Легковые, легкий коммерческий транспорт и мотоциклы.\n
c) Только легковые и мотоциклы.\n
d) Только легкий коммерческий транспорт.''',
                                      reply_markup=inline_keyboards.ob_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'ob-1-a')
@router.callback_query(F.data == 'ob-1-b')
@router.callback_query(F.data == 'ob-1-c')
@router.callback_query(F.data == 'ob-1-d')
async def ob_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-1-a': False,
        'ob-1-b': True,
        'ob-1-c': False,
        'ob-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какая технология используется для точного расчета веса балансировочного груза?\n\n
a) AutoBalance.\n
b) Direct 3D.\n
c) LaserCalc.\n
d) Rim Alignment.''',
                                      reply_markup=inline_keyboards.ob_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ob-2-a')
@router.callback_query(F.data == 'ob-2-b')
@router.callback_query(F.data == 'ob-2-c')
@router.callback_query(F.data == 'ob-2-d')
async def ob_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-2-a': False,
        'ob-2-b': True,
        'ob-2-c': False,
        'ob-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Какая функция позволяет балансировать колеса без нажатия кнопок на панели управления?\n\n
a) No Click.\n
b) Auto Control.\n
c) No Touch.\n
d) FreeSpin.''',
                                      reply_markup=inline_keyboards.ob_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ob-3-a')
@router.callback_query(F.data == 'ob-3-b')
@router.callback_query(F.data == 'ob-3-c')
@router.callback_query(F.data == 'ob-3-d')
async def ob_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-3-a': False,
        'ob-3-b': False,
        'ob-3-c': True,
        'ob-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. На каком часе устанавливается груз для литых дисков?\n\n
a) 12 часов.\n
b) 6 часов.\n
c) 3 часа.\n
d) 9 часов.''',
                               reply_markup=inline_keyboards.ob_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ob-4-a')
@router.callback_query(F.data == 'ob-4-b')
@router.callback_query(F.data == 'ob-4-c')
@router.callback_query(F.data == 'ob-4-d')
async def ob_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-4-a': False,
        'ob-4-b': True,
        'ob-4-c': False,
        'ob-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Какая технология обеспечивает плавный разгон, стабильное вращение и торможение станка?\n\n
a) SmoothDrive.\n
b) S-Drive.\n
c) BalanceControl.\n
d) PowerRun.''',
                                      reply_markup=inline_keyboards.ob_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ob-5-a')
@router.callback_query(F.data == 'ob-5-b')
@router.callback_query(F.data == 'ob-5-c')
@router.callback_query(F.data == 'ob-5-d')
async def ob_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-5-a': False,
        'ob-5-b': True,
        'ob-5-c': False,
        'ob-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Чем обеспечивается комфорт установки груза?\n\n
a) Использованием магнитных креплений.\n
b) LED-подсветкой и лазерным указателем.\n
c) Зеркальным экраном.\n
d) Автоматическим креплением.''',
                                      reply_markup=inline_keyboards.ob_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ob-6-a')
@router.callback_query(F.data == 'ob-6-b')
@router.callback_query(F.data == 'ob-6-c')
@router.callback_query(F.data == 'ob-6-d')
async def ob_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-6-a': False,
        'ob-6-b': True,
        'ob-6-c': False,
        'ob-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. На сколько миллиметров вылет вала станка Galaxy больше по сравнению с младшими моделями?\n\n
a) 25 мм.\n
b) 35 мм.\n
c) 45 мм.\n
d) 50 мм.''',
                                      reply_markup=inline_keyboards.ob_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ob-7-a')
@router.callback_query(F.data == 'ob-7-b')
@router.callback_query(F.data == 'ob-7-c')
@router.callback_query(F.data == 'ob-7-d')
async def ob_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-7-a': False,
        'ob-7-b': False,
        'ob-7-c': True,
        'ob-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какая технология помогает оценить состояние диска и необходимость его ремонта?\n\n
a) DirectCheck.\n
b) Rim Run Out.\n
c) DiskFix.\n
d) RepairAssist.''',
                                      reply_markup=inline_keyboards.ob_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ob-8-a')
@router.callback_query(F.data == 'ob-8-b')
@router.callback_query(F.data == 'ob-8-c')
@router.callback_query(F.data == 'ob-8-d')
async def ob_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-8-a': False,
        'ob-8-b': True,
        'ob-8-c': False,
        'ob-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Что позволяет сохранять отчеты о балансировке на компьютер?\n\n
a) USB-кабель.\n
b) Сохранение на SD-карту.\n
c) Bluetooth-подключение.\n
d) Облачное хранилище.''',
                                      reply_markup=inline_keyboards.ob_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ob-9-a')
@router.callback_query(F.data == 'ob-9-b')
@router.callback_query(F.data == 'ob-9-c')
@router.callback_query(F.data == 'ob-9-d')
async def ob_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-9-a': False,
        'ob-9-b': True,
        'ob-9-c': False,
        'ob-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Сколько комплектов колес можно обслуживать одновременно, переключаясь между операторами?\n\n
a) Два.\n
b) Три.\n
c) Четыре.\n
d) Один.''',
                                      reply_markup=inline_keyboards.ob_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ob-10-a')
@router.callback_query(F.data == 'ob-10-b')
@router.callback_query(F.data == 'ob-10-c')
@router.callback_query(F.data == 'ob-10-d')
async def ob_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-10-a': False,
        'ob-10-b': True,
        'ob-10-c': False,
        'ob-10-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Какая точность изготовления критически важных деталей станка Galaxy?\n\n
a) 5 микрон.\n
b) 7 микрон.\n
c) 10 микрон.\n
d) 15 микрон.''',
                                      reply_markup=inline_keyboards.ob_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ob-11-a')
@router.callback_query(F.data == 'ob-11-b')
@router.callback_query(F.data == 'ob-11-c')
@router.callback_query(F.data == 'ob-11-d')
async def ob_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-11-a': False,
        'ob-11-b': True,
        'ob-11-c': False,
        'ob-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Как защищается электроника станка от скачков напряжения?\n\n
a) Использование стабилизатора.\n
b) Технология PowerGuard.\n
c) Двойная изоляция.\n
d) Система VoltageControl.''',
                                      reply_markup=inline_keyboards.ob_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ob-12-a')
@router.callback_query(F.data == 'ob-12-b')
@router.callback_query(F.data == 'ob-12-c')
@router.callback_query(F.data == 'ob-12-d')
async def ob_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-12-a': False,
        'ob-12-b': True,
        'ob-12-c': False,
        'ob-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Что входит в комплект аксессуаров станка Galaxy?\n\n
а) Только быстросъемная гайка и скребок.\n
b) Калибр, двухсторонний конус, ролик для измерения биения, клещи и скребок.\n
c) Набор из трех конусов и фрезер.\n
d) Только электронная линейка''',
                                      reply_markup=inline_keyboards.ob_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ob-13-a')
@router.callback_query(F.data == 'ob-13-b')
@router.callback_query(F.data == 'ob-13-c')
@router.callback_query(F.data == 'ob-13-d')
async def ob_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-13-a': False,
        'ob-13-b': True,
        'ob-13-c': False,
        'ob-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Какая гарантия предоставляется на балансировочный станок Galaxy?\n\n
a) 1 год.\n
b) 2 года.\n
c) 3 года.\n
d) 5 лет.''',
                                      reply_markup=inline_keyboards.ob_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ob-14-a')
@router.callback_query(F.data == 'ob-14-b')
@router.callback_query(F.data == 'ob-14-c')
@router.callback_query(F.data == 'ob-14-d')
async def ob_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-14-a': False,
        'ob-14-b': True,
        'ob-14-c': False,
        'ob-14-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Что упрощает обслуживание больших и широких колес на станке Galaxy?\n\n
a) Наклонный корпус и увеличенный вылет вала.\n
b) Специальные крепления.\n
c) Углубленные ниши для аксессуаров.\n
d) Двойной лазерный указатель.''',
                                      reply_markup=inline_keyboards.ob_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ob-15-a')
@router.callback_query(F.data == 'ob-15-b')
@router.callback_query(F.data == 'ob-15-c')
@router.callback_query(F.data == 'ob-15-d')
async def ob_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-15-a': True,
        'ob-15-b': False,
        'ob-15-c': False,
        'ob-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Какой интерфейс используется на станке Galaxy?\n\n
a) Текстовый с подсказками.\n
b) Графический 3D интерфейс.\n
c) Сенсорный с клавиатурой.\n
d) Минималистичный черно-белый.''',
                                      reply_markup=inline_keyboards.ob_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ob-16-a')
@router.callback_query(F.data == 'ob-16-b')
@router.callback_query(F.data == 'ob-16-c')
@router.callback_query(F.data == 'ob-16-d')
async def ob_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-16-a': False,
        'ob-16-b': True,
        'ob-16-c': False,
        'ob-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Чем подтверждается точность балансировки станка Galaxy?\n\n
a) Гарантией производителя.\n
b) Свидетельством о внесении в государственный реестр средств измерений.\n
c) Тестами пользователей.\n
d) Отчетами мастерских.''',
                                      reply_markup=inline_keyboards.ob_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ob-17-a')
@router.callback_query(F.data == 'ob-17-b')
@router.callback_query(F.data == 'ob-17-c')
@router.callback_query(F.data == 'ob-17-d')
async def ob_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-17-a': False,
        'ob-17-b': True,
        'ob-17-c': False,
        'ob-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Введите кодовое слово, подтверждающее успешное изучение материала:\n\n
a) Баланс.\n
b) Колесо.\n
c) Грузик.\n
d) Станок.''',
                                      reply_markup=inline_keyboards.ob_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ob-18-a')
@router.callback_query(F.data == 'ob-18-b')
@router.callback_query(F.data == 'ob-18-c')
@router.callback_query(F.data == 'ob-18-d')
async def ob_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ob-18-a': False,
        'ob-18-b': False,
        'ob-18-c': True,
        'ob-18-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 18:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 18:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='ob_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 17 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 19

        if user_score >= 17:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/18.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.stanok_dl_pravok()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/18.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 17 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.balancirovka_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_ob_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_ob(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_st_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='st_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по шиномонтажному станку!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Для каких шин подходит шиномонтажный станок KS-420 Pro?\n\n
a) Только для грузовых шин.\n
b) Для спортивных автомобилей с низкопрофильными шинами.\n
c) Для шин легковых автомобилей с посадочным диаметром от 10 до 24 дюймов.\n
d) Только для шин Runflat.''',
                                      reply_markup=inline_keyboards.st_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'st-1-a')
@router.callback_query(F.data == 'st-1-b')
@router.callback_query(F.data == 'st-1-c')
@router.callback_query(F.data == 'st-1-d')
async def st_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-1-a': False,
        'st-1-b': False,
        'st-1-c': True,
        'st-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какая максимальная ширина шин, которые можно обслуживать на станке?\n\n
a) 200 мм.\n
b) 330 мм.\n
c) 300 мм.\n
d) 350 мм.''',
                                      reply_markup=inline_keyboards.st_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-2-a')
@router.callback_query(F.data == 'st-2-b')
@router.callback_query(F.data == 'st-2-c')
@router.callback_query(F.data == 'st-2-d')
async def st_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-2-a': False,
        'st-2-b': True,
        'st-2-c': False,
        'st-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Из какого материала выполнены фитинги пневматической системы станка?\n\n
a) Пластик.\n
b) Композитный материал.\n
c) Алюминиевый сплав.\n
d) Высококачественная сталь.''',
                                      reply_markup=inline_keyboards.st_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-3-a')
@router.callback_query(F.data == 'st-3-b')
@router.callback_query(F.data == 'st-3-c')
@router.callback_query(F.data == 'st-3-d')
async def st_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-3-a': False,
        'st-3-b': False,
        'st-3-c': False,
        'st-3-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Сколько педалей управления используется на шиномонтажном станке?\n\n
a) Две.\n
b) Три.\n
c) Четыре.\n
d) Пять.''',
                               reply_markup=inline_keyboards.st_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-4-a')
@router.callback_query(F.data == 'st-4-b')
@router.callback_query(F.data == 'st-4-c')
@router.callback_query(F.data == 'st-4-d')
async def st_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-4-a': False,
        'st-4-b': False,
        'st-4-c': True,
        'st-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Какой бренд является поставщиком блока подготовки воздуха для станка?\n\n
a) Bosch.\n
b) SMC.\n
c) Makita.\n
d) Hitachi.''',
                                      reply_markup=inline_keyboards.st_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'st-5-a')
@router.callback_query(F.data == 'st-5-b')
@router.callback_query(F.data == 'st-5-c')
@router.callback_query(F.data == 'st-5-d')
async def st_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-5-a': False,
        'st-5-b': True,
        'st-5-c': False,
        'st-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какой материал используется для корпуса цилиндра отжима борта?\n\n
a) Пластик.\n
b) Углеродистая сталь.\n
c) Алюминиевый сплав.\n
d) Титан.''',
                                      reply_markup=inline_keyboards.st_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-6-a')
@router.callback_query(F.data == 'st-6-b')
@router.callback_query(F.data == 'st-6-c')
@router.callback_query(F.data == 'st-6-d')
async def st_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-6-a': False,
        'st-6-b': False,
        'st-6-c': True,
        'st-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Какой механизм позволяет надежно зафиксировать колесо на рабочем столе?\n\n
a) Червячный колочковый механизм.\n
b) Автоматическая фиксация.\n
c) Лазерная система.\n
d) Магнитные зажимы.''',
                                      reply_markup=inline_keyboards.st_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-7-a')
@router.callback_query(F.data == 'st-7-b')
@router.callback_query(F.data == 'st-7-c')
@router.callback_query(F.data == 'st-7-d')
async def st_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-7-a': True,
        'st-7-b': False,
        'st-7-c': False,
        'st-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какая система используется для предотвращения повреждения колесных дисков при зажиме?\n\n
a) Пластиковые накладки на зажимных колочках.\n
b) Резиновые прокладки.\n
c) Силиконовые вставки.\n
d) Тканевые прокладки.''',
                                      reply_markup=inline_keyboards.st_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-8-a')
@router.callback_query(F.data == 'st-8-b')
@router.callback_query(F.data == 'st-8-c')
@router.callback_query(F.data == 'st-8-d')
async def st_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-8-a': True,
        'st-8-b': False,
        'st-8-c': False,
        'st-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Какой механизм обеспечивает безопасность при накачке шин?\n\n
a) Электронная блокировка.\n
b) Ограничитель давления на 3,5 бара.\n
c) Автоматическая вентиляция.\n
d) Контроль температуры воздуха.''',
                                      reply_markup=inline_keyboards.st_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-9-a')
@router.callback_query(F.data == 'st-9-b')
@router.callback_query(F.data == 'st-9-c')
@router.callback_query(F.data == 'st-9-d')
async def st_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-9-a': False,
        'st-9-b': True,
        'st-9-c': False,
        'st-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Для чего предназначено вспомогательное устройство УВ-1?\n\n
a) Для балансировки колеса.\n
b) Для очистки поверхности диска.\n
c) Для монтажа и демонтажа низкопрофильных шин без монтировки.\n
d) Для защиты шин от проколов.''',
                                      reply_markup=inline_keyboards.st_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-10-a')
@router.callback_query(F.data == 'st-10-b')
@router.callback_query(F.data == 'st-10-c')
@router.callback_query(F.data == 'st-10-d')
async def st_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-10-a': False,
        'st-10-b': False,
        'st-10-c': True,
        'st-10-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Что обеспечивает взрывная накачка ВН-1?\n\n
a) Автоматическое измерение давления.\n
b) Ускоренный демонтаж шин.\n
c) Очистку борта от загрязнений.\n
d) Быструю и безопасную посадку бескамерной шины на диск.''',
                                      reply_markup=inline_keyboards.st_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-11-a')
@router.callback_query(F.data == 'st-11-b')
@router.callback_query(F.data == 'st-11-c')
@router.callback_query(F.data == 'st-11-d')
async def st_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-11-a': False,
        'st-11-b': False,
        'st-11-c': False,
        'st-11-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Какую операцию выполняют с помощью отжимной лопатки?\n\n
a) Удаление грязи с дисков.\n
b) Отжим борта шины.\n
c) Демонтаж покрышки.\n
d) Проверку толщины колеса.''',
                                      reply_markup=inline_keyboards.st_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-12-a')
@router.callback_query(F.data == 'st-12-b')
@router.callback_query(F.data == 'st-12-c')
@router.callback_query(F.data == 'st-12-d')
async def st_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-12-a': False,
        'st-12-b': True,
        'st-12-c': False,
        'st-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Какое кодовое слово спрятано в тексте?\n\n
а) Монтаж.\n
b) Лопатка.\n
c) Корд.\n
d) Колесо''',
                                      reply_markup=inline_keyboards.st_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-13-a')
@router.callback_query(F.data == 'st-13-b')
@router.callback_query(F.data == 'st-13-c')
@router.callback_query(F.data == 'st-13-d')
async def st_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-13-a': False,
        'st-13-b': False,
        'st-13-c': True,
        'st-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Какие преимущества имеет вспомогательное устройство РВ-1 (третья рука)?\n\n
a) Минимизирует использование электроэнергии.\n
b) Облегчение процесса монтажа и демонтажа низкопрофильных шин и шин с жёстким бортом.\n
c) Ускоряет балансировку колес.\n
d) Автоматически измеряет давление в шинах.''',
                                      reply_markup=inline_keyboards.st_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-14-a')
@router.callback_query(F.data == 'st-14-b')
@router.callback_query(F.data == 'st-14-c')
@router.callback_query(F.data == 'st-14-d')
async def st_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-14-a': False,
        'st-14-b': True,
        'st-14-c': False,
        'st-14-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Какое максимальное усилие может развивать цилиндр отжима борта?\n\n
a) 2 тонны.\n
b) 3 тонны.\n
c) 4 тонны.\n
d) 5 тонн.''',
                                      reply_markup=inline_keyboards.st_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-15-a')
@router.callback_query(F.data == 'st-15-b')
@router.callback_query(F.data == 'st-15-c')
@router.callback_query(F.data == 'st-15-d')
async def st_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-15-a': False,
        'st-15-b': True,
        'st-15-c': False,
        'st-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Какой диаметр колесных дисков можно зажимать изнутри?\n\n
a) До 22 дюймов.\n
b) До 24 дюймов.\n
c) До 26 дюймов.\n
d) До 28 дюймов.''',
                                      reply_markup=inline_keyboards.st_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-16-a')
@router.callback_query(F.data == 'st-16-b')
@router.callback_query(F.data == 'st-16-c')
@router.callback_query(F.data == 'st-16-d')
async def st_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-16-a': False,
        'st-16-b': True,
        'st-16-c': False,
        'st-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Какая конструкция рычага отжимной лопатки обеспечивает его прочность?\n\n
a) Разборная стальная конструкция.\n
b) Алюминиевый сплав.\n
c) Цельно гнутая стальная деталь.\n
d) Композитные материалы.''',
                                      reply_markup=inline_keyboards.st_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-17-a')
@router.callback_query(F.data == 'st-17-b')
@router.callback_query(F.data == 'st-17-c')
@router.callback_query(F.data == 'st-17-d')
async def st_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-17-a': False,
        'st-17-b': False,
        'st-17-c': True,
        'st-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Какая система используется для предотвращения коррозии цилиндров:\n\n
a) Пластиковая защита.\n
b) Покрытие антикоррозийным сплавом.\n
c) Герметичные уплотнители.\n
d) Специальное масло.''',
                                      reply_markup=inline_keyboards.st_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-18-a')
@router.callback_query(F.data == 'st-18-b')
@router.callback_query(F.data == 'st-18-c')
@router.callback_query(F.data == 'st-18-d')
async def st_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-18-a': False,
        'st-18-b': True,
        'st-18-c': False,
        'st-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Какая функция у системы стационарного блока подкачки:\n\n
    a) Предотвращает повреждение манометра.\n
    b) Подает воздух под высоким давлением.\n
    c) Ускоряет демонтаж.\n
    d) Защищает колонну от повреждений.''',
                                      reply_markup=inline_keyboards.st_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st-19-a')
@router.callback_query(F.data == 'st-19-b')
@router.callback_query(F.data == 'st-19-c')
@router.callback_query(F.data == 'st-19-d')
async def st_19_note(callback: CallbackQuery, bot: Bot):
    correct_answers = {
        'st-19-a': True,
        'st-19-b': False,
        'st-19-c': False,
        'st-19-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 19:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 19:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='st_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 20

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/19.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.pravka_diskov_uroki()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/19.\n"
                     f"Для перехода к следующему курсу необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.stanok_dl_shinke_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_st_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_st(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_st_pr_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='st_pr_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по станку правки дисков!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Для чего предназначен стенд Titan Allu Compact с электроприводом?\n\n
a) Балансировка колес.\n
b) Правка литых и кованых дисков.\n
c) Шлифовка поверхностей.\n
d) Установка шин.''',
                                      reply_markup=inline_keyboards.st_pr_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'st_pr-1-a')
@router.callback_query(F.data == 'st_pr-1-b')
@router.callback_query(F.data == 'st_pr-1-c')
@router.callback_query(F.data == 'st_pr-1-d')
async def st_pr_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-1-a': False,
        'st_pr-1-b': True,
        'st_pr-1-c': False,
        'st_pr-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какого максимального диаметра и ширины диски можно править на Titan Allu Compact?\n\n
a) Диаметр 24 дюйма, ширина 12 дюймов.\n
b) Диаметр 22 дюйма, ширина 10 дюймов.\n
c) Диаметр 26 дюйма, ширина 15 дюймов.\n
d) Диаметр 20 дюймов, ширина 8 дюймов.''',
                                      reply_markup=inline_keyboards.st_pr_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-2-a')
@router.callback_query(F.data == 'st_pr-2-b')
@router.callback_query(F.data == 'st_pr-2-c')
@router.callback_query(F.data == 'st_pr-2-d')
async def st_pr_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-2-a': True,
        'st_pr-2-b': False,
        'st_pr-2-c': False,
        'st_pr-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Какие элементы позволяют эффективно управлять деформацией на стенде?\n\n
a) Электронные датчики.\n
b) Лазерный указатель.\n
c) Трехфазный привод.\n
d) Два гидравлических цилиндра.''',
                                      reply_markup=inline_keyboards.st_pr_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-3-a')
@router.callback_query(F.data == 'st_pr-3-b')
@router.callback_query(F.data == 'st_pr-3-c')
@router.callback_query(F.data == 'st_pr-3-d')
async def st_pr_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-3-a': False,
        'st_pr-3-b': False,
        'st_pr-3-c': False,
        'st_pr-3-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Для чего используется указатель биения?\n\n
a) Для проверки толщины диска.\n
b) Для определения места повреждения.\n
c) Для контроля давления.\n
d) Для закрепления вала.''',
                               reply_markup=inline_keyboards.st_pr_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-4-a')
@router.callback_query(F.data == 'st_pr-4-b')
@router.callback_query(F.data == 'st_pr-4-c')
@router.callback_query(F.data == 'st_pr-4-d')
async def st_pr_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-4-a': False,
        'st_pr-4-b': True,
        'st_pr-4-c': False,
        'st_pr-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Какой элемент стенда исключает люфт во время правки?\n\n
a) Цельная конструкция моста.\n
b) Магнитная стойка.\n
c) Дополнительные насадки.\n
d) Ручные ключи.''',
                                      reply_markup=inline_keyboards.st_pr_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'st_pr-5-a')
@router.callback_query(F.data == 'st_pr-5-b')
@router.callback_query(F.data == 'st_pr-5-c')
@router.callback_query(F.data == 'st_pr-5-d')
async def st_pr_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-5-a': True,
        'st_pr-5-b': False,
        'st_pr-5-c': False,
        'st_pr-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какие насадки используются при небольших повреждениях дисков?\n\n
a) Треугольная насадка.\n
b) Малая плоская насадка.\n
c) Насадка с широким основанием.\n
d) Круглая насадка.''',
                                      reply_markup=inline_keyboards.st_pr_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-6-a')
@router.callback_query(F.data == 'st_pr-6-b')
@router.callback_query(F.data == 'st_pr-6-c')
@router.callback_query(F.data == 'st_pr-6-d')
async def st_pr_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-6-a': False,
        'st_pr-6-b': True,
        'st_pr-6-c': False,
        'st_pr-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Какую функцию выполняет упор?\n\n
a) Уменьшает вибрации при работе.\n
b) Предотвращает вторичную деформацию.\n
c) Закрепляет инструмент на мосту.\n
d) Увеличивает мощность привода.''',
                                      reply_markup=inline_keyboards.st_pr_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-7-a')
@router.callback_query(F.data == 'st_pr-7-b')
@router.callback_query(F.data == 'st_pr-7-c')
@router.callback_query(F.data == 'st_pr-7-d')
async def st_pr_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-7-a': False,
        'st_pr-7-b': True,
        'st_pr-7-c': False,
        'st_pr-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Сколько механических распределителей используется для управления гидроцилиндрами?\n\n
a) Один.\n
b) Два.\n
c) Три.\n
d) Четыре.''',
                                      reply_markup=inline_keyboards.st_pr_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-8-a')
@router.callback_query(F.data == 'st_pr-8-b')
@router.callback_query(F.data == 'st_pr-8-c')
@router.callback_query(F.data == 'st_pr-8-d')
async def st_pr_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-8-a': False,
        'st_pr-8-b': True,
        'st_pr-8-c': False,
        'st_pr-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Что добавлено для удобства поиска места деформации диска?\n\n
a) Электрический привод вращения вала.\n
b) Система автоматической диагностики.\n
c) Лазерный указатель биения.\n
d) Подсветка зоны повреждения.''',
                                      reply_markup=inline_keyboards.st_pr_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-9-a')
@router.callback_query(F.data == 'st_pr-9-b')
@router.callback_query(F.data == 'st_pr-9-c')
@router.callback_query(F.data == 'st_pr-9-d')
async def st_pr_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-9-a': True,
        'st_pr-9-b': False,
        'st_pr-9-c': False,
        'st_pr-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Как воздействуют на диск при помощи двух цилиндров одновременно?\n\n
a) В двух местах для увеличения усилия.\n
b) По всей окружности для выравнивания.\n
c) Точечно на место повреждения.\n
d) На спицы и обод одновременно.''',
                                      reply_markup=inline_keyboards.st_pr_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-10-a')
@router.callback_query(F.data == 'st_pr-10-b')
@router.callback_query(F.data == 'st_pr-10-c')
@router.callback_query(F.data == 'st_pr-10-d')
async def st_pr_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-10-a': False,
        'st_pr-10-b': False,
        'st_pr-10-c': True,
        'st_pr-10-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Какой ключ входит в комплект стенда для ручной правки литых дисков?\n\n
a) Шестигранный ключ.\n
b) Специальный ключ (чупа-чупс).\n
c) Ключ-гайковерт.\n
d) Трубчатый ключ.''',
                                      reply_markup=inline_keyboards.st_pr_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-11-a')
@router.callback_query(F.data == 'st_pr-11-b')
@router.callback_query(F.data == 'st_pr-11-c')
@router.callback_query(F.data == 'st_pr-11-d')
async def st_pr_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-11-a': False,
        'st_pr-11-b': True,
        'st_pr-11-c': False,
        'st_pr-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Какая толщина гидравлического цилиндра для установки на подвижной раме?\n\n
a) 60 мм.\n
b) 50 мм.\n
c) 45 мм.\n
d) 65 мм.''',
                                      reply_markup=inline_keyboards.st_pr_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-12-a')
@router.callback_query(F.data == 'st_pr-12-b')
@router.callback_query(F.data == 'st_pr-12-c')
@router.callback_query(F.data == 'st_pr-12-d')
async def st_pr_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-12-a': False,
        'st_pr-12-b': True,
        'st_pr-12-c': False,
        'st_pr-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Какое кодовое слово спрятано в видео?\n\n
а) Гидроцилиндр.\n
b) Указатель.\n
c) Проставка.\n
d) Titan''',
                                      reply_markup=inline_keyboards.st_pr_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-13-a')
@router.callback_query(F.data == 'st_pr-13-b')
@router.callback_query(F.data == 'st_pr-13-c')
@router.callback_query(F.data == 'st_pr-13-d')
async def st_pr_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st-13-a': False,
        'st-13-b': False,
        'st-13-c': True,
        'st-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Какая функция помогает предотвратить прокрутку диска вручную?\n\n
a) Автоматический зажим.\n
b) Электропривод вращения вала.\n
c) Ручной механизм фиксации.\n
d) Усилитель давления.''',
                                      reply_markup=inline_keyboards.st_pr_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'st_pr-14-a')
@router.callback_query(F.data == 'st_pr-14-b')
@router.callback_query(F.data == 'st_pr-14-c')
@router.callback_query(F.data == 'st_pr-14-d')
async def st_pr_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'st_pr-14-a': False,
        'st_pr-14-b': True,
        'st_pr-14-c': False,
        'st_pr-14-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 14:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 14:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='st_pr_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 13 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 15

        if user_score >= 13:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/14.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.stanok_dl_shinki()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/14.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 13 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.stanok_dl_pravok_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_st_pr_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_st_pr(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_id_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='id_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по Истории шин!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Сколько лет может пролежать шина в земле, прежде чем полностью разложится?\n\n
a) 1000 лет.\n
b) 10 000 лет.\n
c) 50 000 лет.\n
d) 500 лет.''',
                                      reply_markup=inline_keyboards.id_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'id-1-a')
@router.callback_query(F.data == 'id-1-b')
@router.callback_query(F.data == 'id-1-c')
@router.callback_query(F.data == 'id-1-d')
async def id_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'id-1-a': False,
        'id-1-b': False,
        'id-1-c': True,
        'id-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Кто изобрёл первую резиновую шину?\n\n
a) Карл Бенц.\n
b) Джон Данлоп.\n
c) Томас Эдисон.\n
d) Генри Форд.''',
                                      reply_markup=inline_keyboards.id_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'id-2-a')
@router.callback_query(F.data == 'id-2-b')
@router.callback_query(F.data == 'id-2-c')
@router.callback_query(F.data == 'id-2-d')
async def id_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'id-2-a': False,
        'id-2-b': True,
        'id-2-c': False,
        'id-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Для чего Джон Данлоп изобрёл шину?\n\n
a) Для автомобиля.\n
b) Для велосипеда своего сына.\n
c) Для самолёта.\n
d) Для промышленного оборудования.''',
                                      reply_markup=inline_keyboards.id_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'id-3-a')
@router.callback_query(F.data == 'id-3-b')
@router.callback_query(F.data == 'id-3-c')
@router.callback_query(F.data == 'id-3-d')
async def id_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'id-3-a': False,
        'id-3-b': True,
        'id-3-c': False,
        'id-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Из чего была сделана первая шина Данлопа?\n\n
a) Металл.\n
b) Природный каучук.\n
c) Садовый шланг.\n
d) Синтетическая резина.''',
                               reply_markup=inline_keyboards.id_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'id-4-a')
@router.callback_query(F.data == 'id-4-b')
@router.callback_query(F.data == 'id-4-c')
@router.callback_query(F.data == 'id-4-d')
async def id_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'id-4-a': False,
        'id-4-b': False,
        'id-4-c': True,
        'id-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Почему современные шины черные?\n\n
a) Для снижения их стоимости.\n
b) Из-за использования нефти при производстве.\n
c) Для лучшего сцепления с дорогой.\n
d) Из-за исторической традиции.''',
                                      reply_markup=inline_keyboards.id_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'id-5-a')
@router.callback_query(F.data == 'id-5-b')
@router.callback_query(F.data == 'id-5-c')
@router.callback_query(F.data == 'id-5-d')
async def id_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'id-5-a': False,
        'id-5-b': True,
        'id-5-c': False,
        'id-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какого цвета были борта покрышек до 30-х годов XX века?\n\n
a) Чёрные.\n
b) Кремовые.\n
c) Зелёные.\n
d) Серебристые.''',
                                      reply_markup=inline_keyboards.id_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'id-6-a')
@router.callback_query(F.data == 'id-6-b')
@router.callback_query(F.data == 'id-6-c')
@router.callback_query(F.data == 'id-6-d')
async def id_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'id-6-a': False,
        'id-6-b': True,
        'id-6-c': False,
        'id-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Почему протектор шин был чёрным даже до 30-х годов?\n\n
a) Для стиля.\n
b) Для снижения стоимости.\n
c) Для лучшего сцепления.\n
d) Для эстетики.''',
                                      reply_markup=inline_keyboards.id_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'id-7-a')
@router.callback_query(F.data == 'id-7-b')
@router.callback_query(F.data == 'id-7-c')
@router.callback_query(F.data == 'id-7-d')
async def id_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'id-7-a': False,
        'id-7-b': True,
        'id-7-c': False,
        'id-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какие шины считались признаком современности и стиля в начале XX века?\n\n
a) Полностью чёрные.\n
b) С кремовыми бортами.\n
c) Золотистые.\n
d) Прозрачные.''',
                                      reply_markup=inline_keyboards.id_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'id-8-a')
@router.callback_query(F.data == 'id-8-b')
@router.callback_query(F.data == 'id-8-c')
@router.callback_query(F.data == 'id-8-d')
async def id_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'id-8-a': True,
        'id-8-b': False,
        'id-8-c': False,
        'id-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Какая конструкция шин была распространена изначально?\n\n
a) Камерная.\n
b) Безкамерная.\n
c) С металлическим кордом.\n
d) С синтетическим протектором.''',
                                      reply_markup=inline_keyboards.id_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'id-9-a')
@router.callback_query(F.data == 'id-9-b')
@router.callback_query(F.data == 'id-9-c')
@router.callback_query(F.data == 'id-9-d')
async def id_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'id-9-a': True,
        'id-9-b': False,
        'id-9-c': False,
        'id-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Почему камерные шины часто взрывались?\n\n
a) Из-за плохой установки.\n
b) Из-за перегрева.\n
c) Из-за низкого качества резины.\n
d) Из-за износа.''',
                                      reply_markup=inline_keyboards.id_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'id-10-a')
@router.callback_query(F.data == 'id-10-b')
@router.callback_query(F.data == 'id-10-c')
@router.callback_query(F.data == 'id-10-d')
async def id_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'id-10-a': False,
        'id-10-b': True,
        'id-10-c': False,
        'id-10-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 10:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 10:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='id_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 9 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 11

        if user_score >= 9:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/10.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.ispitaniya_shin()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/10.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 9 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.istoriya_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_id_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_id(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_is_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='is_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по испытаниям шин!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Где обычно размещаются исследовательские центры крупных брендов по производству шин?\n\n
a) Вблизи крупных автодромов.\n
b) На окраинах городов.\n
c) В промышленных зонах.\n
d) На центральных площадях городов.''',
                                      reply_markup=inline_keyboards.is_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'is-1-a')
@router.callback_query(F.data == 'is-1-b')
@router.callback_query(F.data == 'is-1-c')
@router.callback_query(F.data == 'is-1-d')
async def is_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-1-a': False,
        'is-1-b': True,
        'is-1-c': False,
        'is-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Сколько сортов каучука может содержать одна шина?\n\n
a) Один.\n
b) Три.\n
c) Десятки.\n
d) Более ста.''',
                                      reply_markup=inline_keyboards.is_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-2-a')
@router.callback_query(F.data == 'is-2-b')
@router.callback_query(F.data == 'is-2-c')
@router.callback_query(F.data == 'is-2-d')
async def is_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-2-a': False,
        'is-2-b': False,
        'is-2-c': True,
        'is-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Как называется процесс определения химического состава нового сырья для шин?\n\n
a) Ректификация.\n
b) Дистилляция.\n
c) Фильтрация.\n
d) Сублимация.''',
                                      reply_markup=inline_keyboards.is_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-3-a')
@router.callback_query(F.data == 'is-3-b')
@router.callback_query(F.data == 'is-3-c')
@router.callback_query(F.data == 'is-3-d')
async def is_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-3-a': False,
        'is-3-b': True,
        'is-3-c': False,
        'is-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Какую основную функцию выполняет протектор шины?\n\n
a) Обеспечивает надежный контакт с дорогой.\n
b) Снижает шум при движении.\n
c) Уменьшает вес шины.\n
d) Увеличивает тормозной путь.''',
                               reply_markup=inline_keyboards.is_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'is-4-a')
@router.callback_query(F.data == 'is-4-b')
@router.callback_query(F.data == 'is-4-c')
@router.callback_query(F.data == 'is-4-d')
async def is_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-4-a': True,
        'is-4-b': False,
        'is-4-c': False,
        'is-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Чем отличаются протекторы гоночных шин от шин высокой проходимости?\n\n
a) Гоночные шины имеют глубокие канавки.\n
b) Протекторы гоночных шин чаще всего гладкие.\n
c) Шины высокой проходимости всегда шипованные.\n
d) Гоночные шины имеют рисунок для лучшего сцепления с грязью.''',
                                      reply_markup=inline_keyboards.is_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-5-a')
@router.callback_query(F.data == 'is-5-b')
@router.callback_query(F.data == 'is-5-c')
@router.callback_query(F.data == 'is-5-d')
async def is_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-5-a': False,
        'is-5-b': True,
        'is-5-c': False,
        'is-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Сколько времени требуется для ручной вырезки протектора зимней шины?\n\n
a) Более десяти часов.\n
b) Один час.\n
c) Два часа.\n
d) Шесть-восемь часов.''',
                                      reply_markup=inline_keyboards.is_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'is-6-a')
@router.callback_query(F.data == 'is-6-b')
@router.callback_query(F.data == 'is-6-c')
@router.callback_query(F.data == 'is-6-d')
async def is_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-6-a': True,
        'is-6-b': False,
        'is-6-c': False,
        'is-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Что используется для прожига протектора на прототипе шины?\n\n
a) Лазер.\n
b) Газовая горелка.\n
c) Ручной резец.\n
d) Химический раствор.''',
                                      reply_markup=inline_keyboards.is_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-7-a')
@router.callback_query(F.data == 'is-7-b')
@router.callback_query(F.data == 'is-7-c')
@router.callback_query(F.data == 'is-7-d')
async def is_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-7-a': True,
        'is-7-b': False,
        'is-7-c': False,
        'is-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какое давление создается в шине при тестировании на износ?\n\n
a) Давление ниже номинального.\n
b) Номинальное давление.\n
c) Давление выше номинального в несколько раз.\n
d) Атмосферное давление.''',
                                      reply_markup=inline_keyboards.is_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-8-a')
@router.callback_query(F.data == 'is-8-b')
@router.callback_query(F.data == 'is-8-c')
@router.callback_query(F.data == 'is-8-d')
async def is_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-8-a': False,
        'is-8-b': False,
        'is-8-c': True,
        'is-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Что измеряется с помощью чувствительной пластины на испытательном стенде?\n\n
a) Давление в шине.\n
b) Пятно контакта шины.\n
c) Температура протектора.\n
d) Уровень шума.''',
                                      reply_markup=inline_keyboards.is_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-9-a')
@router.callback_query(F.data == 'is-9-b')
@router.callback_query(F.data == 'is-9-c')
@router.callback_query(F.data == 'is-9-d')
async def is_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-9-a': False,
        'is-9-b': True,
        'is-9-c': False,
        'is-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Какое значение имеет равномерное распределение давления в пятне контакта?\n\n
a) Увеличивает скорость автомобиля.\n
b) Снижает расход топлива.\n
c) Уменьшает вес шины.\n
d) Обеспечивает лучшее сцепление с дорогой.''',
                                      reply_markup=inline_keyboards.is_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-10-a')
@router.callback_query(F.data == 'is-10-b')
@router.callback_query(F.data == 'is-10-c')
@router.callback_query(F.data == 'is-10-d')
async def is_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-10-a': False,
        'is-10-b': False,
        'is-10-c': False,
        'is-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Сколько процентов энергии топлива может уходить на сопротивление качению?\n\n
a) 10%.\n
b) 20%.\n
c) 30%.\n
d) 40%.''',
                                      reply_markup=inline_keyboards.is_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-11-a')
@router.callback_query(F.data == 'is-11-b')
@router.callback_query(F.data == 'is-11-c')
@router.callback_query(F.data == 'is-11-d')
async def is_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-11-a': False,
        'is-11-b': False,
        'is-11-c': True,
        'is-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Что происходит с прототипами шин во время жестких тестов?\n\n
a) Они уничтожаются или изнашиваются.\n
b) Они отправляются на продажу.\n
c) Они перерабатываются.\n
d) Они сохраняются для архивов.''',
                                      reply_markup=inline_keyboards.is_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-12-a')
@router.callback_query(F.data == 'is-12-b')
@router.callback_query(F.data == 'is-12-c')
@router.callback_query(F.data == 'is-12-d')
async def is_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-12-a': True,
        'is-12-b': False,
        'is-12-c': False,
        'is-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Какие нюансы учитывают пилоты-испытатели при тестировании шин?\n\n
а) Цвет протектора.\n
b) Громкость шума, комфорт и поведение шин на дороге.\n
c) Вес шин.\n
d) Длину тормозного пути.''',
                                      reply_markup=inline_keyboards.is_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-13-a')
@router.callback_query(F.data == 'is-13-b')
@router.callback_query(F.data == 'is-13-c')
@router.callback_query(F.data == 'is-13-d')
async def is_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-13-a': False,
        'is-13-b': True,
        'is-13-c': False,
        'is-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Какой современный тренд наблюдается в разработке шин?\n\n
a) Увеличение высоты профиля.\n
b) Использование металлического протектора.\n
c) Увеличение количества слоев резины.\n
d) Уменьшение высоты профиля при увеличении посадочного размера.''',
                                      reply_markup=inline_keyboards.is_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-14-a')
@router.callback_query(F.data == 'is-14-b')
@router.callback_query(F.data == 'is-14-c')
@router.callback_query(F.data == 'is-14-d')
async def is_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-14-a': False,
        'is-14-b': False,
        'is-14-c': False,
        'is-14-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Зачем уменьшают высоту профиля шин?\n\n
a) Для установки более крупных тормозных механизмов.\n
b) Для увеличения скорости автомобиля.\n
c) Для улучшения сцепления с дорогой.\n
d) Для экономии материалов.''',
                                      reply_markup=inline_keyboards.is_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-15-a')
@router.callback_query(F.data == 'is-15-b')
@router.callback_query(F.data == 'is-15-c')
@router.callback_query(F.data == 'is-15-d')
async def is_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-15-a': True,
        'is-15-b': False,
        'is-15-c': False,
        'is-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Как создаются мокрые дорожные условия на испытательных треках?\n\n
a) Используются специальные поливочные системы.\n
b) Применяются влажные ковры.\n
c) Располагаются искусственные водоемы.\n
d) Применяются охлаждающие жидкости.''',
                                      reply_markup=inline_keyboards.is_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-16-a')
@router.callback_query(F.data == 'is-16-b')
@router.callback_query(F.data == 'is-16-c')
@router.callback_query(F.data == 'is-16-d')
async def is_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-16-a': False,
        'is-16-b': True,
        'is-16-c': False,
        'is-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Что делает лазер при создании протектора на прототипе?\n\n
a) Вырезает канавки.\n
b) Разогревает резину.\n
c) Прожигает рисунок протектора.\n
d) Измеряет глубину канавок.''',
                                      reply_markup=inline_keyboards.is_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-17-a')
@router.callback_query(F.data == 'is-17-b')
@router.callback_query(F.data == 'is-17-c')
@router.callback_query(F.data == 'is-17-d')
async def is_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-17-a': False,
        'is-17-b': False,
        'is-17-c': True,
        'is-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Какую часть энергии автомобиля тратит шина на деформацию при движении?\n\n
a) До 10%.\n
b) До 30%.\n
c) До 50%.\n
d) До 70%.''',
                                      reply_markup=inline_keyboards.is_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-18-a')
@router.callback_query(F.data == 'is-18-b')
@router.callback_query(F.data == 'is-18-c')
@router.callback_query(F.data == 'is-18-d')
async def is_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-18-a': False,
        'is-18-b': True,
        'is-18-c': False,
        'is-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Почему прототипы шин тестируются на разных автомобилях и пилотах?\n\n
a) Для повышения производительности шин.\n
b) Для ускорения тестирования.\n
c) Для исключения погрешностей испытаний.\n
d) Для снижения затрат.''',
                                      reply_markup=inline_keyboards.is_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-19-a')
@router.callback_query(F.data == 'is-19-b')
@router.callback_query(F.data == 'is-19-c')
@router.callback_query(F.data == 'is-19-d')
async def is_19_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-19-a': False,
        'is-19-b': False,
        'is-19-c': True,
        'is-19-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''20. Сколько шин одного типа производят крупные бренды в год.\n
a) 1 миллион.\n
b) 5 миллионов.\n
c) 12 миллионов.\n
d) 20 миллионов.''',
                                      reply_markup=inline_keyboards.is_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'is-20-a')
@router.callback_query(F.data == 'is-20-b')
@router.callback_query(F.data == 'is-20-c')
@router.callback_query(F.data == 'is-20-d')
async def is_20_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'is-20-a': False,
        'is-20-b': False,
        'is-20-c': True,
        'is-20-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 20:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 20:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='is_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 21

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/20.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.proizvodstvo_shin()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/20.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.ispitaniya_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_is_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_is(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_pr_ds_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='pr_ds_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по параметрам дисков!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что означает параметр 6J на диске?\n\n
a) Ширина диска 6 мм.\n
b) Ширина диска 6 дюймов.\n
c) Диаметр диска 6 дюймов.\n
d) Толщина закраины 6 мм.''',
                                      reply_markup=inline_keyboards.pr_ds_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'pr_ds-1-a')
@router.callback_query(F.data == 'pr_ds-1-b')
@router.callback_query(F.data == 'pr_ds-1-c')
@router.callback_query(F.data == 'pr_ds-1-d')
async def pr_ds_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-1-a': False,
        'pr_ds-1-b': True,
        'pr_ds-1-c': False,
        'pr_ds-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Что обозначает буква J в параметре 6J?\n\n
a) Тип материала диска.\n
b) Диаметр центрального отверстия.\n
c) Форма закраины.\n
d) Тип покраски диска.''',
                                      reply_markup=inline_keyboards.pr_ds_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-2-a')
@router.callback_query(F.data == 'pr_ds-2-b')
@router.callback_query(F.data == 'pr_ds-2-c')
@router.callback_query(F.data == 'pr_ds-2-d')
async def pr_ds_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-2-a': False,
        'pr_ds-2-b': False,
        'pr_ds-2-c': True,
        'pr_ds-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Что обозначает индекс H2?\n\n
a) Высоту закраины диска.\n
b) Наличие двух хампов.\n
c) Тип крепёжных отверстий.\n
d) Диаметр привалочной плоскости.''',
                                      reply_markup=inline_keyboards.pr_ds_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-3-a')
@router.callback_query(F.data == 'pr_ds-3-b')
@router.callback_query(F.data == 'pr_ds-3-c')
@router.callback_query(F.data == 'pr_ds-3-d')
async def pr_ds_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-3-a': False,
        'pr_ds-3-b': True,
        'pr_ds-3-c': False,
        'pr_ds-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Что такое PCD?\n\n
a) Диаметр окружности крепёжных отверстий.\n
b) Количество крепёжных отверстий.\n
c) Ширина диска.\n
d) Тип болтов.''',
                               reply_markup=inline_keyboards.pr_ds_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pr_ds-4-a')
@router.callback_query(F.data == 'pr_ds-4-b')
@router.callback_query(F.data == 'pr_ds-4-c')
@router.callback_query(F.data == 'pr_ds-4-d')
async def pr_ds_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-4-a': True,
        'pr_ds-4-b': False,
        'pr_ds-4-c': False,
        'pr_ds-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Что обозначает параметр ET?\n\n
a) Диаметр диска.\n
b) Вылет диска.\n
c) Толщину закраины.\n
d) Материал диска.''',
                                      reply_markup=inline_keyboards.pr_ds_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-5-a')
@router.callback_query(F.data == 'pr_ds-5-b')
@router.callback_query(F.data == 'pr_ds-5-c')
@router.callback_query(F.data == 'pr_ds-5-d')
async def pr_ds_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-5-a': False,
        'pr_ds-5-b': True,
        'pr_ds-5-c': False,
        'pr_ds-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какова функция хампа на диске?\n\n
a) Удержание бескамерной шины.\n
b) Увеличение жёсткости диска.\n
c) Центрирование диска на ступице.\n
d) Уменьшение веса диска.''',
                                      reply_markup=inline_keyboards.pr_ds_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pr_ds-6-a')
@router.callback_query(F.data == 'pr_ds-6-b')
@router.callback_query(F.data == 'pr_ds-6-c')
@router.callback_query(F.data == 'pr_ds-6-d')
async def pr_ds_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-6-a': True,
        'pr_ds-6-b': False,
        'pr_ds-6-c': False,
        'pr_ds-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Что такое привалочная плоскость?\n\n
a) Поверхность, которой диск прилегает к ступице.\n
b) Внешняя часть закраины.\n
c) Место для установки датчика давления.\n
d) Поверхность крепёжного отверстия.''',
                                      reply_markup=inline_keyboards.pr_ds_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-7-a')
@router.callback_query(F.data == 'pr_ds-7-b')
@router.callback_query(F.data == 'pr_ds-7-c')
@router.callback_query(F.data == 'pr_ds-7-d')
async def pr_ds_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-7-a': True,
        'pr_ds-7-b': False,
        'pr_ds-7-c': False,
        'pr_ds-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Как измеряется ширина диска?\n\n
a) От внешнего края до внешнего края.\n
b) По центральной оси диска.\n
c) По краю полки диска.\n
d) По диаметру закраины.''',
                                      reply_markup=inline_keyboards.pr_ds_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-8-a')
@router.callback_query(F.data == 'pr_ds-8-b')
@router.callback_query(F.data == 'pr_ds-8-c')
@router.callback_query(F.data == 'pr_ds-8-d')
async def pr_ds_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-8-a': False,
        'pr_ds-8-b': False,
        'pr_ds-8-c': True,
        'pr_ds-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Что обозначает параметр 16 в спецификации 6Jx16?\n\n
a) Ширина диска в дюймах.\n
b) Посадочный диаметр шины.\n
c) Количество крепёжных отверстий.\n
d) Высота хампа.''',
                                      reply_markup=inline_keyboards.pr_ds_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-9-a')
@router.callback_query(F.data == 'pr_ds-9-b')
@router.callback_query(F.data == 'pr_ds-9-c')
@router.callback_query(F.data == 'pr_ds-9-d')
async def pr_ds_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-9-a': False,
        'pr_ds-9-b': True,
        'pr_ds-9-c': False,
        'pr_ds-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Почему важно учитывать максимально допустимую нагрузку диска?\n\n
a) Для увеличения срока службы шин.\n
b) Для уменьшения износа тормозных колодок.\n
c) Для улучшения внешнего вида.\n
d) Для предотвращения деформации или поломки.''',
                                      reply_markup=inline_keyboards.pr_ds_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-10-a')
@router.callback_query(F.data == 'pr_ds-10-b')
@router.callback_query(F.data == 'pr_ds-10-c')
@router.callback_query(F.data == 'pr_ds-10-d')
async def pr_ds_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-10-a': False,
        'pr_ds-10-b': False,
        'pr_ds-10-c': False,
        'pr_ds-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Какой параметр важен для предотвращения биений диска?\n\n
a) Диаметр диска.\n
b) Толщина закраины.\n
c) Центральное отверстие.\n
d) Высота хампа.''',
                                      reply_markup=inline_keyboards.pr_ds_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-11-a')
@router.callback_query(F.data == 'pr_ds-11-b')
@router.callback_query(F.data == 'pr_ds-11-c')
@router.callback_query(F.data == 'pr_ds-11-d')
async def pr_ds_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-11-a': False,
        'pr_ds-11-b': False,
        'pr_ds-11-c': True,
        'pr_ds-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Что означает спецификация 5x114.3?\n\n
a) 5 отверстий, диаметр окружности крепёжных отверстий – 114.3 мм.\n
b) 5 отверстий диаметром 114.3 мм.\n
c) 5 крепёжных болтов длиной 114.3 мм.\n
d) Диаметр закраины 114.3 мм.''',
                                      reply_markup=inline_keyboards.pr_ds_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-12-a')
@router.callback_query(F.data == 'pr_ds-12-b')
@router.callback_query(F.data == 'pr_ds-12-c')
@router.callback_query(F.data == 'pr_ds-12-d')
async def pr_ds_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-12-a': True,
        'pr_ds-12-b': False,
        'pr_ds-12-c': False,
        'pr_ds-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Чем опасна неправильная развёртка PCD?\n\n
а) Увеличится износ шин.\n
b) Диск не подойдёт к ступице.\n
c) Снизится эффективность торможения.\n
d) Увеличится вес автомобиля.''',
                                      reply_markup=inline_keyboards.pr_ds_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-13-a')
@router.callback_query(F.data == 'pr_ds-13-b')
@router.callback_query(F.data == 'pr_ds-13-c')
@router.callback_query(F.data == 'pr_ds-13-d')
async def pr_ds_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-13-a': False,
        'pr_ds-13-b': True,
        'pr_ds-13-c': False,
        'pr_ds-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Какую нагрузку должен выдерживать один диск для автомобиля весом 4 тонны?\n\n
a) 500 кг.\n
b) 1 тонна.\n
c) 1.5 тонны.\n
d) 2 тонны.''',
                                      reply_markup=inline_keyboards.pr_ds_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-14-a')
@router.callback_query(F.data == 'pr_ds-14-b')
@router.callback_query(F.data == 'pr_ds-14-c')
@router.callback_query(F.data == 'pr_ds-14-d')
async def pr_ds_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-14-a': False,
        'pr_ds-14-b': True,
        'pr_ds-14-c': False,
        'pr_ds-14-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Для чего используются центровочные кольца?\n\n
a) Для центрирования диска на ступице.\n
b) Для уменьшения веса диска.\n
c) Для увеличения нагрузки на диск.\n
d) Для предотвращения коррозии диска.''',
                                      reply_markup=inline_keyboards.pr_ds_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-15-a')
@router.callback_query(F.data == 'pr_ds-15-b')
@router.callback_query(F.data == 'pr_ds-15-c')
@router.callback_query(F.data == 'pr_ds-15-d')
async def pr_ds_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-15-a': True,
        'pr_ds-15-b': False,
        'pr_ds-15-c': False,
        'pr_ds-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Какой параметр определяет соответствие диска размеру ступицы?\n\n
a) H2.\n
b) Центральное отверстие.\n
c) PCD.\n
d) Высота закраины.''',
                                      reply_markup=inline_keyboards.pr_ds_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-16-a')
@router.callback_query(F.data == 'pr_ds-16-b')
@router.callback_query(F.data == 'pr_ds-16-c')
@router.callback_query(F.data == 'pr_ds-16-d')
async def pr_ds_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-16-a': False,
        'pr_ds-16-b': True,
        'pr_ds-16-c': False,
        'pr_ds-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Что такое универсальное центральное отверстие?\n\n
a) Отверстие фиксированного размера.\n
b) Отверстие для крепёжных болтов.\n
c) Отверстие большего размера, адаптируемое для разных ступиц.\n
d) Отверстие для установки вентиля.''',
                                      reply_markup=inline_keyboards.pr_ds_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-17-a')
@router.callback_query(F.data == 'pr_ds-17-b')
@router.callback_query(F.data == 'pr_ds-17-c')
@router.callback_query(F.data == 'pr_ds-17-d')
async def pr_ds_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-17-a': False,
        'pr_ds-17-b': False,
        'pr_ds-17-c': True,
        'pr_ds-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Как влияет неправильный вылет диска (ET) на автомобиль?\n\n
a) Уменьшает вес автомобиля.\n
b) Увеличивает износ шин и нагрузку на подвеску.\n
c) Снижает расход топлива.\n
d) Увеличивает диаметр диска.''',
                                      reply_markup=inline_keyboards.pr_ds_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-18-a')
@router.callback_query(F.data == 'pr_ds-18-b')
@router.callback_query(F.data == 'pr_ds-18-c')
@router.callback_query(F.data == 'pr_ds-18-d')
async def pr_ds_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-18-a': False,
        'pr_ds-18-b': True,
        'pr_ds-18-c': False,
        'pr_ds-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Какой параметр важен при установке датчиков давления?\n\n
a) Высота закраины.\n
b) Диаметр хампа.\n
c) Наличие специальной площадки под датчик.\n
d) Тип болтов.''',
                                      reply_markup=inline_keyboards.pr_ds_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-19-a')
@router.callback_query(F.data == 'pr_ds-19-b')
@router.callback_query(F.data == 'pr_ds-19-c')
@router.callback_query(F.data == 'pr_ds-19-d')
async def pr_ds_19_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-19-a': False,
        'pr_ds-19-b': False,
        'pr_ds-19-c': True,
        'pr_ds-19-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''20. Почему важна правильная конфигурация крепёжной части диска.\n
a) Для улучшения внешнего вида.\n
b) Для уменьшения веса автомобиля.\n
c) Для надёжного закрепления диска.\n
d) Для увеличения диаметра закраины.''',
                                      reply_markup=inline_keyboards.pr_ds_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pr_ds-20-a')
@router.callback_query(F.data == 'pr_ds-20-b')
@router.callback_query(F.data == 'pr_ds-20-c')
@router.callback_query(F.data == 'pr_ds-20-d')
async def pr_ds_20_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pr_ds-20-a': False,
        'pr_ds-20-b': False,
        'pr_ds-20-c': True,
        'pr_ds-20-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 20:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 20:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='pr_ds_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 21

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/20.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.kolca()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/20.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.parametri_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_pr_ds_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_pr_ds(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_kd_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='kd_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по кольцам для литых дисков!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Для чего используются проставочные кольца?\n\n
a) Для увеличения диаметра диска.\n
b) Для уменьшения центрального отверстия до нужного диаметра.\n
c) Для фиксации вентиля.\n
d) Для улучшения дизайна дисков.''',
                                      reply_markup=inline_keyboards.kd_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'kd-1-a')
@router.callback_query(F.data == 'kd-1-b')
@router.callback_query(F.data == 'kd-1-c')
@router.callback_query(F.data == 'kd-1-d')
async def kd_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'kd-1-a': False,
        'kd-1-b': True,
        'kd-1-c': False,
        'kd-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Что означает термин “универсальное центральное отверстие?\n\n
a) Отверстие стандартного размера.\n
b) Отверстие для установки вентиля.\n
c) Максимально большое центральное отверстие, которое адаптируется кольцами.\n
d) Отверстие, используемое только на спортивных дисках.''',
                                      reply_markup=inline_keyboards.kd_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'kd-2-a')
@router.callback_query(F.data == 'kd-2-b')
@router.callback_query(F.data == 'kd-2-c')
@router.callback_query(F.data == 'kd-2-d')
async def kd_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'kd-2-a': False,
        'kd-2-b': False,
        'kd-2-c': True,
        'kd-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Какие материалы используются для изготовления проставочных колец?\n\n
a) Только сталь.\n
b) Пластик и алюминий.\n
c) Карбон.\n
d) Дерево.''',
                                      reply_markup=inline_keyboards.kd_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'kd-3-a')
@router.callback_query(F.data == 'kd-3-b')
@router.callback_query(F.data == 'kd-3-c')
@router.callback_query(F.data == 'kd-3-d')
async def kd_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'kd-3-a': False,
        'kd-3-b': True,
        'kd-3-c': False,
        'kd-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Какой главный минус пластиковых колец?\n\n
a) Плохая устойчивость к перегреву и трещины при использовании .\n
b) Высокая стоимость.\n
c) Сложность установки.\n
d) Необходимость регулярной замены.''',
                               reply_markup=inline_keyboards.kd_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'kd-4-a')
@router.callback_query(F.data == 'kd-4-b')
@router.callback_query(F.data == 'kd-4-c')
@router.callback_query(F.data == 'kd-4-d')
async def kd_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'kd-4-a': True,
        'kd-4-b': False,
        'kd-4-c': False,
        'kd-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Чем алюминиевые кольца отличаются от пластиковых?\n\n
a) Они легче и дешевле.\n
b) Они дороже, но обеспечивают более жёсткую конструкцию.\n
c) Они меньше по размеру.\n
d) Они используются только на спортивных автомобилях.''',
                                      reply_markup=inline_keyboards.kd_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'kd-5-a')
@router.callback_query(F.data == 'kd-5-b')
@router.callback_query(F.data == 'kd-5-c')
@router.callback_query(F.data == 'kd-5-d')
async def kd_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'kd-5-a': False,
        'kd-5-b': True,
        'kd-5-c': False,
        'kd-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какой параметр диска позволяет использовать универсальные кольца?\n\n
a) Большое центральное отверстие.\n
b) PCD.\n
c) Вылет диска.\n
d) Высота закраины.''',
                                      reply_markup=inline_keyboards.kd_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'kd-6-a')
@router.callback_query(F.data == 'kd-6-b')
@router.callback_query(F.data == 'kd-6-c')
@router.callback_query(F.data == 'kd-6-d')
async def kd_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'kd-6-a': True,
        'kd-6-b': False,
        'kd-6-c': False,
        'kd-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Какие автомобили чаще всего используют развёртку 5x114.3?\n\n
a) Азиатские.\n
b) Немецкие.\n
c) Европейские.\n
d) Американские.''',
                                      reply_markup=inline_keyboards.kd_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'kd-7-a')
@router.callback_query(F.data == 'kd-7-b')
@router.callback_query(F.data == 'kd-7-c')
@router.callback_query(F.data == 'kd-7-d')
async def kd_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'kd-7-a': True,
        'kd-7-b': False,
        'kd-7-c': False,
        'kd-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Почему пластиковые кольца не прикипают к диску?\n\n
a) Из-за смазки, нанесённой на кольцо.\n
b) Из-за меньшей нагрузки.\n
c) Из-за своей структуры.\n
d) Из-за особенности крепежа.''',
                                      reply_markup=inline_keyboards.kd_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'kd-8-a')
@router.callback_query(F.data == 'kd-8-b')
@router.callback_query(F.data == 'kd-8-c')
@router.callback_query(F.data == 'kd-8-d')
async def kd_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'kd-8-a': False,
        'kd-8-b': False,
        'kd-8-c': True,
        'kd-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Как избежать прикипания алюминиевых колец?\n\n
a) Использовать дополнительные болты.\n
b) Смазывать кольца моторным или силиконовым маслом.\n
c) Устанавливать пластиковые аналоги.\n
d) Не использовать кольца при установке дисков.''',
                                      reply_markup=inline_keyboards.kd_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'kd-9-a')
@router.callback_query(F.data == 'kd-9-b')
@router.callback_query(F.data == 'kd-9-c')
@router.callback_query(F.data == 'kd-9-d')
async def kd_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'kd-9-a': False,
        'kd-9-b': True,
        'kd-9-c': False,
        'kd-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Что происходит, если использовать кольца ненадлежащего качества?\n\n
a) Увеличивается вес автомобиля.\n
b) Увеличивается расход топлива.\n
c) Улучшается сцепление с дорогой.\n
d) Диск плохо центрируется, возможны биения.''',
                                      reply_markup=inline_keyboards.kd_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'kd-10-a')
@router.callback_query(F.data == 'kd-10-b')
@router.callback_query(F.data == 'kd-10-c')
@router.callback_query(F.data == 'kd-10-d')
async def kd_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'kd-10-a': False,
        'kd-10-b': False,
        'kd-10-c': False,
        'kd-10-d': True,
    }

    if dict_to_check_progress[callback.from_user.id] == 10:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 10:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='kd_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 9 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 11

        if user_score >= 9:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/10.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.shinshik()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/10.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 9 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.kolca_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_kd_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_kd(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_ot_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='ot_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по отличиям дисков!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Почему штампованные диски самые дешевые?\n\n
a) Производятся из алюминия, что снижает стоимость.\n
b) Производятся из стали и имеют массовое производство.\n
c) Они менее популярны, поэтому продаются дешевле.\n
d) Их изготавливают вручную, что снижает цену.''',
                                      reply_markup=inline_keyboards.ot_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'ot-1-a')
@router.callback_query(F.data == 'ot-1-b')
@router.callback_query(F.data == 'ot-1-c')
@router.callback_query(F.data == 'ot-1-d')
async def ot_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-1-a': False,
        'ot-1-b': True,
        'ot-1-c': False,
        'ot-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какой процесс используется для соединения обода и диска в штампованных дисках?\n\n
a) Ручная сварка.\n
b) Литье под давлением.\n
c) 4-точечная автоматическая сварка в газовой среде.\n
d) Склеивание эпоксидной смолой.''',
                                      reply_markup=inline_keyboards.ot_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-2-a')
@router.callback_query(F.data == 'ot-2-b')
@router.callback_query(F.data == 'ot-2-c')
@router.callback_query(F.data == 'ot-2-d')
async def ot_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-2-a': False,
        'ot-2-b': False,
        'ot-2-c': True,
        'ot-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Почему литые диски называются именно так?\n\n
a) Они изготавливаются из легированной стали.\n
b) Они изготавливаются путем заливки расплавленного алюминиевого сплава в форму.\n
c) Их вырезают из цельного блока металла.\n
d) Они создаются с использованием порошковой технологии.''',
                                      reply_markup=inline_keyboards.ot_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-3-a')
@router.callback_query(F.data == 'ot-3-b')
@router.callback_query(F.data == 'ot-3-c')
@router.callback_query(F.data == 'ot-3-d')
async def ot_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-3-a': False,
        'ot-3-b': True,
        'ot-3-c': False,
        'ot-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Что является основным недостатком литых дисков?\n\n
a) Риск появления трещин при нарушении технологии производства.\n
b) Сложность покраски.\n
c) Склонность к деформации при низких температурах.\n
d) Трудности с утилизацией.''',
                               reply_markup=inline_keyboards.ot_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ot-4-a')
@router.callback_query(F.data == 'ot-4-b')
@router.callback_query(F.data == 'ot-4-c')
@router.callback_query(F.data == 'ot-4-d')
async def ot_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-4-a': True,
        'ot-4-b': False,
        'ot-4-c': False,
        'ot-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Какая особенность кованых дисков делает их столь прочными?\n\n
a) Использование титанового сплава.\n
b) Обработка давлением, изменяющая структуру металла.\n
c) Закалка при сверхвысоких температурах.\n
d) Покрытие эпоксидной смолой.''',
                                      reply_markup=inline_keyboards.ot_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-5-a')
@router.callback_query(F.data == 'ot-5-b')
@router.callback_query(F.data == 'ot-5-c')
@router.callback_query(F.data == 'ot-5-d')
async def ot_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-5-a': False,
        'ot-5-b': True,
        'ot-5-c': False,
        'ot-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Что означает термин "авиационный алюминий", используемый в кованых дисках?\n\n
a) Сплав, обладающий прочностью стали и легкостью алюминия.\n
b) Алюминий, произведенный на аэрокосмических предприятиях.\n
c) Сплав, используемый только в авиации.\n
d) Особая технология закалки металла.''',
                                      reply_markup=inline_keyboards.ot_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ot-6-a')
@router.callback_query(F.data == 'ot-6-b')
@router.callback_query(F.data == 'ot-6-c')
@router.callback_query(F.data == 'ot-6-d')
async def ot_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-6-a': True,
        'ot-6-b': False,
        'ot-6-c': False,
        'ot-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Сколько весит кованый диск по сравнению с карбоновым?\n\n
a) Карбоновый диск легче.\n
b) Они весят одинаково.\n
c) Кованый диск легче.\n
d) Вес зависит от производителя.''',
                                      reply_markup=inline_keyboards.ot_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-7-a')
@router.callback_query(F.data == 'ot-7-b')
@router.callback_query(F.data == 'ot-7-c')
@router.callback_query(F.data == 'ot-7-d')
async def ot_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-7-a': True,
        'ot-7-b': False,
        'ot-7-c': False,
        'ot-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какой уникальный материал используется для изготовления дисков на Koenigsegg?\n\n
a) Титановый сплав.\n
b) Алюминиевый композит.\n
c) Углеродное волокно (карбон).\n
d) Магний.''',
                                      reply_markup=inline_keyboards.ot_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-8-a')
@router.callback_query(F.data == 'ot-8-b')
@router.callback_query(F.data == 'ot-8-c')
@router.callback_query(F.data == 'ot-8-d')
async def ot_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-8-a': False,
        'ot-8-b': False,
        'ot-8-c': True,
        'ot-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Какую нагрузку выдерживают карбоновые диски?\n\n
a) Они гнутся под большими нагрузками.\n
b) Они либо остаются целыми, либо ломаются при экстремальной нагрузке.\n
c) Они гнутся при любых нагрузках.\n
d) Они ломаются при контакте с бордюром.''',
                                      reply_markup=inline_keyboards.ot_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-9-a')
@router.callback_query(F.data == 'ot-9-b')
@router.callback_query(F.data == 'ot-9-c')
@router.callback_query(F.data == 'ot-9-d')
async def ot_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-9-a': False,
        'ot-9-b': True,
        'ot-9-c': False,
        'ot-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Каким автомобилям принадлежат первые карбоновые диски в серийном производстве?\n\n
a) Ferrari.\n
b) Lamborghini.\n
c) McLaren.\n
d) Koenigsegg.''',
                                      reply_markup=inline_keyboards.ot_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-10-a')
@router.callback_query(F.data == 'ot-10-b')
@router.callback_query(F.data == 'ot-10-c')
@router.callback_query(F.data == 'ot-10-d')
async def ot_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-10-a': False,
        'ot-10-b': False,
        'ot-10-c': False,
        'ot-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Почему облегченные диски улучшают динамику автомобиля?\n\n
a) Снижается расход топлива.\n
b) Увеличивается сцепление с дорогой.\n
c) Они быстрее вращаются, снижая инерцию.\n
d) Уменьшается износ шин.''',
                                      reply_markup=inline_keyboards.ot_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-11-a')
@router.callback_query(F.data == 'ot-11-b')
@router.callback_query(F.data == 'ot-11-c')
@router.callback_query(F.data == 'ot-11-d')
async def ot_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-11-a': False,
        'ot-11-b': False,
        'ot-11-c': True,
        'ot-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Какой основной риск связан с дешевыми литыми дисками?\n\n
a) Возможность разрушения на ходу из-за трещин.\n
b) Потеря внешнего вида.\n
c) Образование коррозии.\n
d) Низкая устойчивость к температурным перепадам.''',
                                      reply_markup=inline_keyboards.ot_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-12-a')
@router.callback_query(F.data == 'ot-12-b')
@router.callback_query(F.data == 'ot-12-c')
@router.callback_query(F.data == 'ot-12-d')
async def ot_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-12-a': True,
        'ot-12-b': False,
        'ot-12-c': False,
        'ot-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Какой тип дисков лучше выдерживает удар об бордюр?\n\n
а) Литые.\n
b) Кованые.\n
c) Штампованные.\n
d) Карбоновые.''',
                                      reply_markup=inline_keyboards.ot_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-13-a')
@router.callback_query(F.data == 'ot-13-b')
@router.callback_query(F.data == 'ot-13-c')
@router.callback_query(F.data == 'ot-13-d')
async def ot_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-13-a': False,
        'ot-13-b': True,
        'ot-13-c': False,
        'ot-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Почему штампованные диски чаще подвергаются ремонту, чем замене?\n\n
a) Они изначально дороже.\n
b) Их легко отремонтировать и восстановить.\n
c) Ремонт обходится дешевле, чем производство новых.\n
d) У них высокий запас прочности.''',
                                      reply_markup=inline_keyboards.ot_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-14-a')
@router.callback_query(F.data == 'ot-14-b')
@router.callback_query(F.data == 'ot-14-c')
@router.callback_query(F.data == 'ot-14-d')
async def ot_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-14-a': False,
        'ot-14-b': True,
        'ot-14-c': False,
        'ot-14-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Чем обусловлена высокая стоимость карбоновых дисков?\n\n
a) Высокая сложность и эксклюзивность производства.\n
b) Использование дорогого сырья.\n
c) Высокая трудоемкость ручной сборки.\n
d) Ограниченный спрос на рынке.''',
                                      reply_markup=inline_keyboards.ot_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-15-a')
@router.callback_query(F.data == 'ot-15-b')
@router.callback_query(F.data == 'ot-15-c')
@router.callback_query(F.data == 'ot-15-d')
async def ot_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-15-a': True,
        'ot-15-b': False,
        'ot-15-c': False,
        'ot-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Какие преимущества дают кованые диски в условиях спортивной эксплуатации?\n\n
a) Меньший вес и лучшая управляемость.\n
b) Минимальная деформация и способность выдерживать высокие нагрузки.\n
c) Устойчивость к высокой температуре.\n
d) Возможность изменения формы под нагрузкой.''',
                                      reply_markup=inline_keyboards.ot_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ot-16-a')
@router.callback_query(F.data == 'ot-16-b')
@router.callback_query(F.data == 'ot-16-c')
@router.callback_query(F.data == 'ot-16-d')
async def ot_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ot-16-a': False,
        'ot-16-b': True,
        'ot-16-c': False,
        'ot-16-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 16:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 16:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='ot_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 15 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 17

        if user_score >= 15:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/16.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.parametri_diskov()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/16.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 15 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.litorkovka_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_ot_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_ot(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_mk_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='mk_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по маркировки шин!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что означает цифра 255 в маркировке шины 255/55R16?\n\n
a) Диаметр шины в дюймах.\n
b) Ширина шины в миллиметрах.\n
c) Высота профиля шины.\n
d) Максимальная нагрузка на шину.''',
                                      reply_markup=inline_keyboards.mk_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'mk-1-a')
@router.callback_query(F.data == 'mk-1-b')
@router.callback_query(F.data == 'mk-1-c')
@router.callback_query(F.data == 'mk-1-d')
async def mk_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-1-a': False,
        'mk-1-b': True,
        'mk-1-c': False,
        'mk-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Как определяется высота профиля шины?\n\n
a) Как фиксированное значение для всех шин.\n
b) В миллиметрах, указанных на боковине шины.\n
c) В процентах от ширины шины.\n
d) Как сумма ширины и диаметра шины.''',
                                      reply_markup=inline_keyboards.mk_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-2-a')
@router.callback_query(F.data == 'mk-2-b')
@router.callback_query(F.data == 'mk-2-c')
@router.callback_query(F.data == 'mk-2-d')
async def mk_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-2-a': False,
        'mk-2-b': False,
        'mk-2-c': True,
        'mk-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Что означает буква R в маркировке шин?\n\n
a) Радиус шины.\n
b) Радиальная конструкция.\n
c) Размер центрального отверстия.\n
d) Тип резиновой смеси.''',
                                      reply_markup=inline_keyboards.mk_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-3-a')
@router.callback_query(F.data == 'mk-3-b')
@router.callback_query(F.data == 'mk-3-c')
@router.callback_query(F.data == 'mk-3-d')
async def mk_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-3-a': False,
        'mk-3-b': True,
        'mk-3-c': False,
        'mk-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Что показывает индекс нагрузки в маркировке шин?\n\n
a) Максимальную нагрузку на одну шину.\n
b) Максимально допустимую скорость.\n
c) Давление в шине.\n
d) Толщину боковины.''',
                               reply_markup=inline_keyboards.mk_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'mk-4-a')
@router.callback_query(F.data == 'mk-4-b')
@router.callback_query(F.data == 'mk-4-c')
@router.callback_query(F.data == 'mk-4-d')
async def mk_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-4-a': True,
        'mk-4-b': False,
        'mk-4-c': False,
        'mk-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Как расшифровывается индекс скорости шины?\n\n
a) Рекомендуемая скорость для безопасного вождения.\n
b) Максимальная скорость, при которой шина сохраняет свои характеристики.\n
c) Скорость, при которой шина начинает разрушаться.\n
d) Минимальная скорость для эксплуатации.''',
                                      reply_markup=inline_keyboards.mk_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-5-a')
@router.callback_query(F.data == 'mk-5-b')
@router.callback_query(F.data == 'mk-5-c')
@router.callback_query(F.data == 'mk-5-d')
async def mk_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-5-a': False,
        'mk-5-b': True,
        'mk-5-c': False,
        'mk-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Что означает маркировка 91V на шине?\n\n
a) Индекс нагрузки 91 и максимальная скорость 240 км/ч.\n
b) Максимальное давление 91 и скорость 240 км/ч.\n
c) Диаметр шины 91 мм и скорость 240 км/ч.\n
d) Нагрузка 240 кг и индекс скорости V.''',
                                      reply_markup=inline_keyboards.mk_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'mk-6-a')
@router.callback_query(F.data == 'mk-6-b')
@router.callback_query(F.data == 'mk-6-c')
@router.callback_query(F.data == 'mk-6-d')
async def mk_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-6-a': True,
        'mk-6-b': False,
        'mk-6-c': False,
        'mk-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Как определяется дата производства шины?\n\n
a) По четырём цифрам на боковине: первые две — неделя, вторые две — год.\n
b) По маркировке на внутренней части шины.\n
c) По первым двум цифрам, обозначающим месяц.\n
d) По цвету маркировки.''',
                                      reply_markup=inline_keyboards.mk_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-7-a')
@router.callback_query(F.data == 'mk-7-b')
@router.callback_query(F.data == 'mk-7-c')
@router.callback_query(F.data == 'mk-7-d')
async def mk_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-7-a': True,
        'mk-7-b': False,
        'mk-7-c': False,
        'mk-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Что означает маркировка M+S на шинах?\n\n
a) Зимняя шина.\n
b) Усиленная конструкция шины.\n
c) Грязь и снег.\n
d) Покрышка для спортивных автомобилей.''',
                                      reply_markup=inline_keyboards.mk_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-8-a')
@router.callback_query(F.data == 'mk-8-b')
@router.callback_query(F.data == 'mk-8-c')
@router.callback_query(F.data == 'mk-8-d')
async def mk_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-8-a': False,
        'mk-8-b': False,
        'mk-8-c': True,
        'mk-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Какая маркировка указывает на зимнюю шину?\n\n
a) M+S.\n
b) Снежинка или пик горы.\n
c) RAIN.\n
d) AQUA.''',
                                      reply_markup=inline_keyboards.mk_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-9-a')
@router.callback_query(F.data == 'mk-9-b')
@router.callback_query(F.data == 'mk-9-c')
@router.callback_query(F.data == 'mk-9-d')
async def mk_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-9-a': False,
        'mk-9-b': True,
        'mk-9-c': False,
        'mk-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Что показывает маркировка XL на шинах?\n\n
a) Увеличенный радиус шины.\n
b) Шина для спортивных автомобилей.\n
c) Шина с дополнительной защитой от проколов.\n
d) Усиленная конструкция с повышенным индексом нагрузки.''',
                                      reply_markup=inline_keyboards.mk_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-10-a')
@router.callback_query(F.data == 'mk-10-b')
@router.callback_query(F.data == 'mk-10-c')
@router.callback_query(F.data == 'mk-10-d')
async def mk_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-10-a': False,
        'mk-10-b': False,
        'mk-10-c': False,
        'mk-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Какая маркировка обозначает шины с возможностью езды при проколе?\n\n
a) M+S.\n
b) XL.\n
c) RunFlat или RFT.\n
d) INSIDE.''',
                                      reply_markup=inline_keyboards.mk_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-11-a')
@router.callback_query(F.data == 'mk-11-b')
@router.callback_query(F.data == 'mk-11-c')
@router.callback_query(F.data == 'mk-11-d')
async def mk_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-11-a': False,
        'mk-11-b': False,
        'mk-11-c': True,
        'mk-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Что означает маркировка OUTSIDE на шине?\n\n
a) Внешняя сторона асимметричной шины.\n
b) Направление движения шины.\n
c) Индекс нагрузки шины.\n
d) Тип протектора.''',
                                      reply_markup=inline_keyboards.mk_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-12-a')
@router.callback_query(F.data == 'mk-12-b')
@router.callback_query(F.data == 'mk-12-c')
@router.callback_query(F.data == 'mk-12-d')
async def mk_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-12-a': True,
        'mk-12-b': False,
        'mk-12-c': False,
        'mk-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Что означает маркировка TUBELESS?\n\n
а) Камерная шина.\n
b) Бескамерная шина.\n
c) Усиленная шина.\n
d) Шина с металлическим кордом.''',
                                      reply_markup=inline_keyboards.mk_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-13-a')
@router.callback_query(F.data == 'mk-13-b')
@router.callback_query(F.data == 'mk-13-c')
@router.callback_query(F.data == 'mk-13-d')
async def mk_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-13-a': False,
        'mk-13-b': True,
        'mk-13-c': False,
        'mk-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Какие данные включены в европейскую маркировку шин?\n\n
a) Индекс износа, шумность, сцепление на снегу.\n
b) Максимальная нагрузка, индекс скорости, сцепление с дорогой.\n
c) Сопротивление качению, тип конструкции, радиус шины.\n
d) Топливная экономичность, сцепление на мокрой дороге, шумность.''',
                                      reply_markup=inline_keyboards.mk_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-14-a')
@router.callback_query(F.data == 'mk-14-b')
@router.callback_query(F.data == 'mk-14-c')
@router.callback_query(F.data == 'mk-14-d')
async def mk_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-14-a': False,
        'mk-14-b': False,
        'mk-14-c': False,
        'mk-14-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Чем отличаются шины с маркировкой STUDLESS?\n\n
a) Они предназначены для использования без шипов.\n
b) Они имеют шипы.\n
c) Они не подходят для зимних условий.\n
d) Они предназначены только для летнего использования.''',
                                      reply_markup=inline_keyboards.mk_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-15-a')
@router.callback_query(F.data == 'mk-15-b')
@router.callback_query(F.data == 'mk-15-c')
@router.callback_query(F.data == 'mk-15-d')
async def mk_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-15-a': True,
        'mk-15-b': False,
        'mk-15-c': False,
        'mk-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Какой класс шума является самым тихим в европейской маркировке?\n\n
a) C.\n
b) A.\n
c) E.\n
d) G.''',
                                      reply_markup=inline_keyboards.mk_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-16-a')
@router.callback_query(F.data == 'mk-16-b')
@router.callback_query(F.data == 'mk-16-c')
@router.callback_query(F.data == 'mk-16-d')
async def mk_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-16-a': False,
        'mk-16-b': True,
        'mk-16-c': False,
        'mk-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Что означает индекс A в классе сцепления на мокрой дороге?\n\n
a) Наихудший показатель.\n
b) Средний уровень сцепления.\n
c) Лучший показатель сцепления.\n
d) Сцепление для зимних дорог.''',
                                      reply_markup=inline_keyboards.mk_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-17-a')
@router.callback_query(F.data == 'mk-17-b')
@router.callback_query(F.data == 'mk-17-c')
@router.callback_query(F.data == 'mk-17-d')
async def mk_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-17-a': False,
        'mk-17-b': False,
        'mk-17-c': True,
        'mk-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Какой параметр указывает на сопротивление качению шины?\n\n
a) Индекс нагрузки.\n
b) Индекс топливной экономичности.\n
c) Индекс сцепления.\n
d) Индекс скорости.''',
                                      reply_markup=inline_keyboards.mk_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-18-a')
@router.callback_query(F.data == 'mk-18-b')
@router.callback_query(F.data == 'mk-18-c')
@router.callback_query(F.data == 'mk-18-d')
async def mk_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-18-a': False,
        'mk-18-b': True,
        'mk-18-c': False,
        'mk-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Какие шины маркируются словом AQUA?\n\n
a) Зимние шины.\n
b) Спортивные шины.\n
c) Шины для условий с большим количеством воды.\n
d) Усиленные шины.''',
                                      reply_markup=inline_keyboards.mk_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-19-a')
@router.callback_query(F.data == 'mk-19-b')
@router.callback_query(F.data == 'mk-19-c')
@router.callback_query(F.data == 'mk-19-d')
async def mk_19_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-19-a': False,
        'mk-19-b': False,
        'mk-19-c': True,
        'mk-19-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''20. Что означает символ зонта на боковине шины?\n
a) Шина с усиленной конструкцией.\n
b) Шина для зимнего использования.\n
c) Шина для мокрой поверхности.\n
d) Шина с увеличенным индексом нагрузки.''',
                                      reply_markup=inline_keyboards.mk_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'mk-20-a')
@router.callback_query(F.data == 'mk-20-b')
@router.callback_query(F.data == 'mk-20-c')
@router.callback_query(F.data == 'mk-20-d')
async def mk_20_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'mk-20-a': False,
        'mk-20-b': False,
        'mk-20-c': True,
        'mk-20-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 20:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 20:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='mk_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 21

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/20.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.shinka_disk()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/20.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.markirovka_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_mk_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_mk(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_pz_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='pz_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по ремонту шин с порезом!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Какое первое действие выполняется после обнаружения пореза?\n\n
a) Вскрыть шину.\n
b) Отметить порез мелом.\n
c) Протереть шину растворителем.\n
d) Нанести клей.''',
                                      reply_markup=inline_keyboards.pz_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'pz-1-a')
@router.callback_query(F.data == 'pz-1-b')
@router.callback_query(F.data == 'pz-1-c')
@router.callback_query(F.data == 'pz-1-d')
async def pz_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-1-a': False,
        'pz-1-b': True,
        'pz-1-c': False,
        'pz-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Как правильно выкручивать золотник?\n\n
a) Резким движением.\n
b) Плоскогубцами.\n
c) Используя специальный инструмент.\n
d) Руками.''',
                                      reply_markup=inline_keyboards.pz_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-2-a')
@router.callback_query(F.data == 'pz-2-b')
@router.callback_query(F.data == 'pz-2-c')
@router.callback_query(F.data == 'pz-2-d')
async def pz_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-2-a': False,
        'pz-2-b': False,
        'pz-2-c': True,
        'pz-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. В каком направлении нужно размещать вентиль при работе с колесом?\n\n
a) Под углом 45 градусов.\n
b) Всегда к себе.\n
c) В сторону от мастера.\n
d) Перпендикулярно полу.''',
                                      reply_markup=inline_keyboards.pz_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-3-a')
@router.callback_query(F.data == 'pz-3-b')
@router.callback_query(F.data == 'pz-3-c')
@router.callback_query(F.data == 'pz-3-d')
async def pz_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-3-a': False,
        'pz-3-b': True,
        'pz-3-c': False,
        'pz-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Почему важно снимать балансировочные грузы перед ремонтом?\n\n
a) Чтобы не мешали проворачивать колесо.\n
b) Для облегчения шины.\n
c) Чтобы не повредить золотник.\n
d) Для доступа к порезу.''',
                               reply_markup=inline_keyboards.pz_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pz-4-a')
@router.callback_query(F.data == 'pz-4-b')
@router.callback_query(F.data == 'pz-4-c')
@router.callback_query(F.data == 'pz-4-d')
async def pz_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-4-a': True,
        'pz-4-b': False,
        'pz-4-c': False,
        'pz-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Для чего используется мел при подготовке к ремонту?\n\n
a) Для измерения глубины пореза.\n
b) Для маркировки места пореза.\n
c) Для удаления грязи.\n
d) Для отметки давления в шине.''',
                                      reply_markup=inline_keyboards.pz_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-5-a')
@router.callback_query(F.data == 'pz-5-b')
@router.callback_query(F.data == 'pz-5-c')
@router.callback_query(F.data == 'pz-5-d')
async def pz_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-5-a': False,
        'pz-5-b': True,
        'pz-5-c': False,
        'pz-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какая латка используется для ремонта большого пореза?\n\n
a) С двумя слоями корда.\n
b) С одним слоем корда.\n
c) Универсальная латка.\n
d) Без дополнительных слоев.''',
                                      reply_markup=inline_keyboards.pz_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pz-6-a')
@router.callback_query(F.data == 'pz-6-b')
@router.callback_query(F.data == 'pz-6-c')
@router.callback_query(F.data == 'pz-6-d')
async def pz_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-6-a': True,
        'pz-6-b': False,
        'pz-6-c': False,
        'pz-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Какой инструмент используется для зачистки поверхности перед нанесением латки?\n\n
a) Шлифовальная машинка с абразивным кругом.\n
b) Плоская отвертка.\n
c) Кисточка.\n
d) Нож.''',
                                      reply_markup=inline_keyboards.pz_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-7-a')
@router.callback_query(F.data == 'pz-7-b')
@router.callback_query(F.data == 'pz-7-c')
@router.callback_query(F.data == 'pz-7-d')
async def pz_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-7-a': True,
        'pz-7-b': False,
        'pz-7-c': False,
        'pz-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Почему важно удалить все "ребрышки" на поверхности шины перед нанесением латки?\n\n
a) Чтобы улучшить балансировку.\n
b) Чтобы уменьшить вес шины.\n
c) Чтобы латка прилипла ровно.\n
d) Чтобы не повредить герметик.''',
                                      reply_markup=inline_keyboards.pz_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-8-a')
@router.callback_query(F.data == 'pz-8-b')
@router.callback_query(F.data == 'pz-8-c')
@router.callback_query(F.data == 'pz-8-d')
async def pz_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-8-a': False,
        'pz-8-b': False,
        'pz-8-c': True,
        'pz-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Сколько слоев клея-активатора наносится на шину перед установкой латки?\n\n
a) Один.\n
b) Два.\n
c) Три.\n
d) Четыре.''',
                                      reply_markup=inline_keyboards.pz_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-9-a')
@router.callback_query(F.data == 'pz-9-b')
@router.callback_query(F.data == 'pz-9-c')
@router.callback_query(F.data == 'pz-9-d')
async def pz_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-9-a': False,
        'pz-9-b': True,
        'pz-9-c': False,
        'pz-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Как проверяется готовность клея перед установкой латки?\n\n
a) Он должен потемнеть.\n
b) Он должен начать пузыриться.\n
c) Он должен стать липким.\n
d) Он должен стать матовым.''',
                                      reply_markup=inline_keyboards.pz_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-10-a')
@router.callback_query(F.data == 'pz-10-b')
@router.callback_query(F.data == 'pz-10-c')
@router.callback_query(F.data == 'pz-10-d')
async def pz_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-10-a': False,
        'pz-10-b': False,
        'pz-10-c': False,
        'pz-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Как правильно разместить латку на шине?\n\n
a) Любой стороной.\n
b) По центру пореза без учета направления.\n
c) Стрелкой к борту.\n
d) Стороной с пленкой вниз.''',
                                      reply_markup=inline_keyboards.pz_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pz-11-a')
@router.callback_query(F.data == 'pz-11-b')
@router.callback_query(F.data == 'pz-11-c')
@router.callback_query(F.data == 'pz-11-d')
async def pz_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-11-a': False,
        'pz-11-b': False,
        'pz-11-c': True,
        'pz-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Стороной с пленкой вниз?\n\n
a) Герметиком.\n
b) Густым клеем.\n
c) Растворителем.\n
d) Мелом.''',
                                      reply_markup=inline_keyboards.pz_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-12-a')
@router.callback_query(F.data == 'pz-12-b')
@router.callback_query(F.data == 'pz-12-c')
@router.callback_query(F.data == 'pz-12-d')
async def pz_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-12-a': True,
        'pz-12-b': False,
        'pz-12-c': False,
        'pz-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Почему важно обработать края латки герметиком?\n\n
а) Для улучшения сцепления.\n
b) Чтобы исключить попадание конденсата.\n
c) Для увеличения срока службы шины.\n
d) Для дополнительной прочности.''',
                                      reply_markup=inline_keyboards.pz_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-13-a')
@router.callback_query(F.data == 'pz-13-b')
@router.callback_query(F.data == 'pz-13-c')
@router.callback_query(F.data == 'pz-13-d')
async def pz_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-13-a': False,
        'pz-13-b': True,
        'pz-13-c': False,
        'pz-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Как завершается процесс ремонта колеса?\n\n
a) Установка балансировочных грузов.\n
b) Нанесение третьего слоя клея.\n
c) Установка шины на автомобиль.\n
d) Контрольная проверка герметичности шины.''',
                                      reply_markup=inline_keyboards.pz_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-14-a')
@router.callback_query(F.data == 'pz-14-b')
@router.callback_query(F.data == 'pz-14-c')
@router.callback_query(F.data == 'pz-14-d')
async def pz_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-14-a': False,
        'pz-14-b': False,
        'pz-14-c': False,
        'pz-14-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Каким способом вы проверяете герметичность шины после ремонта?\n\n
a) Контрольным проливом.\n
b) Сдавливанием руками.\n
c) Нагреванием шины.\n
d) Визуальным осмотром.''',
                                      reply_markup=inline_keyboards.pz_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-15-a')
@router.callback_query(F.data == 'pz-15-b')
@router.callback_query(F.data == 'pz-15-c')
@router.callback_query(F.data == 'pz-15-d')
async def pz_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-15-a': True,
        'pz-15-b': False,
        'pz-15-c': False,
        'pz-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Что говорит о том, что шина готова к передаче клиенту?\n\n
a) Латка блестит.\n
b) Латка прочно приклеена, шина герметична.\n
c) Шина выглядит новой.\n
d) Латка полностью скрыта краской.''',
                                      reply_markup=inline_keyboards.pz_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-16-a')
@router.callback_query(F.data == 'pz-16-b')
@router.callback_query(F.data == 'pz-16-c')
@router.callback_query(F.data == 'pz-16-d')
async def pz_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-16-a': False,
        'pz-16-b': True,
        'pz-16-c': False,
        'pz-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Какой минимальный запас используется при обводке латки мелом перед зачисткой?\n\n
a) 1 мм.\n
b) 3–5 мм.\n
c) 10 мм.\n
d) Без запаса.''',
                                      reply_markup=inline_keyboards.pz_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-17-a')
@router.callback_query(F.data == 'pz-17-b')
@router.callback_query(F.data == 'pz-17-c')
@router.callback_query(F.data == 'pz-17-d')
async def pz_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-17-a': False,
        'pz-17-b': True,
        'pz-17-c': False,
        'pz-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Почему важно использовать ровный слой клея при нанесении?\n\n
a) Для ускорения высыхания.\n
b) Чтобы избежать избыточной толщины.\n
c) Чтобы не повредить латочный материал.\n
d) Для экономии клея.''',
                                      reply_markup=inline_keyboards.pz_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-18-a')
@router.callback_query(F.data == 'pz-18-b')
@router.callback_query(F.data == 'pz-18-c')
@router.callback_query(F.data == 'pz-18-d')
async def pz_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-18-a': False,
        'pz-18-b': True,
        'pz-18-c': False,
        'pz-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Что нужно сделать перед приклеиванием латки?\n\n
a) Сжать шину руками.\n
b) Проверить толщину резины.\n
c) Убедиться, что поверхность чистая и обезжиренная.\n
d) Установить балансировочные грузы.''',
                                      reply_markup=inline_keyboards.pz_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-19-a')
@router.callback_query(F.data == 'pz-19-b')
@router.callback_query(F.data == 'pz-19-c')
@router.callback_query(F.data == 'pz-19-d')
async def pz_19_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-19-a': False,
        'pz-19-b': False,
        'pz-19-c': True,
        'pz-19-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''20. Какую функцию выполняет прикатка после установки латки?\n
a) Создает ровный слой герметика.\n
b) Проверяет равномерность нанесения клея.\n
c) Убирает воздух из-под латки.\n
d) Формирует дополнительные слои корда.''',
                                      reply_markup=inline_keyboards.pz_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pz-20-a')
@router.callback_query(F.data == 'pz-20-b')
@router.callback_query(F.data == 'pz-20-c')
@router.callback_query(F.data == 'pz-20-d')
async def pz_20_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pz-20-a': False,
        'pz-20-b': False,
        'pz-20-c': True,
        'pz-20-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 20:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 20:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='pz_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 21

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/20.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.snyatie_i_ustanovka()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/20.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.porez_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_pz_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_pz(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_sn_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='sn_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по cнятию и установке колеса на атомобиль!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Где чаще всего хранят секретку для колеса?\n\n
a) В бардачке.\n
b) В багажнике.\n
c) Под локотником.\n
d) Под капотом.''',
                                      reply_markup=inline_keyboards.sn_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'sn-1-a')
@router.callback_query(F.data == 'sn-1-b')
@router.callback_query(F.data == 'sn-1-c')
@router.callback_query(F.data == 'sn-1-d')
async def sn_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-1-a': False,
        'sn-1-b': True,
        'sn-1-c': False,
        'sn-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какой инструмент чаще всего используется для снятия сильно затянутых гаек?\n\n
a) Крестовой ключ.\n
b) Головка в виде «ромашки».\n
c) Вороток с головкой.\n
d) Газовый ключ.''',
                                      reply_markup=inline_keyboards.sn_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-2-a')
@router.callback_query(F.data == 'sn-2-b')
@router.callback_query(F.data == 'sn-2-c')
@router.callback_query(F.data == 'sn-2-d')
async def sn_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-2-a': False,
        'sn-2-b': False,
        'sn-2-c': True,
        'sn-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Что нужно сделать перед использованием домкрата на автомобиле с пневматической подвеской?\n\n
a) Осмотреть колесо на наличие повреждений.\n
b) Заблокировать подвеску на программном уровне.\n
c) Проверить давление в шинах.\n
d) Снять секретку.''',
                                      reply_markup=inline_keyboards.sn_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-3-a')
@router.callback_query(F.data == 'sn-3-b')
@router.callback_query(F.data == 'sn-3-c')
@router.callback_query(F.data == 'sn-3-d')
async def sn_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-3-a': False,
        'sn-3-b': True,
        'sn-3-c': False,
        'sn-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Какое действие выполняется первым при снятии колеса?\n\n
a) Ослабить гайки.\n
b) Установить домкрат.\n
c) Поднять автомобиль.\n
d) Снять защитный колпак.''',
                               reply_markup=inline_keyboards.sn_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'sn-4-a')
@router.callback_query(F.data == 'sn-4-b')
@router.callback_query(F.data == 'sn-4-c')
@router.callback_query(F.data == 'sn-4-d')
async def sn_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-4-a': True,
        'sn-4-b': False,
        'sn-4-c': False,
        'sn-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Что можно использовать для предотвращения повреждения порога автомобиля при подъеме домкратом?\n\n
a) Картон.\n
b) Резинку от протектора.\n
c) Металлический лист.\n
d) Тряпку.''',
                                      reply_markup=inline_keyboards.sn_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-5-a')
@router.callback_query(F.data == 'sn-5-b')
@router.callback_query(F.data == 'sn-5-c')
@router.callback_query(F.data == 'sn-5-d')
async def sn_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-5-a': False,
        'sn-5-b': True,
        'sn-5-c': False,
        'sn-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Как откручивается сорванная секретка?\n\n
a) Используется головка в виде «ромашки», которая набивается на гайку (Экстрактор).\n
b) Применяется крестовой ключ.\n
c) Используется стандартный вороток.\n
d) Откручивается руками.''',
                                      reply_markup=inline_keyboards.pz_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'sn-6-a')
@router.callback_query(F.data == 'sn-6-b')
@router.callback_query(F.data == 'sn-6-c')
@router.callback_query(F.data == 'sn-6-d')
async def sn_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-6-a': True,
        'sn-6-b': False,
        'sn-6-c': False,
        'sn-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. В каком порядке затягиваются гайки на колесе?\n\n
a) В порядке «крест на крест».\n
b) По часовой стрелке.\n
c) Против часовой стрелки.\n
d) Секретка первая, остальные по кругу.''',
                                      reply_markup=inline_keyboards.sn_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-7-a')
@router.callback_query(F.data == 'sn-7-b')
@router.callback_query(F.data == 'sn-7-c')
@router.callback_query(F.data == 'sn-7-d')
async def sn_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-7-a': True,
        'sn-7-b': False,
        'sn-7-c': False,
        'sn-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Где чаще всего располагается поддомкратник?\n\n
a) На раме автомобиля.\n
b) На днище автомобиля.\n
c) На пороге автомобиля, обозначен вырезом.\n
d) На ступице колеса.''',
                                      reply_markup=inline_keyboards.sn_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-8-a')
@router.callback_query(F.data == 'sn-8-b')
@router.callback_query(F.data == 'sn-8-c')
@router.callback_query(F.data == 'sn-8-d')
async def sn_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-8-a': False,
        'sn-8-b': False,
        'sn-8-c': True,
        'sn-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Для чего используется динамометрический ключ при установке колеса?\n\n
a) Для выравнивания колеса.\n
b) Для проверки момента затяжки гаек.\n
c) Для установки секретки.\n
d) Для подъема домкрата.''',
                                      reply_markup=inline_keyboards.sn_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-9-a')
@router.callback_query(F.data == 'sn-9-b')
@router.callback_query(F.data == 'sn-9-c')
@router.callback_query(F.data == 'sn-9-d')
async def sn_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-9-a': False,
        'sn-9-b': True,
        'sn-9-c': False,
        'sn-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Почему важно проверять проставочную резинку домкрата после того, как сняли автомобиль с домкрата?\n\n
a) Чтобы проверить, не порвалась ли резинка.\n
b) Чтобы убедиться, что домкрат работает исправно.\n
c) Чтобы избежать повреждения домкрата.\n
d) Чтобы убедиться, что резинка не осталась прилипшей к порогу автомобиля.''',
                                      reply_markup=inline_keyboards.sn_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-10-a')
@router.callback_query(F.data == 'sn-10-b')
@router.callback_query(F.data == 'sn-10-c')
@router.callback_query(F.data == 'sn-10-d')
async def sn_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-10-a': False,
        'sn-10-b': False,
        'sn-10-c': False,
        'sn-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Как правильно обработать ступицу перед установкой колеса?\n\n
a) Покрасить ступицу для защиты от коррозии.\n
b) Протереть сухой тканью.\n
c) Очистить грязь и нанести медную смазку на шпильки.\n
d) Сбрызнуть WD-40.''',
                                      reply_markup=inline_keyboards.sn_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'sn-11-a')
@router.callback_query(F.data == 'sn-11-b')
@router.callback_query(F.data == 'sn-11-c')
@router.callback_query(F.data == 'sn-11-d')
async def sn_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-11-a': False,
        'sn-11-b': False,
        'sn-11-c': True,
        'sn-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Какие гайки закручиваются последними при установке колеса?\n\n
a) Секретка.\n
b) Первая гайка по порядку.\n
c) Самая тугая гайка.\n
d) Любая произвольно.''',
                                      reply_markup=inline_keyboards.sn_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-12-a')
@router.callback_query(F.data == 'sn-12-b')
@router.callback_query(F.data == 'sn-12-c')
@router.callback_query(F.data == 'sn-12-d')
async def sn_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-12-a': True,
        'sn-12-b': False,
        'sn-12-c': False,
        'sn-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Как правильно установить домкрат, если поддомкратник отсутствует?\n\n
а) Под любую часть порога.\n
b) Под жесткую часть кузова, раму или лонжерон.\n
c) Под подвеску.\n
d) Под днище автомобиля.''',
                                      reply_markup=inline_keyboards.sn_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-13-a')
@router.callback_query(F.data == 'sn-13-b')
@router.callback_query(F.data == 'sn-13-c')
@router.callback_query(F.data == 'sn-13-d')
async def sn_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-13-a': False,
        'sn-13-b': True,
        'sn-13-c': False,
        'sn-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Как понять, что колесный диск предназначен для задней оси?\n\n
a) Диск окрашен в другой цвет.\n
b) На диске указана буква Z.\n
c) У диска более глубокий рисунок.\n
d) Ширина диска больше.''',
                                      reply_markup=inline_keyboards.sn_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-14-a')
@router.callback_query(F.data == 'sn-14-b')
@router.callback_query(F.data == 'sn-14-c')
@router.callback_query(F.data == 'sn-14-d')
async def sn_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-14-a': False,
        'sn-14-b': False,
        'sn-14-c': False,
        'sn-14-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Что делать перед установкой нового колеса на ступицу?\n\n
a) Очистить ступицу от грязи металлической щеткой.\n
b) Убедиться в наличии смазки на гайках.\n
c) Проверить давление в шинах.\n
d) Повернуть ступицу для проверки подшипников.''',
                                      reply_markup=inline_keyboards.sn_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-15-a')
@router.callback_query(F.data == 'sn-15-b')
@router.callback_query(F.data == 'sn-15-c')
@router.callback_query(F.data == 'sn-15-d')
async def sn_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-15-a': True,
        'sn-15-b': False,
        'sn-15-c': False,
        'sn-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Для чего используется проставочное кольцо при установке дисков?\n\n
a) Для защиты резины.\n
b) Для центровки диска на ступице.\n
c) Для украшения.\n
d) Для усиления крепления.''',
                                      reply_markup=inline_keyboards.sn_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-16-a')
@router.callback_query(F.data == 'sn-16-b')
@router.callback_query(F.data == 'sn-16-c')
@router.callback_query(F.data == 'sn-16-d')
async def sn_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-16-a': False,
        'sn-16-b': True,
        'sn-16-c': False,
        'sn-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Почему важно затягивать гайки в порядке «крест на крест»?\n\n
a) Чтобы гайки не закисли.\n
b) Чтобы равномерно распределить нагрузку.\n
c) Чтобы колеса не открутились.\n
d) Чтобы ускорить процесс.''',
                                      reply_markup=inline_keyboards.sn_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-17-a')
@router.callback_query(F.data == 'sn-17-b')
@router.callback_query(F.data == 'sn-17-c')
@router.callback_query(F.data == 'sn-17-d')
async def sn_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-17-a': False,
        'sn-17-b': True,
        'sn-17-c': False,
        'sn-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Какое значение момента затяжки чаще всего используется для колесных гаек?\n\n
a) 90-100 Нм.\n
b) 110-120 Нм.\n
c) 130-140 Нм.\n
d) 150-160 Нм.''',
                                      reply_markup=inline_keyboards.sn_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-18-a')
@router.callback_query(F.data == 'sn-18-b')
@router.callback_query(F.data == 'sn-18-c')
@router.callback_query(F.data == 'sn-18-d')
async def sn_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-18-a': False,
        'sn-18-b': True,
        'sn-18-c': False,
        'sn-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Как избежать потери гаек при их снятии?\n\n
a) Складывать их на землю.\n
b) Класть гайки в карман.\n
c) Хранить гайки в специальной магнитной тарелочке.\n
d) Оставить их на колесе.''',
                                      reply_markup=inline_keyboards.sn_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-19-a')
@router.callback_query(F.data == 'sn-19-b')
@router.callback_query(F.data == 'sn-19-c')
@router.callback_query(F.data == 'sn-19-d')
async def sn_19_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-19-a': False,
        'sn-19-b': False,
        'sn-19-c': True,
        'sn-19-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''20. Почему важно очищать колесо от грязи и снега перед балансировкой?\n
a) Чтобы ускорить процесс балансировки.\n
b) Чтобы уменьшить износ оборудования.\n
c) Чтобы обеспечить точность балансировки.\n
d) Чтобы защитить станок от поломки.''',
                                      reply_markup=inline_keyboards.sn_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sn-20-a')
@router.callback_query(F.data == 'sn-20-b')
@router.callback_query(F.data == 'sn-20-c')
@router.callback_query(F.data == 'sn-20-d')
async def sn_20_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sn-20-a': False,
        'sn-20-b': False,
        'sn-20-c': True,
        'sn-20-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 20:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 20:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='sn_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 21

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/20.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.remont_kolesa()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/20.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.snyatie_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_sn_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_sn(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_sb_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='sb_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по сборке и разборке на шиномонтажном станке!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Чем помечают колеса перед разборкой?\n\n
a) Маркером.\n
b) Желтым восковым мелом.\n
c) Краской.\n
d) Шариковой ручкой.''',
                                      reply_markup=inline_keyboards.sb_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'sb-1-a')
@router.callback_query(F.data == 'sb-1-b')
@router.callback_query(F.data == 'sb-1-c')
@router.callback_query(F.data == 'sb-1-d')
async def sb_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-1-a': False,
        'sb-1-b': True,
        'sb-1-c': False,
        'sb-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какие буквы пишутся на колесе для обозначения его положения?\n\n
a) ВП, ЗЛ.\n
b) ПП, ЗВ.\n
c) ПЛ (передняя левая), ЗЛ (задняя левая), ПП (передняя правая), ЗП (задняя правая).\n
d) ВЛ, ЗП.''',
                                      reply_markup=inline_keyboards.sb_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-2-a')
@router.callback_query(F.data == 'sb-2-b')
@router.callback_query(F.data == 'sb-2-c')
@router.callback_query(F.data == 'sb-2-d')
async def sb_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-2-a': False,
        'sb-2-b': False,
        'sb-2-c': True,
        'sb-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Где нужно располагать вентиль перед разборкой колеса?\n\n
a) Ближе к диску.\n
b) Перпендикулярно полу или у ноги.\n
c) На уровне монтажной лапы.\n
d) Под углом 45 градусов.''',
                                      reply_markup=inline_keyboards.sb_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-3-a')
@router.callback_query(F.data == 'sb-3-b')
@router.callback_query(F.data == 'sb-3-c')
@router.callback_query(F.data == 'sb-3-d')
async def sb_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-3-a': False,
        'sb-3-b': True,
        'sb-3-c': False,
        'sb-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Что делают первым при разборке колеса?\n\n
a) Откручивают колпачок и выкручивают золотник.\n
b) Снимают диск.\n
c) Проверяют давление.\n
d) Откручивают болты.''',
                               reply_markup=inline_keyboards.sb_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'sb-4-a')
@router.callback_query(F.data == 'sb-4-b')
@router.callback_query(F.data == 'sb-4-c')
@router.callback_query(F.data == 'sb-4-d')
async def sb_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-4-a': True,
        'sb-4-b': False,
        'sb-4-c': False,
        'sb-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Какой инструмент используется для отжатия борта шины?\n\n
a) Монтировка.\n
b) Бортоотжим.\n
c) Под углом 90 градусов.\n
d) В центре колеса.''',
                                      reply_markup=inline_keyboards.sb_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-5-a')
@router.callback_query(F.data == 'sb-5-b')
@router.callback_query(F.data == 'sb-5-c')
@router.callback_query(F.data == 'sb-5-d')
async def sb_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-5-a': False,
        'sb-5-b': True,
        'sb-5-c': False,
        'sb-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какой метод используется для предотвращения повреждения диска?\n\n
a) Использование защитных накладок.\n
b) Установка дополнительного борта.\n
c) Применение смазки.\n
d) Нагревание диска.''',
                                      reply_markup=inline_keyboards.sb_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'sb-6-a')
@router.callback_query(F.data == 'sb-6-b')
@router.callback_query(F.data == 'sb-6-c')
@router.callback_query(F.data == 'sb-6-d')
async def sb_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-6-a': True,
        'sb-6-b': False,
        'sb-6-c': False,
        'sb-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Что делать, если метка съехала при сборке?\n\n
a) Проворачивать колесо относительно диска.\n
b) Оставить как есть.\n
c) Добавить еще пасты.\n
d) Установить новую метку.''',
                                      reply_markup=inline_keyboards.sb_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-7-a')
@router.callback_query(F.data == 'sb-7-b')
@router.callback_query(F.data == 'sb-7-c')
@router.callback_query(F.data == 'sb-7-d')
async def sb_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-7-a': True,
        'sb-7-b': False,
        'sb-7-c': False,
        'sb-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Почему шину накачивают без золотника?\n\n
a) Для увеличения давления.\n
b) Чтобы проверить герметичность.\n
c) Чтобы она просела на место.\n
d) Для удобства балансировки.''',
                                      reply_markup=inline_keyboards.sb_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-8-a')
@router.callback_query(F.data == 'sb-8-b')
@router.callback_query(F.data == 'sb-8-c')
@router.callback_query(F.data == 'sb-8-d')
async def sb_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-8-a': False,
        'sb-8-b': False,
        'sb-8-c': True,
        'sb-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Что такое "хамп-зона"?\n\n
a) Место для установки вентиля.\n
b) Замок бескамерного диска.\n
c) Зона балансировки.\n
d) Усиленная часть протектора.''',
                                      reply_markup=inline_keyboards.sb_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-9-a')
@router.callback_query(F.data == 'sb-9-b')
@router.callback_query(F.data == 'sb-9-c')
@router.callback_query(F.data == 'sb-9-d')
async def sb_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-9-a': False,
        'sb-9-b': True,
        'sb-9-c': False,
        'sb-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Какое давление накачивают перед установкой золотника?\n\n
a) 1 атм.\n
b) 2 атм.\n
c) 2,5 атм.\n
d) 3,5 атм.''',
                                      reply_markup=inline_keyboards.sb_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-10-a')
@router.callback_query(F.data == 'sb-10-b')
@router.callback_query(F.data == 'sb-10-c')
@router.callback_query(F.data == 'sb-10-d')
async def sb_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-10-a': False,
        'sb-10-b': False,
        'sb-10-c': False,
        'sb-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Для чего используется дополнительная монтировка при работе с RunFlat?\n\n
a) Для смазки диска.\n
b) Для балансировки.\n
c) Для натяжения шины.\n
d) Для фиксации вентиля.''',
                                      reply_markup=inline_keyboards.sb_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'sb-11-a')
@router.callback_query(F.data == 'sb-11-b')
@router.callback_query(F.data == 'sb-11-c')
@router.callback_query(F.data == 'sb-11-d')
async def sb_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-11-a': False,
        'sb-11-b': False,
        'sb-11-c': True,
        'sb-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Какой метод сборки колес RunFlat описан в видео?\n\n
a) Две монтировки или использование доплапы.\n
b) Три монтировки.\n
c) Один монтажный ключ.\n
d) Балансировочный станок.''',
                                      reply_markup=inline_keyboards.sb_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-12-a')
@router.callback_query(F.data == 'sb-12-b')
@router.callback_query(F.data == 'sb-12-c')
@router.callback_query(F.data == 'sb-12-d')
async def sb_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-12-a': True,
        'sb-12-b': False,
        'sb-12-c': False,
        'sb-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Как предотвратить повреждение датчика давления при сборке?\n\n
а) Установить его под углом.\n
b) Разместить напротив монтажной лапы.\n
c) Использовать дополнительную монтировку.\n
d) Смазать датчик.''',
                                      reply_markup=inline_keyboards.sb_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-13-a')
@router.callback_query(F.data == 'sb-13-b')
@router.callback_query(F.data == 'sb-13-c')
@router.callback_query(F.data == 'sb-13-d')
async def sb_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-13-a': False,
        'sb-13-b': True,
        'sb-13-c': False,
        'sb-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Какие основные метки могут быть на шине?\n\n
a) ВЕНТИЛЬ, ЛАПА.\n
b) FRONT, BACK.\n
c) LEFT, RIGHT.\n
d) INSIDE, OUTSIDE, ROTATION.''',
                                      reply_markup=inline_keyboards.sb_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-14-a')
@router.callback_query(F.data == 'sb-14-b')
@router.callback_query(F.data == 'sb-14-c')
@router.callback_query(F.data == 'sb-14-d')
async def sb_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-14-a': False,
        'sb-14-b': False,
        'sb-14-c': False,
        'sb-14-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Почему важно смазывать борта шины монтажной пастой перед сборкой?\n\n
a) Для облегчения процесса монтажа/демонтажа.\n
b) Чтобы сохранить метки.\n
c) Для балансировки.\n
d) Чтобы уменьшить износ диска.''',
                                      reply_markup=inline_keyboards.sb_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-15-a')
@router.callback_query(F.data == 'sb-15-b')
@router.callback_query(F.data == 'sb-15-c')
@router.callback_query(F.data == 'sb-15-d')
async def sb_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-15-a': True,
        'sb-15-b': False,
        'sb-15-c': False,
        'sb-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Какой инструмент используется для отжатия борта шины?\n\n
a) Монтировка.\n
b) Бортоотжим.\n
c) Балансировочный станок.\n
d) Тиски.''',
                                      reply_markup=inline_keyboards.sb_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-16-a')
@router.callback_query(F.data == 'sb-16-b')
@router.callback_query(F.data == 'sb-16-c')
@router.callback_query(F.data == 'sb-16-d')
async def sb_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-16-a': False,
        'sb-16-b': True,
        'sb-16-c': False,
        'sb-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Как установить монтажную лапу на станке?\n\n
a) На уровне протектора.\n
b) С минимальным расстоянием от диска, чтобы при вращении не касалась диска.\n
c) У вентиля.\n
d) В центре колеса.''',
                                      reply_markup=inline_keyboards.sb_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-17-a')
@router.callback_query(F.data == 'sb-17-b')
@router.callback_query(F.data == 'sb-17-c')
@router.callback_query(F.data == 'sb-17-d')
async def sb_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-17-a': False,
        'sb-17-b': True,
        'sb-17-c': False,
        'sb-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Что нужно сделать перед сборкой колеса?\n\n
a) Протереть диск.\n
b) Смазать монтажной пастой.\n
c) Проверить давление.\n
d) Установить монтировку.''',
                                      reply_markup=inline_keyboards.sb_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-18-a')
@router.callback_query(F.data == 'sb-18-b')
@router.callback_query(F.data == 'sb-18-c')
@router.callback_query(F.data == 'sb-18-d')
async def sb_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-18-a': False,
        'sb-18-b': True,
        'sb-18-c': False,
        'sb-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Что показывает метка "INSIDE" на шине?\n\n
a) Направление движения.\n
b) Внутреннюю сторону шины.\n
c) Давление воздуха.\n
d) Место установки вентиля.''',
                                      reply_markup=inline_keyboards.sb_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-19-a')
@router.callback_query(F.data == 'sb-19-b')
@router.callback_query(F.data == 'sb-19-c')
@router.callback_query(F.data == 'sb-19-d')
async def sb_19_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-19-a': False,
        'sb-19-b': False,
        'sb-19-c': True,
        'sb-19-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''20. Какую сторону шины надевают первой при сборке?\n
a) Верхнюю.\n
b) Наружную.\n
c) Внутреннюю.\n
d) Любую.''',
                                      reply_markup=inline_keyboards.sb_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sb-20-a')
@router.callback_query(F.data == 'sb-20-b')
@router.callback_query(F.data == 'sb-20-c')
@router.callback_query(F.data == 'sb-20-d')
async def sb_20_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sb-20-a': False,
        'sb-20-b': False,
        'sb-20-c': True,
        'sb-20-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 20:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 20:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='sb_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 21

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/20.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.beskamernogo_kolesa()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/20.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.sborkakol_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_sb_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_sb(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_rn_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='rn_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по ремонту прокола бескамерного колеса!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что делается в первую очередь при ремонте прокола бескамерного колеса?\n\n
a) Снимается саморез.\n
b) Осматривается колесо на наличие инородных предметов.\n
c) Проверяется состояние вентиля.\n
d) Зачищается место прокола.''',
                                      reply_markup=inline_keyboards.rn_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'rn-1-a')
@router.callback_query(F.data == 'rn-1-b')
@router.callback_query(F.data == 'rn-1-c')
@router.callback_query(F.data == 'rn-1-d')
async def rn_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-1-a': False,
        'rn-1-b': True,
        'rn-1-c': False,
        'rn-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Чем помечается место нахождения самореза?\n\n
a) Латкой.\n
b) Маркером.\n
c) Мелом.\n
d) Ножом.''',
                                      reply_markup=inline_keyboards.rn_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-2-a')
@router.callback_query(F.data == 'rn-2-b')
@router.callback_query(F.data == 'rn-2-c')
@router.callback_query(F.data == 'rn-2-d')
async def rn_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-2-a': False,
        'rn-2-b': False,
        'rn-2-c': True,
        'rn-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Почему важно пометить место вентиля?\n\n
a) Для проверки прокола.\n
b) Чтобы сохранить оптимизацию после сборки.\n
c) Для удобства очистки.\n
d) Для фиксации латки.''',
                                      reply_markup=inline_keyboards.rn_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-3-a')
@router.callback_query(F.data == 'rn-3-b')
@router.callback_query(F.data == 'rn-3-c')
@router.callback_query(F.data == 'rn-3-d')
async def rn_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-3-a': False,
        'rn-3-b': True,
        'rn-3-c': False,
        'rn-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Что делается перед снятием самореза?\n\n
a) Колесо проверяется изнутри.\n
b) Колесо очищается.\n
c) Проклеивается латка.\n
d) Подбирается инструмент.''',
                               reply_markup=inline_keyboards.rn_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'rn-4-a')
@router.callback_query(F.data == 'rn-4-b')
@router.callback_query(F.data == 'rn-4-c')
@router.callback_query(F.data == 'rn-4-d')
async def rn_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-4-a': True,
        'rn-4-b': False,
        'rn-4-c': False,
        'rn-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Чем рекомендуется вытаскивать саморез?\n\n
a) Отверткой.\n
b) Кусачками.\n
c) Плоскогубцами.\n
d) Ручным скребком.''',
                                      reply_markup=inline_keyboards.rn_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-5-a')
@router.callback_query(F.data == 'rn-5-b')
@router.callback_query(F.data == 'rn-5-c')
@router.callback_query(F.data == 'rn-5-d')
async def rn_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-5-a': False,
        'rn-5-b': True,
        'rn-5-c': False,
        'rn-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Как называется инструмент для зачистки места прокола?\n\n
a) Камень для зачистки.\n
b) Ролик.\n
c) Шкребок.\n
d) Лабу.''',
                                      reply_markup=inline_keyboards.rn_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'rn-6-a')
@router.callback_query(F.data == 'rn-6-b')
@router.callback_query(F.data == 'rn-6-c')
@router.callback_query(F.data == 'rn-6-d')
async def rn_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-6-a': True,
        'rn-6-b': False,
        'rn-6-c': False,
        'rn-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Сколько времени требуется для высыхания бескамерного клея?\n\n
a) 1-2 минуты.\n
b) 3-5 минут.\n
c) 10 минут.\n
d) Клей сохнет мгновенно.''',
                                      reply_markup=inline_keyboards.rn_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-7-a')
@router.callback_query(F.data == 'rn-7-b')
@router.callback_query(F.data == 'rn-7-c')
@router.callback_query(F.data == 'rn-7-d')
async def rn_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-7-a': False,
        'rn-7-b': True,
        'rn-7-c': False,
        'rn-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Как определить, что клей высох?\n\n
a) Клей становится прозрачным.\n
b) Латка не прилипает к пальцу.\n
c) Палец еле прилипает к клею.\n
d) На клее образуется корка.''',
                                      reply_markup=inline_keyboards.rn_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-8-a')
@router.callback_query(F.data == 'rn-8-b')
@router.callback_query(F.data == 'rn-8-c')
@router.callback_query(F.data == 'rn-8-d')
async def rn_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-8-a': False,
        'rn-8-b': False,
        'rn-8-c': True,
        'rn-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Когда снимается защитная фольга с латки?\n\n
a) Ее нужно разрезать ножом.\n
b) Она снимается перед приклеиванием.\n
c) После прокатки роликом.\n
d) Защитная фольга не снимается.''',
                                      reply_markup=inline_keyboards.rn_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-9-a')
@router.callback_query(F.data == 'rn-9-b')
@router.callback_query(F.data == 'rn-9-c')
@router.callback_query(F.data == 'rn-9-d')
async def rn_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-9-a': False,
        'rn-9-b': True,
        'rn-9-c': False,
        'rn-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Чем приклеивается латка к месту прокола?\n\n
a) Клеем.\n
b) Обычным клеем.\n
c) Герметиком.\n
d) Бескамерным клеем.''',
                                      reply_markup=inline_keyboards.rn_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-10-a')
@router.callback_query(F.data == 'rn-10-b')
@router.callback_query(F.data == 'rn-10-c')
@router.callback_query(F.data == 'rn-10-d')
async def rn_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-10-a': False,
        'rn-10-b': False,
        'rn-10-c': False,
        'rn-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Как прокатывается латка после приклеивания?\n\n
a) Сначала вдоль, потом поперек.\n
b) В произвольном направлении.\n
c) От центра к краям.\n
d) Только по краям.''',
                                      reply_markup=inline_keyboards.rn_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'rn-11-a')
@router.callback_query(F.data == 'rn-11-b')
@router.callback_query(F.data == 'rn-11-c')
@router.callback_query(F.data == 'rn-11-d')
async def rn_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-11-a': False,
        'rn-11-b': False,
        'rn-11-c': True,
        'rn-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Для чего снимается защитная пленка с латки?\n\n
a) Для прокатки края.\n
b) Чтобы проверить качество клея.\n
c) Для проверки на герметичность.\n
d) Для крепления на диск.''',
                                      reply_markup=inline_keyboards.rn_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-12-a')
@router.callback_query(F.data == 'rn-12-b')
@router.callback_query(F.data == 'rn-12-c')
@router.callback_query(F.data == 'rn-12-d')
async def rn_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-12-a': True,
        'rn-12-b': False,
        'rn-12-c': False,
        'rn-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Как называется слой, который восстанавливается при сложном ремонте?\n\n
а) Протектор.\n
b) Innerliner.\n
c) Лабу.\n
d) Камень для зачистки.''',
                                      reply_markup=inline_keyboards.rn_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-13-a')
@router.callback_query(F.data == 'rn-13-b')
@router.callback_query(F.data == 'rn-13-c')
@router.callback_query(F.data == 'rn-13-d')
async def rn_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-13-a': False,
        'rn-13-b': True,
        'rn-13-c': False,
        'rn-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Как осматривается колесо изнутри?\n\n
a) Визуально.\n
b) Камнем для зачистки.\n
c) Роликом.\n
d) Рукой в перчатке.''',
                                      reply_markup=inline_keyboards.rn_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-14-a')
@router.callback_query(F.data == 'rn-14-b')
@router.callback_query(F.data == 'rn-14-c')
@router.callback_query(F.data == 'rn-14-d')
async def rn_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-14-a': False,
        'rn-14-b': False,
        'rn-14-c': False,
        'rn-14-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Какой инструмент применяется для зачистки в более сложных случаях?\n\n
a) Шкребок.\n
b) Ролик.\n
c) Отвертка.\n
d) Ладка.''',
                                      reply_markup=inline_keyboards.rn_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-15-a')
@router.callback_query(F.data == 'rn-15-b')
@router.callback_query(F.data == 'rn-15-c')
@router.callback_query(F.data == 'rn-15-d')
async def rn_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-15-a': True,
        'rn-15-b': False,
        'rn-15-c': False,
        'rn-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Какой размер ладки упоминается в тексте?\n\n
a) OP1 или OP2.\n
b) OP3 или OP4.\n
c) OP5 или OP6.\n
d) OP7 или OP8.''',
                                      reply_markup=inline_keyboards.rn_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-16-a')
@router.callback_query(F.data == 'rn-16-b')
@router.callback_query(F.data == 'rn-16-c')
@router.callback_query(F.data == 'rn-16-d')
async def rn_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-16-a': False,
        'rn-16-b': True,
        'rn-16-c': False,
        'rn-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Какой метод ремонта демонстрировался в видео?\n\n
a) Самый сложный.\n
b) Самый простой.\n
c) Технологически сложный.\n
d) Экспериментальный.''',
                                      reply_markup=inline_keyboards.rn_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-17-a')
@router.callback_query(F.data == 'rn-17-b')
@router.callback_query(F.data == 'rn-17-c')
@router.callback_query(F.data == 'rn-17-d')
async def rn_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-17-a': False,
        'rn-17-b': True,
        'rn-17-c': False,
        'rn-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Почему простой способ ремонта считается надежным?\n\n
a) Используются дорогие материалы.\n
b) Проверен 18-летним опытом.\n
c) Требует меньше инструментов.\n
d) Применяются дополнительные технологии.''',
                                      reply_markup=inline_keyboards.rn_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-18-a')
@router.callback_query(F.data == 'rn-18-b')
@router.callback_query(F.data == 'rn-18-c')
@router.callback_query(F.data == 'rn-18-d')
async def rn_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-18-a': False,
        'rn-18-b': True,
        'rn-18-c': False,
        'rn-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Чем дополнительно прокатываются края латки?\n\n
a) Камнем.\n
b) Отверткой.\n
c) Роликом.\n
d) Латкой.''',
                                      reply_markup=inline_keyboards.rn_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'rn-19-a')
@router.callback_query(F.data == 'rn-19-b')
@router.callback_query(F.data == 'rn-19-c')
@router.callback_query(F.data == 'rn-19-d')
async def rn_19_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'rn-19-a': False,
        'rn-19-b': False,
        'rn-19-c': True,
        'rn-19-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 19:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 19:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='rn_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 20

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/19.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.remont_kolesa()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/19.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.remont_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_rn_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_rn(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_bc_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='bc_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по балансировки колеса!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что необходимо сделать перед балансировкой колеса?\n\n
a) Помыть колесо.\n
b) Снять старые балансировочные грузы.\n
c) Поставить колесо на автомобиль.\n
d) Оборудовать колесо новым шинами.''',
                                      reply_markup=inline_keyboards.bc_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'bc-1-a')
@router.callback_query(F.data == 'bc-1-b')
@router.callback_query(F.data == 'bc-1-c')
@router.callback_query(F.data == 'bc-1-d')
async def bc_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-1-a': False,
        'bc-1-b': True,
        'bc-1-c': False,
        'bc-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Как снимаются старые балансировочные грузы?\n\n
a) При помощи металлической отвертки.\n
b) Вручную.\n
c) Поддевая пластиковой лопаткой.\n
d) С помощью молотка.''',
                                      reply_markup=inline_keyboards.bc_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-2-a')
@router.callback_query(F.data == 'bc-2-b')
@router.callback_query(F.data == 'bc-2-c')
@router.callback_query(F.data == 'bc-2-d')
async def bc_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-2-a': False,
        'bc-2-b': False,
        'bc-2-c': True,
        'bc-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Каким инструментом удаляются остатки старого скотча?\n\n
a) С помощью металлической щетки.\n
b) При помощи специальной резиновой насадки на дрели.\n
c) Ножом.\n
d) Пластиковой лопаткой.''',
                                      reply_markup=inline_keyboards.bc_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-3-a')
@router.callback_query(F.data == 'bc-3-b')
@router.callback_query(F.data == 'bc-3-c')
@router.callback_query(F.data == 'bc-3-d')
async def bc_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-3-a': False,
        'bc-3-b': True,
        'bc-3-c': False,
        'bc-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Что нужно учитывать при очистке диска?\n\n
a) Не повредить краску.\n
b) Очистить только внутреннюю часть.\n
c) Ничего не очищать.\n
d) Стереть все маркировки на диске.''',
                               reply_markup=inline_keyboards.bc_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'bc-4-a')
@router.callback_query(F.data == 'bc-4-b')
@router.callback_query(F.data == 'bc-4-c')
@router.callback_query(F.data == 'bc-4-d')
async def bc_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-4-a': True,
        'bc-4-b': False,
        'bc-4-c': False,
        'bc-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Где на диске часто указана его ширина?\n\n
a) На внешней части диска.\n
b) На внутренней стороне спицы.\n
c) На упаковке.\n
d) На задней стороне диска.''',
                                      reply_markup=inline_keyboards.bc_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-5-a')
@router.callback_query(F.data == 'bc-5-b')
@router.callback_query(F.data == 'bc-5-c')
@router.callback_query(F.data == 'bc-5-d')
async def bc_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-5-a': False,
        'bc-5-b': True,
        'bc-5-c': False,
        'bc-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какие параметры нужно выставить на балансировочном станке?\n\n
a) Диаметр и ширину диска.\n
b) Скорость вращения колеса.\n
c) Марку автомобиля.\n
d) Тип шины.''',
                                      reply_markup=inline_keyboards.bc_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'bc-6-a')
@router.callback_query(F.data == 'bc-6-b')
@router.callback_query(F.data == 'bc-6-c')
@router.callback_query(F.data == 'bc-6-d')
async def bc_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-6-a': True,
        'bc-6-b': False,
        'bc-6-c': False,
        'bc-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Какой параметр диаметр диска указан в примере?\n\n
a) 15 дюймов.\n
b) 16 дюймов.\n
c) 17 дюймов.\n
d) 18 дюймов.''',
                                      reply_markup=inline_keyboards.bc_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-7-a')
@router.callback_query(F.data == 'bc-7-b')
@router.callback_query(F.data == 'bc-7-c')
@router.callback_query(F.data == 'bc-7-d')
async def bc_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-7-a': False,
        'bc-7-b': False,
        'bc-7-c': True,
        'bc-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какую ширину диска нужно выставить на станке?\n\n
a) 6 дюймов.\n
b) 7,5 дюймов.\n
c) 8 дюймов.\n
d) 7 дюймов.''',
                                      reply_markup=inline_keyboards.bc_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-8-a')
@router.callback_query(F.data == 'bc-8-b')
@router.callback_query(F.data == 'bc-8-c')
@router.callback_query(F.data == 'bc-8-d')
async def bc_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-8-a': False,
        'bc-8-b': True,
        'bc-8-c': False,
        'bc-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Что происходит после выставления параметров на станке?\n\n
a) Станок начинается вращать колесо.\n
b) Станок определяет необходимые грузы для балансировки.\n
c) Станок показывает 0 грамм на обеих сторонах.\n
d) Станок автоматически наклеивает грузы.''',
                                      reply_markup=inline_keyboards.bc_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-9-a')
@router.callback_query(F.data == 'bc-9-b')
@router.callback_query(F.data == 'bc-9-c')
@router.callback_query(F.data == 'bc-9-d')
async def bc_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-9-a': False,
        'bc-9-b': True,
        'bc-9-c': False,
        'bc-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Что такое оптимизация колеса на балансировочном станке?\n\n
a) Процесс наклеивания груза.\n
b) Оборудование с автоматическим подбором груза.\n
c) Применение особых режимов вращения.\n
d) Определение, как повернуть резину относительно диска для минимальных значений балансировки.''',
                                      reply_markup=inline_keyboards.bc_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-10-a')
@router.callback_query(F.data == 'bc-10-b')
@router.callback_query(F.data == 'bc-10-c')
@router.callback_query(F.data == 'bc-10-d')
async def bc_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-10-a': False,
        'bc-10-b': False,
        'bc-10-c': False,
        'bc-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Что нужно сделать с местом наклеивания груза?\n\n
a) Намочить его.\n
b) Покрасить.\n
c) Обезжирить.\n
d) Залить клеем.''',
                                      reply_markup=inline_keyboards.bc_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'bc-11-a')
@router.callback_query(F.data == 'bc-11-b')
@router.callback_query(F.data == 'bc-11-c')
@router.callback_query(F.data == 'bc-11-d')
async def bc_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-11-a': False,
        'bc-11-b': False,
        'bc-11-c': True,
        'bc-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Каким материалом обезжиривается место наклеивания груза?\n\n
a) Растворителем и туалетной бумагой.\n
b) Тканью.\n
c) Влажной салфеткой.\n
d) Губкой.''',
                                      reply_markup=inline_keyboards.bc_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-12-a')
@router.callback_query(F.data == 'bc-12-b')
@router.callback_query(F.data == 'bc-12-c')
@router.callback_query(F.data == 'bc-12-d')
async def bc_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-12-a': True,
        'bc-12-b': False,
        'bc-12-c': False,
        'bc-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Какой вес баланса груза указывается в примере?\n\n
а) 30 грамм.\n
b) 50 грамм и 40 грамм.\n
c) 70 грамм.\n
d) 100 грамм.''',
                                      reply_markup=inline_keyboards.bc_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-13-a')
@router.callback_query(F.data == 'bc-13-b')
@router.callback_query(F.data == 'bc-13-c')
@router.callback_query(F.data == 'bc-13-d')
async def bc_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-13-a': False,
        'bc-13-b': True,
        'bc-13-c': False,
        'bc-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Почему балансировочные грузы не приклеиваются сразу полностью?\n\n
a) Чтобы не испортить их.\n
b) Чтобы не повредить поверхность колеса.\n
c) Чтобы проверить другие грузы.\n
d) Чтобы в случае ошибки можно было их изменить или перенести.''',
                                      reply_markup=inline_keyboards.bc_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-14-a')
@router.callback_query(F.data == 'bc-14-b')
@router.callback_query(F.data == 'bc-14-c')
@router.callback_query(F.data == 'bc-14-d')
async def bc_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-14-a': False,
        'bc-14-b': False,
        'bc-14-c': False,
        'bc-14-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Что делается после того, как станок показал 0 грамм на обеих сторонах?\n\n
a) Прижимают грузы пальцем и снимают колесо.\n
b) Устанавливают колесо на машину.\n
c) Грузы закручиваются винтами.\n
d) Проводят дополнительную проверку на других станках.''',
                                      reply_markup=inline_keyboards.bc_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-15-a')
@router.callback_query(F.data == 'bc-15-b')
@router.callback_query(F.data == 'bc-15-c')
@router.callback_query(F.data == 'bc-15-d')
async def bc_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-15-a': True,
        'bc-15-b': False,
        'bc-15-c': False,
        'bc-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Что нужно сделать после финального наклеивания груза на колесо?\n\n
a) Проверить, что колесо вращается свободно.\n
b) Снять со станка и простучать грузы молотком.\n
c) Прокрутить колесо, чтобы убедиться в точности баланса.\n
d) Проверить давление в шинах.''',
                                      reply_markup=inline_keyboards.bc_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-16-a')
@router.callback_query(F.data == 'bc-16-b')
@router.callback_query(F.data == 'bc-16-c')
@router.callback_query(F.data == 'bc-16-d')
async def bc_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-16-a': False,
        'bc-16-b': True,
        'bc-16-c': False,
        'bc-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Что нужно установить на колесо после завершения балансировки?\n\n
a) Новый шланг.\n
b) Центральный колпачок.\n
c) Специальный защитный кожух.\n
d) Логотип компании.''',
                                      reply_markup=inline_keyboards.bc_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-17-a')
@router.callback_query(F.data == 'bc-17-b')
@router.callback_query(F.data == 'bc-17-c')
@router.callback_query(F.data == 'bc-17-d')
async def bc_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-17-a': False,
        'bc-17-b': True,
        'bc-17-c': False,
        'bc-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Почему важно не приклеивать грузы сразу полностью?\n\n
a) Чтобы в случае ошибки можно было переместить их.\n
b) Чтобы проверить балансировку еще раз.\n
c) Чтобы установить другие грузы.\n
d) Чтобы избежать повреждения шины.''',
                                      reply_markup=inline_keyboards.bc_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'bc-18-a')
@router.callback_query(F.data == 'bc-18-b')
@router.callback_query(F.data == 'bc-18-c')
@router.callback_query(F.data == 'bc-18-d')
async def bc_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'bc-18-a': False,
        'bc-18-b': True,
        'bc-18-c': False,
        'bc-18-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 18:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 18:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='bc_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 17 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 19

        if user_score >= 17:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/18.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.doprodaja()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/18.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 17 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.balance_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_bc_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_bc(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_pj_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='pj_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по допродажам!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что должен учитывать мастер в своей внешности, принимая клиента?\n\n
a) Наличие дорогой обуви.\n
b) Чистота и опрятность формы.\n
c) Использование яркой униформы.\n
d) Модную стрижку.''',
                                      reply_markup=inline_keyboards.pj_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'pj-1-a')
@router.callback_query(F.data == 'pj-1-b')
@router.callback_query(F.data == 'pj-1-c')
@router.callback_query(F.data == 'pj-1-d')
async def pj_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-1-a': False,
        'pj-1-b': True,
        'pj-1-c': False,
        'pj-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Что следует сделать, если у одного из колес давление ниже, чем у остальных?\n\n
a) Сразу заменить колесо.\n
b) Игнорировать, если спустило незначительно.\n
c) Предложить клиенту снять колесо и проверить, что внутри.\n
d) Установить запасное колесо.''',
                                      reply_markup=inline_keyboards.pj_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-2-a')
@router.callback_query(F.data == 'pj-2-b')
@router.callback_query(F.data == 'pj-2-c')
@router.callback_query(F.data == 'pj-2-d')
async def pj_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-2-a': False,
        'pj-2-b': False,
        'pj-2-c': True,
        'pj-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Почему важно проверять вентиль подкачки?\n\n
a) Чтобы убедиться, что колпачок красивый.\n
b) Для предотвращения утечки воздуха.\n
c) Чтобы заменить его на более длинный.\n
d) Это не является важным моментом.''',
                                      reply_markup=inline_keyboards.pj_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-3-a')
@router.callback_query(F.data == 'pj-3-b')
@router.callback_query(F.data == 'pj-3-c')
@router.callback_query(F.data == 'pj-3-d')
async def pj_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-3-a': False,
        'pj-3-b': True,
        'pj-3-c': False,
        'pj-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Что может указывать на необходимость замены вентиля?\n\n
a) Трещины на вентиле.\n
b) Отсутствие колпачка.\n
c) Перегрев шины.\n
d) Повреждение диска.''',
                               reply_markup=inline_keyboards.pj_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pj-4-a')
@router.callback_query(F.data == 'pj-4-b')
@router.callback_query(F.data == 'pj-4-c')
@router.callback_query(F.data == 'pj-4-d')
async def pj_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-4-a': True,
        'pj-4-b': False,
        'pj-4-c': False,
        'pj-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Сколько лет считается нормальным сроком эксплуатации колеса?\n\n
a) До 3 лет.\n
b) До 6 лет.\n
c) До 10 лет.\n
d) До 12 лет.''',
                                      reply_markup=inline_keyboards.pj_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-5-a')
@router.callback_query(F.data == 'pj-5-b')
@router.callback_query(F.data == 'pj-5-c')
@router.callback_query(F.data == 'pj-5-d')
async def pj_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-5-a': False,
        'pj-5-b': True,
        'pj-5-c': False,
        'pj-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какой способ взаимодействия с клиентом предлагается для предложения дополнительных услуг?\n\n
a) Обсудить проблему и предложить решение.\n
b) Навязывать клиенту все услуги сразу.\n
c) Игнорировать мелкие неисправности.\n
d) Установить цену без обсуждения.''',
                                      reply_markup=inline_keyboards.pj_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pj-6-a')
@router.callback_query(F.data == 'pj-6-b')
@router.callback_query(F.data == 'pj-6-c')
@router.callback_query(F.data == 'pj-6-d')
async def pj_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-6-a': True,
        'pj-6-b': False,
        'pj-6-c': False,
        'pj-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Что можно предложить клиенту при отсутствии секреток?\n\n
a) Заменить секретки на обычные болты.\n
b) Ничего не предлагать.\n
c) Установить новые секретки.\n
d) Проверить старые болты.''',
                                      reply_markup=inline_keyboards.pj_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-7-a')
@router.callback_query(F.data == 'pj-7-b')
@router.callback_query(F.data == 'pj-7-c')
@router.callback_query(F.data == 'pj-7-d')
async def pj_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-7-a': False,
        'pj-7-b': False,
        'pj-7-c': True,
        'pj-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Почему стоит проверять болты и гайки на колесах?\n\n
a) Чтобы убедиться, что они выглядят красиво.\n
b) Для предотвращения ржавления и их возможной поломки.\n
c) Чтобы установить болты другой длины.\n
d) Это неважно.''',
                                      reply_markup=inline_keyboards.pj_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-8-a')
@router.callback_query(F.data == 'pj-8-b')
@router.callback_query(F.data == 'pj-8-c')
@router.callback_query(F.data == 'pj-8-d')
async def pj_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-8-a': False,
        'pj-8-b': True,
        'pj-8-c': False,
        'pj-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Что следует проверить после разборки колеса?\n\n
a) Состояние резины.\n
b) Ровность диска.\n
c) Наличие секреток.\n
d) Цвет шин.''',
                                      reply_markup=inline_keyboards.pj_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-9-a')
@router.callback_query(F.data == 'pj-9-b')
@router.callback_query(F.data == 'pj-9-c')
@router.callback_query(F.data == 'pj-9-d')
async def pj_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-9-a': False,
        'pj-9-b': True,
        'pj-9-c': False,
        'pj-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Что такое оптимизация колеса?\n\n
a) Установка более легкого диска.\n
b) Устранение царапин на диске.\n
c) Проверка шин на износ.\n
d) Прокручивание колеса относительно диска для минимального веса на балансировке.''',
                                      reply_markup=inline_keyboards.pj_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-10-a')
@router.callback_query(F.data == 'pj-10-b')
@router.callback_query(F.data == 'pj-10-c')
@router.callback_query(F.data == 'pj-10-d')
async def pj_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-10-a': False,
        'pj-10-b': False,
        'pj-10-c': False,
        'pj-10-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''11. Что можно предложить клиенту во время сезонной смены шин?\n\n
a) Услугу консервации или хранения колес.\n
b) Покраску шин.\n
c) Ремонт подвески.\n
d) Проверку аккумулятора.''',
                                      reply_markup=inline_keyboards.pj_11_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pj-11-a')
@router.callback_query(F.data == 'pj-11-b')
@router.callback_query(F.data == 'pj-11-c')
@router.callback_query(F.data == 'pj-11-d')
async def pj_11_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-11-a': False,
        'pj-11-b': False,
        'pj-11-c': True,
        'pj-11-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''12. Как следует общаться с клиентом, чтобы сохранить его доверие?\n\n
a) Предлагать решения проблем, оставаясь честным.\n
b) Навязывать услуги.\n
c) Убеждать, что услуги обязательны.\n
d) Скрывать информацию о состоянии шин.''',
                                      reply_markup=inline_keyboards.pj_12_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-12-a')
@router.callback_query(F.data == 'pj-12-b')
@router.callback_query(F.data == 'pj-12-c')
@router.callback_query(F.data == 'pj-12-d')
async def pj_12_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-12-a': True,
        'pj-12-b': False,
        'pj-12-c': False,
        'pj-12-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''13. Почему важно проверять состояние резины?\n\n
а) Чтобы узнать возраст резины.\n
b) Для выявления повреждений или износа.\n
c) Чтобы оценить внешний вид автомобиля.\n
d) Это не важно при подкачке колес.''',
                                      reply_markup=inline_keyboards.pj_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-13-a')
@router.callback_query(F.data == 'pj-13-b')
@router.callback_query(F.data == 'pj-13-c')
@router.callback_query(F.data == 'pj-13-d')
async def pj_13_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-13-a': False,
        'pj-13-b': True,
        'pj-13-c': False,
        'pj-13-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''14. Что делать, если у вентиля обнаружены трещины?\n\n
a) Ничего, если утечки воздуха нет.\n
b) Проклеить трещины герметиком.\n
c) Установить новый вентиль бесплатно.\n
d) Предложить его заменить.''',
                                      reply_markup=inline_keyboards.pj_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-14-a')
@router.callback_query(F.data == 'pj-14-b')
@router.callback_query(F.data == 'pj-14-c')
@router.callback_query(F.data == 'pj-14-d')
async def pj_14_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-14-a': False,
        'pj-14-b': False,
        'pj-14-c': False,
        'pj-14-d': True,
    }
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''15. Какие дополнительные услуги можно предложить при подкачке колес?\n\n
a) Проверку и замену вентиля.\n
b) Балансировку колес.\n
c) Оптимизацию колеса.\n
d) Все перечисленные варианты.''',
                                      reply_markup=inline_keyboards.pj_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-15-a')
@router.callback_query(F.data == 'pj-15-b')
@router.callback_query(F.data == 'pj-15-c')
@router.callback_query(F.data == 'pj-15-d')
async def pj_15_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-15-a': True,
        'pj-15-b': False,
        'pj-15-c': False,
        'pj-15-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''16. Как мастер должен объяснить клиенту необходимость ремонта?\n\n
a) Указывать только на самые дорогие проблемы.\n
b) Простым языком рассказать, какие проблемы могут возникнуть.\n
c) Не предлагать услуги, если клиент не спрашивает.\n
d) Использовать сложные технические термины.''',
                                      reply_markup=inline_keyboards.pj_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-16-a')
@router.callback_query(F.data == 'pj-16-b')
@router.callback_query(F.data == 'pj-16-c')
@router.callback_query(F.data == 'pj-16-d')
async def pj_16_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-16-a': False,
        'pj-16-b': True,
        'pj-16-c': False,
        'pj-16-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''17. Что важно учитывать при проверке даты выпуска шин?\n\n
a) Год выпуска автомобиля.\n
b) Возраст шин и их срок эксплуатации.\n
c) Цвет протектора.\n
d) Количество слоев резины.''',
                                      reply_markup=inline_keyboards.pj_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-17-a')
@router.callback_query(F.data == 'pj-17-b')
@router.callback_query(F.data == 'pj-17-c')
@router.callback_query(F.data == 'pj-17-d')
async def pj_17_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-17-a': False,
        'pj-17-b': True,
        'pj-17-c': False,
        'pj-17-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''18. Какой подход к клиенту считается правильным?\n\n
a) Заставлять клиента оплачивать услуги заранее.\n
b) Предлагать только то, что необходимо, без давления.\n
c) Игнорировать мелкие проблемы, чтобы не отвлекать клиента.\n
d) Находить максимальное количество услуг для увеличения чека.''',
                                      reply_markup=inline_keyboards.pj_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-18-a')
@router.callback_query(F.data == 'pj-18-b')
@router.callback_query(F.data == 'pj-18-c')
@router.callback_query(F.data == 'pj-18-d')
async def pj_18_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pj-18-a': False,
        'pj-18-b': True,
        'pj-18-c': False,
        'pj-18-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''19. Что может произойти, если не заменить поврежденный вентиль?\n\n
    a) Проблем не будет.\n
    b) Может произойти утечка воздуха или вентиль оборвется.\n
    c) Ухудшится внешний вид колеса.\n
    d) Увеличится расход топлива.''',
                                      reply_markup=inline_keyboards.pj_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-19-a')
@router.callback_query(F.data == 'pj-19-b')
@router.callback_query(F.data == 'pj-19-c')
@router.callback_query(F.data == 'pj-19-d')
async def pj_19_note(callback: CallbackQuery, bot: Bot):
    correct_answers = {
        'pj-19-a': False,
        'pj-19-b': True,
        'pj-19-c': False,
        'pj-19-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''20. Какие повреждения резины требуют немедленной замены?\n\n
    a) Небольшие потертости.\n
    b) Глубокие трещины и вырванные куски.\n
    c) Легкие царапины на боковине.\n
    d) Износ, не достигающий индикатора протектора.''',
                                      reply_markup=inline_keyboards.pj_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pj-20-a')
@router.callback_query(F.data == 'pj-20-b')
@router.callback_query(F.data == 'pj-20-c')
@router.callback_query(F.data == 'pj-20-d')
async def pj_20_note(callback: CallbackQuery, bot: Bot):
    correct_answers = {
        'pj-20-a': False,
        'pj-20-b': True,
        'pj-20-c': False,
        'pj-20-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 20:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 20:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='pj_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 18 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 21

        if user_score >= 18:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/20.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.treningi()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/20.\n"
                     f"Для перехода к следующему курсу необходимо набрать минимум 18 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.prodaja_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_pj_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_pj(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_lt_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='lt_exam_pass'):
            await callback.answer(text='Вы уже проходили тест "Как делают шины"!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Какие основные компоненты входят в состав резины для автомобильной шины?\n\n
a) Каучук и природный латекс.\n
b) Технический углерод, смола и вулканизирующие активаторы.\n
c) Кремниевая кислота и масло.\n
d) Текстильный корд и медная проволока.''',
                                      reply_markup=inline_keyboards.lt_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'lt-1-a')
@router.callback_query(F.data == 'lt-1-b')
@router.callback_query(F.data == 'lt-1-c')
@router.callback_query(F.data == 'lt-1-d')
async def lt_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lt-1-a': False,
        'lt-1-b': True,
        'lt-1-c': False,
        'lt-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Почему резиновую массу многократно перемалывают?\n\n
a) Чтобы сделать её мягче.\n
b) Чтобы она быстрее высыхала.\n
c) Для равномерного распределения компонентов и удаления воздуха.\n
d) Для улучшения адгезии.''',
                                      reply_markup=inline_keyboards.lt_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lt-2-a')
@router.callback_query(F.data == 'lt-2-b')
@router.callback_query(F.data == 'lt-2-c')
@router.callback_query(F.data == 'lt-2-d')
async def lt_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lt-2-a': False,
        'lt-2-b': False,
        'lt-2-c': True,
        'lt-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Какое основное свойство металлического корда используется в производстве шин?\n\n
a) Пластичность.\n
b) Высокая упругость.\n
c) Низкая теплопроводность.\n
d) Устойчивость к коррозии.''',
                                      reply_markup=inline_keyboards.lt_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lt-3-a')
@router.callback_query(F.data == 'lt-3-b')
@router.callback_query(F.data == 'lt-3-c')
@router.callback_query(F.data == 'lt-3-d')
async def lt_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lt-3-a': False,
        'lt-3-b': True,
        'lt-3-c': False,
        'lt-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Для чего резину моют в мыльном растворе?\n\n
a) Для предотвращения слипания.\n
b) Чтобы удалить загрязнения.\n
c) Чтобы улучшить блеск поверхности.\n
d) Для уменьшения износа.''',
                               reply_markup=inline_keyboards.lt_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'lt-4-a')
@router.callback_query(F.data == 'lt-4-b')
@router.callback_query(F.data == 'lt-4-c')
@router.callback_query(F.data == 'lt-4-d')
async def lt_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lt-4-a': True,
        'lt-4-b': False,
        'lt-4-c': False,
        'lt-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Что обеспечивает текстильный или полимерный корд в шине?\n\n
a) Лучшую эластичность.\n
b) Прочность и жесткость.\n
c) Повышение сцепления с дорогой.\n
d) Защиту от проколов.''',
                                      reply_markup=inline_keyboards.lt_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lt-5-a')
@router.callback_query(F.data == 'lt-5-b')
@router.callback_query(F.data == 'lt-5-c')
@router.callback_query(F.data == 'lt-5-d')
async def lt_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lt-5-a': False,
        'lt-5-b': True,
        'lt-5-c': False,
        'lt-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какой тип шин обладает меньшим сопротивлением качению?\n\n
a) Радиальные.\n
b) Диагональные.\n
c) Летние.\n
d) Зимние.''',
                                      reply_markup=inline_keyboards.lt_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'lt-6-a')
@router.callback_query(F.data == 'lt-6-b')
@router.callback_query(F.data == 'lt-6-c')
@router.callback_query(F.data == 'lt-6-d')
async def lt_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lt-6-a': True,
        'lt-6-b': False,
        'lt-6-c': False,
        'lt-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Почему шины окрашивают в черный цвет?\n\n
a) Для улучшения прочности.\n
b) Для защиты от ультрафиолета.\n
c) Чтобы подчеркнуть протектор.\n
d) Проверить старые болты.''',
                                      reply_markup=inline_keyboards.lt_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lt-7-a')
@router.callback_query(F.data == 'lt-7-b')
@router.callback_query(F.data == 'lt-7-c')
@router.callback_query(F.data == 'lt-7-d')
async def lt_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lt-7-a': False,
        'lt-7-b': False,
        'lt-7-c': True,
        'lt-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Чем отличаются шины до вулканизации?\n\n
a) Уже имеют рисунок протектора.\n
b) Очень мягкие и легко мнутся руками.\n
c) Устойчивы к высоким температурам.\n
d) Более устойчивы к износу.''',
                                      reply_markup=inline_keyboards.lt_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lt-8-a')
@router.callback_query(F.data == 'lt-8-b')
@router.callback_query(F.data == 'lt-8-c')
@router.callback_query(F.data == 'lt-8-d')
async def lt_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lt-8-a': False,
        'lt-8-b': True,
        'lt-8-c': False,
        'lt-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Как проверяют шины после изготовления?\n\n
a) Пробной установкой на автомобиль.\n
b) Рентгеном для выявления дефектов.\n
c) Нагревом до высокой температуры.\n
d) Тестом на износ.''',
                                      reply_markup=inline_keyboards.lt_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lt-9-a')
@router.callback_query(F.data == 'lt-9-b')
@router.callback_query(F.data == 'lt-9-c')
@router.callback_query(F.data == 'lt-9-d')
async def lt_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lt-9-a': False,
        'lt-9-b': True,
        'lt-9-c': False,
        'lt-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Что происходит в процессе вулканизации?\n\n
a) Формирование рисунка протектора.\n
b) Изменение структуры металлического корда.\n
c) Окрашивание шины.\n
d) Создание пространственной сетки молекул каучука.''',
                                      reply_markup=inline_keyboards.lt_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lt-10-a')
@router.callback_query(F.data == 'lt-10-b')
@router.callback_query(F.data == 'lt-10-c')
@router.callback_query(F.data == 'lt-10-d')
async def lt_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lt-10-a': False,
        'lt-10-b': False,
        'lt-10-c': False,
        'lt-10-d': True,
    }

    if dict_to_check_progress[callback.from_user.id] == 10:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 10:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='lt_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 9 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 11

        if user_score >= 9:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/10.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.kolesa_shini()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/10.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 9 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.proizvodstvo_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_lt_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_lt(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_pv_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='pv_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по колёсам и шинам!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что составляет основную часть шины?\n\n
a) Слой резины.\n
b) Тканевый каркас, называемый кордой.\n
c) Брекер.\n
d) Протектор.''',
                                      reply_markup=inline_keyboards.pv_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'pv-1-a')
@router.callback_query(F.data == 'pv-1-b')
@router.callback_query(F.data == 'pv-1-c')
@router.callback_query(F.data == 'pv-1-d')
async def pv_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pv-1-a': False,
        'pv-1-b': True,
        'pv-1-c': False,
        'pv-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Как называется часть шины, которая обеспечивает плотную посадку на диск колеса?\n\n
a) Протектор.\n
b) Брекер.\n
c) Борт.\n
d) Боковина.''',
                                      reply_markup=inline_keyboards.pv_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pv-2-a')
@router.callback_query(F.data == 'pv-2-b')
@router.callback_query(F.data == 'pv-2-c')
@router.callback_query(F.data == 'pv-2-d')
async def pv_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pv-2-a': False,
        'pv-2-b': False,
        'pv-2-c': True,
        'pv-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Из чего состоит корда шины?\n\n
a) Только из ткани.\n
b) Слой резины и слой ткани.\n
c) Только из резины.\n
d) Из нескольких слоев резины.''',
                                      reply_markup=inline_keyboards.pv_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pv-3-a')
@router.callback_query(F.data == 'pv-3-b')
@router.callback_query(F.data == 'pv-3-c')
@router.callback_query(F.data == 'pv-3-d')
async def pv_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pv-3-a': False,
        'pv-3-b': True,
        'pv-3-c': False,
        'pv-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Где на шине наносятся все надписи и обозначения?\n\n
a) На боковине.\n
b) На корде.\n
c) На протекторе.\n
d) На бортовой части.''',
                               reply_markup=inline_keyboards.pv_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pv-4-a')
@router.callback_query(F.data == 'pv-4-b')
@router.callback_query(F.data == 'pv-4-c')
@router.callback_query(F.data == 'pv-4-d')
async def pv_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pv-4-a': True,
        'pv-4-b': False,
        'pv-4-c': False,
        'pv-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Что такое брекер шины?\n\n
a) Слой ткани.\n
b) Прорезиненный корд, расположенный между каркасом и протектором.\n
c) Слой резины.\n
d) Элемент, защищающий от проколов.''',
                                      reply_markup=inline_keyboards.pv_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pv-5-a')
@router.callback_query(F.data == 'pv-5-b')
@router.callback_query(F.data == 'pv-5-c')
@router.callback_query(F.data == 'pv-5-d')
async def pv_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pv-5-a': False,
        'pv-5-b': True,
        'pv-5-c': False,
        'pv-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какую функцию выполняет брекер?\n\n
a) Предохраняет каркас от толчков и ударов.\n
b) Защищает протектор от повреждений.\n
c) Обеспечивает герметичность посадки на диск.\n
d) Наносит на шину надписи.''',
                                      reply_markup=inline_keyboards.pv_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'pv-6-a')
@router.callback_query(F.data == 'pv-6-b')
@router.callback_query(F.data == 'pv-6-c')
@router.callback_query(F.data == 'pv-6-d')
async def pv_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pv-6-a': True,
        'pv-6-b': False,
        'pv-6-c': False,
        'pv-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Для чего нужен протектор шины?\n\n
a) Для герметичности посадки.\n
b) Для создания оптимального пятна контакта.\n
c) Для защиты шины от проколов и повреждений.\n
d) Для защиты от коррозии.''',
                                      reply_markup=inline_keyboards.pv_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pv-7-a')
@router.callback_query(F.data == 'pv-7-b')
@router.callback_query(F.data == 'pv-7-c')
@router.callback_query(F.data == 'pv-7-d')
async def pv_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pv-7-a': False,
        'pv-7-b': False,
        'pv-7-c': True,
        'pv-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Что влияет на форму пятна контакта шины с дорогой?\n\n
a) Слой ткани.\n
b) Брекер.\n
c) Борт.\n
d) Протектор.''',
                                      reply_markup=inline_keyboards.pv_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pv-8-a')
@router.callback_query(F.data == 'pv-8-b')
@router.callback_query(F.data == 'pv-8-c')
@router.callback_query(F.data == 'pv-8-d')
async def pv_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pv-8-a': False,
        'pv-8-b': True,
        'pv-8-c': False,
        'pv-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Где расположен брекер в шине?\n\n
a) Между боковиной и резиновым слоем.\n
b) Между каркасом и протектором.\n
c) На внешней стороне шины.\n
d) Внутри корды.''',
                                      reply_markup=inline_keyboards.pv_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pv-9-a')
@router.callback_query(F.data == 'pv-9-b')
@router.callback_query(F.data == 'pv-9-c')
@router.callback_query(F.data == 'pv-9-d')
async def pv_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pv-9-a': False,
        'pv-9-b': True,
        'pv-9-c': False,
        'pv-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Какие слои содержатся в корде шины?\n\n
a) Слой ткани и слой металла.\n
b) Только резина.\n
c) Только ткань.\n
d) Несколько слоев резины и ткани.''',
                                      reply_markup=inline_keyboards.pv_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'pv-10-a')
@router.callback_query(F.data == 'pv-10-b')
@router.callback_query(F.data == 'pv-10-c')
@router.callback_query(F.data == 'pv-10-d')
async def pv_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'pv-10-a': False,
        'pv-10-b': False,
        'pv-10-c': False,
        'pv-10-d': True,
    }

    if dict_to_check_progress[callback.from_user.id] == 10:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 10:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='pv_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 9 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 11

        if user_score >= 9:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/10.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.kolesa_shini()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/10.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 9 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.kolesaishini_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_pv_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_pv(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_ki_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='ki_exam_pass'):
                await callback.answer(text='Вы уже проходили тест по левым и правым шинам. Разница!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что обозначает маркировка "Rotation" на шинах?\n\n
a) Внешняя сторона.\n
b) Направление вращения.\n
c) Внутренняя сторона.\n
d) Тип протектора.''',
                                      reply_markup=inline_keyboards.ki_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'ki-1-a')
@router.callback_query(F.data == 'ki-1-b')
@router.callback_query(F.data == 'ki-1-c')
@router.callback_query(F.data == 'ki-1-d')
async def ki_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ki-1-a': False,
        'ki-1-b': True,
        'ki-1-c': False,
        'ki-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. На асимметричных шинах маркировка "Outside" указывает?\n\n
a) Внутреннюю сторону шины.\n
b) Направление установки.\n
c) Внешнюю сторону шины.\n
d) Тип протектора.''',
                                      reply_markup=inline_keyboards.ki_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ki-2-a')
@router.callback_query(F.data == 'ki-2-b')
@router.callback_query(F.data == 'ki-2-c')
@router.callback_query(F.data == 'ki-2-d')
async def ki_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ki-2-a': False,
        'ki-2-b': False,
        'ki-2-c': True,
        'ki-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Основная цель асимметричного рисунка протектора?\n\n
a) Увеличение скорости автомобиля.\n
b) Уменьшение риска аквапланирования.\n
c) Улучшение сцепления на снегу.\n
d) Уменьшение износа шины.''',
                                      reply_markup=inline_keyboards.ki_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ki-3-a')
@router.callback_query(F.data == 'ki-3-b')
@router.callback_query(F.data == 'ki-3-c')
@router.callback_query(F.data == 'ki-3-d')
async def ki_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ki-3-a': False,
        'ki-3-b': True,
        'ki-3-c': False,
        'ki-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Как правильно устанавливать асимметричные шины?\n\n
a) По маркировкам Inside и Outside.\n
b) Согласно маркировке Rotation.\n
c) В зависимости от стороны автомобиля.\n
d) В произвольном порядке.''',
                               reply_markup=inline_keyboards.ki_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ki-4-a')
@router.callback_query(F.data == 'ki-4-b')
@router.callback_query(F.data == 'ki-4-c')
@router.callback_query(F.data == 'ki-4-d')
async def ki_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ki-4-a': True,
        'ki-4-b': False,
        'ki-4-c': False,
        'ki-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Почему асимметричные шины уменьшают шум?\n\n
a) Из-за использования специальных материалов.\n
b) Из-за гашения звуков волн противофазой.\n
c) Благодаря направленному протектору.\n
d) Из-за уменьшения трения.''',
                                      reply_markup=inline_keyboards.ki_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ki-5-a')
@router.callback_query(F.data == 'ki-5-b')
@router.callback_query(F.data == 'ki-5-c')
@router.callback_query(F.data == 'ki-5-d')
async def ki_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ki-5-a': False,
        'ki-5-b': True,
        'ki-5-c': False,
        'ki-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Что могло стать причиной появления асимметричных шин?\n\n
a) Проблемы с запасами только левых или правых шин.\n
b) Экономия на производстве.\n
c) Потребность в новых технологиях.\n
d) Увеличение прибыли.''',
                                      reply_markup=inline_keyboards.ki_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ki-6-a')
@router.callback_query(F.data == 'ki-6-b')
@router.callback_query(F.data == 'ki-6-c')
@router.callback_query(F.data == 'ki-6-d')
async def ki_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ki-6-a': True,
        'ki-6-b': False,
        'ki-6-c': False,
        'ki-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Как производители решают проблему остатков левых или правых шин?\n\n
a) Продают их дешевле.\n
b) Утилизируют их.\n
c) Производят асимметричные шины.\n
d) Не решают эту проблему.''',
                                      reply_markup=inline_keyboards.ki_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ki-7-a')
@router.callback_query(F.data == 'ki-7-b')
@router.callback_query(F.data == 'ki-7-c')
@router.callback_query(F.data == 'ki-7-d')
async def ki_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ki-7-a': False,
        'ki-7-b': False,
        'ki-7-c': True,
        'ki-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какие шины имеют одинаковую маркировку "Rotation" с обеих сторон?\n\n
a) Асимметричные.\n
b) Направленные.\n
c) Симметричные.\n
d) Всесезонные.''',
                                      reply_markup=inline_keyboards.ki_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ki-8-a')
@router.callback_query(F.data == 'ki-8-b')
@router.callback_query(F.data == 'ki-8-c')
@router.callback_query(F.data == 'ki-8-d')
async def ki_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ki-8-a': False,
        'ki-8-b': True,
        'ki-8-c': False,
        'ki-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Как асимметричные шины влияют на управление в дождь?\n\n
a) Ухудшают сцепление.\n
b) Улучшают отвод воды.\n
c) Не влияют.\n
d) Увеличивают аквапланирование.''',
                                      reply_markup=inline_keyboards.ki_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ki-9-a')
@router.callback_query(F.data == 'ki-9-b')
@router.callback_query(F.data == 'ki-9-c')
@router.callback_query(F.data == 'ki-9-d')
async def ki_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ki-9-a': False,
        'ki-9-b': True,
        'ki-9-c': False,
        'ki-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Какой совет дают производители по установке шин?\n\n
a) Устанавливать по рисунку протектора.\n
b) Устанавливать на глаз.\n
c) Не обращать внимания на маркировки.\n
d) Устанавливать по маркировкам на боковинах.''',
                                      reply_markup=inline_keyboards.ki_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ki-10-a')
@router.callback_query(F.data == 'ki-10-b')
@router.callback_query(F.data == 'ki-10-c')
@router.callback_query(F.data == 'ki-10-d')
async def ki_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ki-10-a': False,
        'ki-10-b': False,
        'ki-10-c': False,
        'ki-10-d': True,
    }

    if dict_to_check_progress[callback.from_user.id] == 10:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 10:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='ki_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 9 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 11

        if user_score >= 9:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/10.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.left_right()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/10.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 9 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.leftandright_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_ki_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_ki(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_lr_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='lr_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по Маркировки шин. Часть 2!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что обозначает цифра 91 в маркировке шины?\n\n
a) Максимальная ширина шины.\n
b) Индекс нагрузки на одно колесо.\n
c) Скоростной индекс.\n
d) Порядковый номер недели производства.''',
                                      reply_markup=inline_keyboards.lr_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'lr-1-a')
@router.callback_query(F.data == 'lr-1-b')
@router.callback_query(F.data == 'lr-1-c')
@router.callback_query(F.data == 'lr-1-d')
async def lr_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lr-1-a': False,
        'lr-1-b': True,
        'lr-1-c': False,
        'lr-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какая информация указана в размере шин "215/55 R16"?\n\n
a) Высота профиля, индекс скорости, год выпуска.\n
b) Индекс нагрузки, материал каркаса, страна производства.\n
c) Ширина, высота профиля, диаметр обода.\n
d) Тип рисунка протектора, сезонность, уровень шума.''',
                                      reply_markup=inline_keyboards.lr_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lr-2-a')
@router.callback_query(F.data == 'lr-2-b')
@router.callback_query(F.data == 'lr-2-c')
@router.callback_query(F.data == 'lr-2-d')
async def lr_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lr-2-a': False,
        'lr-2-b': False,
        'lr-2-c': True,
        'lr-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Какой индекс скорости соответствует максимальной скорости 240 км/ч?\n\n
a) W.\n
b) V.\n
c) T.\n
d) H.''',
                                      reply_markup=inline_keyboards.lr_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lr-3-a')
@router.callback_query(F.data == 'lr-3-b')
@router.callback_query(F.data == 'lr-3-c')
@router.callback_query(F.data == 'lr-3-d')
async def lr_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lr-3-a': False,
        'lr-3-b': True,
        'lr-3-c': False,
        'lr-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Что обозначает маркировка "RunFlat" на шинах?\n\n
a) Возможность движения при полной потере давления.\n
b) Для бездорожья.\n
c) Усиленная боковина.\n
d) Снижение шума.''',
                               reply_markup=inline_keyboards.lr_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'lr-4-a')
@router.callback_query(F.data == 'lr-4-b')
@router.callback_query(F.data == 'lr-4-c')
@router.callback_query(F.data == 'lr-4-d')
async def lr_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lr-4-a': True,
        'lr-4-b': False,
        'lr-4-c': False,
        'lr-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Что означает буква R в маркировке размера шин?\n\n
a) Радиус.\n
b) Радиальная конструкция.\n
c) Шипованная шина.\n
d) Размер обода.''',
                                      reply_markup=inline_keyboards.lr_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lr-5-a')
@router.callback_query(F.data == 'lr-5-b')
@router.callback_query(F.data == 'lr-5-c')
@router.callback_query(F.data == 'lr-5-d')
async def lr_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lr-5-a': False,
        'lr-5-b': True,
        'lr-5-c': False,
        'lr-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какой диапазон гарантии обычно предоставляется на шины?\n\n
a) 3 года.\n
b) 5 лет.\n
c) 7 лет.\n
d) 10 лет.''',
                                      reply_markup=inline_keyboards.lr_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'lr-6-a')
@router.callback_query(F.data == 'lr-6-b')
@router.callback_query(F.data == 'lr-6-c')
@router.callback_query(F.data == 'lr-6-d')
async def lr_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lr-6-a': False,
        'lr-6-b': True,
        'lr-6-c': False,
        'lr-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Что обозначает маркировка "M+S"?\n\n
a) Для использования на воде.\n
b) Для использования летом.\n
c) Грязь и снег (всесезонные шины).\n
d) Усиленный каркас.''',
                                      reply_markup=inline_keyboards.lr_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lr-7-a')
@router.callback_query(F.data == 'lr-7-b')
@router.callback_query(F.data == 'lr-7-c')
@router.callback_query(F.data == 'lr-7-d')
async def lr_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lr-7-a': False,
        'lr-7-b': False,
        'lr-7-c': True,
        'lr-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Что обозначает "XL" в маркировке шин?\n\n
a) Экономия топлива.\n
b) Усиленная шина с повышенным индексом нагрузки.\n
c) Летняя шина.\n
d) Бескамерная шина.''',
                                      reply_markup=inline_keyboards.lr_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lr-8-a')
@router.callback_query(F.data == 'lr-8-b')
@router.callback_query(F.data == 'lr-8-c')
@router.callback_query(F.data == 'lr-8-d')
async def lr_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lr-8-a': False,
        'lr-8-b': True,
        'lr-8-c': False,
        'lr-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Какие данные включены в маркировку EU?\n\n
a) Год выпуска, индекс нагрузки, уровень шума.\n
b) Класс экономии топлива, сцепление, шумность.\n
c) Тип каркаса, рисунок протектора, сезонность.\n
d) Материал шины, размер, страна производства.''',
                                      reply_markup=inline_keyboards.lr_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lr-9-a')
@router.callback_query(F.data == 'lr-9-b')
@router.callback_query(F.data == 'lr-9-c')
@router.callback_query(F.data == 'lr-9-d')
async def lr_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lr-9-a': False,
        'lr-9-b': True,
        'lr-9-c': False,
        'lr-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Что означает маркировка "Outside"?\n\n
a) Направление вращения.\n
b) Внутренняя сторона шины.\n
c) Для бескамерных шин.\n
d) Наружная сторона шины.''',
                                      reply_markup=inline_keyboards.lr_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'lr-10-a')
@router.callback_query(F.data == 'lr-10-b')
@router.callback_query(F.data == 'lr-10-c')
@router.callback_query(F.data == 'lr-10-d')
async def lr_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'lr-10-a': False,
        'lr-10-b': False,
        'lr-10-c': False,
        'lr-10-d': True,
    }

    if dict_to_check_progress[callback.from_user.id] == 10:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 10:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='lr_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 9 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 11

        if user_score >= 9:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/10.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.shinka_disk()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/10.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 9 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.markirovkads_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_lr_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_lr(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_ms_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='ms_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по шинке дисков!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Из чего изготавливаются штампованные диски?\n\n
a) Из алюминиевых сплавов.\n
b) Из стали.\n
c) Из пластика.\n
d) Из магния.''',
                                      reply_markup=inline_keyboards.ms_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'ms-1-a')
@router.callback_query(F.data == 'ms-1-b')
@router.callback_query(F.data == 'ms-1-c')
@router.callback_query(F.data == 'ms-1-d')
async def ms_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ms-1-a': False,
        'ms-1-b': True,
        'ms-1-c': False,
        'ms-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Какое основное свойство штампованных дисков?\n\n
a) Высокая прочность.\n
b) Легкость.\n
c) Пластичность.\n
d) Хрупкость.''',
                                      reply_markup=inline_keyboards.ms_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ms-2-a')
@router.callback_query(F.data == 'ms-2-b')
@router.callback_query(F.data == 'ms-2-c')
@router.callback_query(F.data == 'ms-2-d')
async def ms_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ms-2-a': False,
        'ms-2-b': False,
        'ms-2-c': True,
        'ms-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. Чем отличаются литые диски?\n\n
a) Их можно легко выправить после удара.\n
b) Они хрупкие и могут треснуть при ударе.\n
c) Они изготавливаются из стали.\n
d) Они всегда дешевые.''',
                                      reply_markup=inline_keyboards.ms_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ms-3-a')
@router.callback_query(F.data == 'ms-3-b')
@router.callback_query(F.data == 'ms-3-c')
@router.callback_query(F.data == 'ms-3-d')
async def ms_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ms-3-a': False,
        'ms-3-b': True,
        'ms-3-c': False,
        'ms-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Из каких материалов изготавливаются литые диски?\n\n
a) Из алюминиевых или магниевых сплавов.\n
b) Из стали.\n
c) Из пластика.\n
d) Из кованой стали.''',
                               reply_markup=inline_keyboards.ms_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ms-4-a')
@router.callback_query(F.data == 'ms-4-b')
@router.callback_query(F.data == 'ms-4-c')
@router.callback_query(F.data == 'ms-4-d')
async def ms_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ms-4-a': True,
        'ms-4-b': False,
        'ms-4-c': False,
        'ms-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Что нужно регулярно проверять у литых дисков?\n\n
a) Балансировку.\n
b) Трещины.\n
c) Цвет покрытия.\n
d) Форма отверстий.''',
                                      reply_markup=inline_keyboards.ms_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ms-5-a')
@router.callback_query(F.data == 'ms-5-b')
@router.callback_query(F.data == 'ms-5-c')
@router.callback_query(F.data == 'ms-5-d')
async def ms_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ms-5-a': False,
        'ms-5-b': True,
        'ms-5-c': False,
        'ms-5-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''6. Какое основное свойство кованных дисков?\n\n
a) Пластичность.\n
b) Высокая прочность.\n
c) Хрупкость.\n
d) Устойчивость к коррозии.''',
                                      reply_markup=inline_keyboards.ms_6_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'ms-6-a')
@router.callback_query(F.data == 'ms-6-b')
@router.callback_query(F.data == 'ms-6-c')
@router.callback_query(F.data == 'ms-6-d')
async def ms_6_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ms-6-a': False,
        'ms-6-b': True,
        'ms-6-c': False,
        'ms-6-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''7. Какое воздействие кованные диски могут передавать на подвеску?\n\n
a) Уменьшают вибрации.\n
b) Увеличивают плавность хода.\n
c) Передают ударный нагрузку.\n
d) Снижают износ деталей.''',
                                      reply_markup=inline_keyboards.ms_7_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ms-7-a')
@router.callback_query(F.data == 'ms-7-b')
@router.callback_query(F.data == 'ms-7-c')
@router.callback_query(F.data == 'ms-7-d')
async def ms_7_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ms-7-a': False,
        'ms-7-b': False,
        'ms-7-c': True,
        'ms-7-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''8. Какие диски являются наиболее легкими?\n\n
a) Штампованные.\n
b) Кованые.\n
c) Литые.\n
d) Пластиковые.''',
                                      reply_markup=inline_keyboards.ms_8_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ms-8-a')
@router.callback_query(F.data == 'ms-8-b')
@router.callback_query(F.data == 'ms-8-c')
@router.callback_query(F.data == 'ms-8-d')
async def ms_8_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ms-8-a': False,
        'ms-8-b': True,
        'ms-8-c': False,
        'ms-8-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''9. Какой внешний вид у литых дисков?\n\n
a) Некрасивый.\n
b) Стильный и привлекательный.\n
c) Обычный и простой.\n
d) Незаметный.''',
                                      reply_markup=inline_keyboards.ms_9_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ms-9-a')
@router.callback_query(F.data == 'ms-9-b')
@router.callback_query(F.data == 'ms-9-c')
@router.callback_query(F.data == 'ms-9-d')
async def ms_9_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ms-9-a': False,
        'ms-9-b': True,
        'ms-9-c': False,
        'ms-9-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''10. Какие диски самые дорогие?\n\n
a) Штампованные.\n
b) Литые.\n
c) Пластиковые.\n
d) Кованые.''',
                                      reply_markup=inline_keyboards.ms_10_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ms-10-a')
@router.callback_query(F.data == 'ms-10-b')
@router.callback_query(F.data == 'ms-10-c')
@router.callback_query(F.data == 'ms-10-d')
async def ms_10_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'ms-10-a': False,
        'ms-10-b': False,
        'ms-10-c': False,
        'ms-10-d': True,
    }

    if dict_to_check_progress[callback.from_user.id] == 10:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 10:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='ms_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 9 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 11

        if user_score >= 9:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/10.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=inline_keyboards.shinka_disk()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/10.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 9 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.shinkadisk_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_ms_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_ms(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()

@router.callback_query(F.data == 'get_me_to_sd_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    try:
        user_id = callback.from_user.id
        user_name = callback.from_user.first_name

        # Проверяем, проходил ли пользователь тест
        if sqlite_funcs.check_user_test(user_id, test_column='sd_exam_pass'):
            await callback.answer(text='Вы уже проходили тест по шинке дисков!', show_alert=True)
        else:
            # Проверяем, есть ли пользователь в базе, и добавляем его при необходимости
            if sqlite_funcs.check_user(user_id):
                sqlite_funcs.adding_users(tg_id=user_id, name=user_name)

            # Уведомляем администраторов
            await bot.send_message(chat_id=admin_id, text=f'Пользователь {user_name} начал проходить тест.')

            # Инициализация прогресса
            dict_to_check_progress[user_id] = 1
            users[user_id] = 0

            # Отправляем первый вопрос
            await callback.message.answer(
                text="Тест нужно пройти полностью, до конца, иначе результат не зачтется. Удачи!"
            )

        await callback.message.answer(text='''1. Что означает маркировка Studded на шинах?\n\n
a) Шина не может быть шипованной.\n
b) Шина всегда поставляется с шипами.\n
c) Шина предназначена для летней эксплуатации.\n
d) Шина поставляется без протектора.''',
                                      reply_markup=inline_keyboards.sd_1_answer()
        )
        await callback.answer()
    except Exception as e:
        print(f"Ошибка в 'lets_start_a_test': {e}")
        await callback.message.answer("Произошла ошибка. Попробуйте позже.")
        await callback.answer()

@router.callback_query(F.data == 'sd-1-a')
@router.callback_query(F.data == 'sd-1-b')
@router.callback_query(F.data == 'sd-1-c')
@router.callback_query(F.data == 'sd-1-d')
async def sd_1_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sd-1-a': False,
        'sd-1-b': True,
        'sd-1-c': False,
        'sd-1-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''2. Что означает маркировка Studable?\n\n
a) Шина всегда шипованная.\n
b) Шина предназначена только для сухих дорог.\n
c) Шина может быть шипована при необходимости.\n
d) Шина выпускается с металлическим каркасом.''',
                                      reply_markup=inline_keyboards.sd_2_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sd-2-a')
@router.callback_query(F.data == 'sd-2-b')
@router.callback_query(F.data == 'sd-2-c')
@router.callback_query(F.data == 'sd-2-d')
async def sd_2_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sd-2-a': False,
        'sd-2-b': False,
        'sd-2-c': True,
        'sd-2-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''3. В чём главное отличие шин Studded от Studable?\n\n
a) Studable всегда поставляются с шипами.\n
b) Studded всегда шипованы на заводе, а Studable могут быть шипованы позже.\n
c) Studded используются только в России.\n
d) Разницы нет, это одно и то же.''',
                                      reply_markup=inline_keyboards.sd_3_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sd-3-a')
@router.callback_query(F.data == 'sd-3-b')
@router.callback_query(F.data == 'sd-3-c')
@router.callback_query(F.data == 'sd-3-d')
async def sd_3_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sd-3-a': False,
        'sd-3-b': True,
        'sd-3-c': False,
        'sd-3-d': False,
    }
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await bot.send_message(text='''4. Для чего могут использоваться шины Studable без шипов?\n\n
a) Для регионов с мягким климатом.\n
b) Для спортивных автомобилей.\n
c) Для грузовых автомобилей.\n
d) Для езды по гравию.''',
                               reply_markup=inline_keyboards.sd_4_answer(), chat_id=callback.from_user.id
                               )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')

@router.callback_query(F.data == 'sd-4-a')
@router.callback_query(F.data == 'sd-4-b')
@router.callback_query(F.data == 'sd-4-c')
@router.callback_query(F.data == 'sd-4-d')
async def sd_4_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sd-4-a': True,
        'sd-4-b': False,
        'sd-4-c': False,
        'sd-4-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)
        await callback.message.answer(text='''5. Почему шины Studable иногда продаются без шипов?\n\n
a) Чтобы снизить стоимость.\n
b) Для адаптации к погодным условиям страны продаж.\n
c) Для увеличения срока службы.\n
d) Для повышения топливной экономичности.''',
                                      reply_markup=inline_keyboards.sd_5_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'sd-5-a')
@router.callback_query(F.data == 'sd-5-b')
@router.callback_query(F.data == 'sd-5-c')
@router.callback_query(F.data == 'sd-5-d')
async def sd_5_note(callback: CallbackQuery, bot: Bot):

    correct_answers = {
        'sd-5-a': False,
        'sd-5-b': True,
        'sd-5-c': False,
        'sd-5-d': False,
    }

    if dict_to_check_progress[callback.from_user.id] == 5:
        is_correct = correct_answers.get(callback.data, False)
        if is_correct:
            users[callback.from_user.id] += 1
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
        else:
            await bot.send_message(text='Неправильно!', chat_id=callback.from_user.id)

        user_id = callback.from_user.id
        user_score = users.get(callback.from_user.id, 0)
        if dict_to_check_progress[user_id] == 5:
            # Обновляем статус теста в базе данных
            sqlite_funcs.update_test_status(
                tg_id=user_id,
                test_column='sd_exam_pass',  # Убедитесь, что столбец существует
                status=1 if user_score >= 5 else 0
            )
            dict_to_check_progress[callback.from_user.id] = 6

        if user_score >= 5:
            await callback.message.answer(
            text = f"Поздравляю! Вы прошли тест, результат: {user_score}/5.\n"
            f"Теперь вы можете перейти к изучению других курсов.",
            reply_markup=reply_keyboards.choose_course()
            )

        else:
            await callback.message.answer(
                text=f"К сожалению, вы не прошли тест. Ваш результат: {user_score}/5.\n"
                     f"Для перехода к следующему уроку необходимо набрать минимум 5 баллов.\n"
                     f"Попробуйте пройти тест ещё раз.",
                reply_markup=inline_keyboards.studorstudd_zanovo()  # Клавиатура для повторного прохождения
            )
            sqlite_funcs.change_opportunity_for_sd_test(callback.from_user.id)
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id
            )
            await bot.send_message(
                text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{user_score} баллов',
                chat_id=admin_id1
            )
            sqlite_funcs.get_finished_with_sd(callback.from_user.id)
            # Сброс очков
            users[callback.from_user.id] = 0
            dict_to_check_progress[callback.from_user.id] = 1  # Возвращаем на первый вопрос

    else:
        # Если пользователь пытается ответить повторно
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')
    await callback.answer()