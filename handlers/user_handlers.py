import time
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram import Router, F, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from CarKnowlegdeTest import carTest

from keyboards import inline_keyboards, reply_keyboards
from database_funcs import sqlite_funcs

admin_id = 1004684045
admin_id1 = 332518143

router = Router()

storage = MemoryStorage()

dict_to_check_progress = {}
users = {}
users_car_test = dict()


# FSM (состояния)
class QuizStates(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    Q6 = State()
    Q7 = State()
    Q8 = State()
    Q9 = State()
    Q10 = State()


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
                              'Для прохождения курсов необходимо узнать у куратора специальный код для допуска\n\n'
                              'Расти и развивайся вместе с нами!\n'
                              '/menu',
                         reply_markup=reply_keyboards.choose_course())


@router.message(F.text == 'Слесарные работы')
async def show_hello_slesarka(message: Message):
    await message.answer(text='Добро пожаловать на курс!\n\nДля продолжения, необходимо авторизоваться\nВведите код:',
                         reply_markup=ReplyKeyboardRemove())


@router.message(F.text == '6481373')
async def send_osmotr_video(message: Message):
    await message.answer(
        text='Устройство автомобиля - это тот фундамент, который необходимо заложить перед изучением дальнейшего материала.\n\n'
             'В этом видео вы поймете из чего состоит автомобиль. На простых примерах будут показаны основные его части.\n\n'
             'Если нет доступа - обратитесь к Павлу Лизневу',
        reply_markup=inline_keyboards.send_video_osmotr()
    )


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
                              'Для продолжения, введите код:',
                         reply_markup=ReplyKeyboardRemove())


@router.message(F.text == '4073972')
async def send_video_about_ac_1st_part(message: Message):
    await message.answer(text='Ниже представлены видеоматериалы по работам.\n\n'
                              'Ознакомьтесь со всеми',
                         reply_markup=inline_keyboards.graphics_to_continue())


@router.callback_query(F.data == 'get_me_to_menu')
async def redirect_to_menu(callback: CallbackQuery):
    await callback.message.answer(text='Это главное меню!', reply_markup=reply_keyboards.choose_course())


@router.message(F.text == 'Электрика авто')
async def say_hello_electricity(message: Message):
    await message.answer(text='Приветствую на курсе по электрике автомобиля!\n\n'
                              'Для продолжения, введите код:',
                         reply_markup=ReplyKeyboardRemove())


@router.message(F.text == 'Шиномонтаж')
async def say_hello_electricity(message: Message):
    await message.answer(text='Приветствую на курсе по шиномонтажу!\n\n'
                              'Для продолжения, введите код:',
                         reply_markup=ReplyKeyboardRemove())


@router.callback_query(F.data == 'i_did_watch_the_video')
async def start_quiz(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id not in users_car_test:
        users_car_test[callback.from_user.id] = {
            'first_name': callback.from_user.first_name,
            'username': callback.from_user.username,
            'tries': 1,
            'correct_answers': 0,
            'incorrect_answers': 0
        }
    else:
        users_car_test[callback.from_user.id]['tries'] += 1
        users_car_test[callback.from_user.id]['correct_answers'] = 0
        users_car_test[callback.from_user.id]['incorrect_answers'] = 0
    await callback.message.answer(carTest.questions[0]["question"], reply_markup=reply_keyboards.get_keyboard(0))
    await state.set_state(QuizStates.Q1)
    await callback.answer()


async def handle_answer(message: Message, state: FSMContext, question_index: int, next_state: State, bot: Bot):
    user_answer = message.text

    correct_answer = [a for a, correct in carTest.questions[question_index]["answers"] if correct][0]
    print(user_answer)
    if user_answer == correct_answer:
        users_car_test[message.from_user.id]['correct_answers'] += 1
        await message.answer("Правильный ответ!")
    else:
        users_car_test[message.from_user.id]['incorrect_answers'] += 1
        await message.answer(f"Неправильный ответ.\n\nПравильный ответ: {correct_answer}")

    # Переход к следующему вопросу или завершение
    if question_index + 1 < len(carTest.questions):
        await message.answer(carTest.questions[question_index + 1]["question"],
                                      reply_markup=reply_keyboards.get_keyboard(question_index + 1))
        await state.set_state(next_state)
    else:
        await bot.send_message(chat_id=admin_id1,
                               text='Юзер {}\n@{}\nЗавершил тест\n\nПравильных ответов - {}\n\nНеверно - {}'.format(users_car_test[message.from_user.id]['first_name'],
                                                                                                              users_car_test[message.from_user.id]['username'],
                                                                                                              users_car_test[message.from_user.id]['correct_answers'],
                                                                                                                 users_car_test[
                                                                                                                     message.from_user.id][
                                                                                                                     'incorrect_answers'] ))
        if users_car_test[message.from_user.id]['correct_answers'] > 8:
            await message.answer("Поздравляю вы хорошо усвоили материал!\n\n"
                                          "Теперь можете переходить к следующему уроку.",
                                 reply_markup=inline_keyboards.next_lesson_2())

        else:
            await message.answer('Некоторые ответы были неверные.\n'
                                          'Для перехода к следующему уроку необходимо понять предыдущую тему и пройти тест еще раз.',
                                          reply_markup=inline_keyboards.send_video_osmotr())
        await state.clear()


# Обработчики для каждого вопроса
@router.message(QuizStates.Q1)
async def question_1(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question_index = data.get("question_index", 0)
    await handle_answer(message, state, question_index, QuizStates.Q2, bot)


@router.message(QuizStates.Q2)
async def question_2(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question_index = data.get("question_index", 1)
    await handle_answer(message, state, question_index, QuizStates.Q3, bot)


@router.message(QuizStates.Q3)
async def question_3(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question_index = data.get("question_index", 2)
    await handle_answer(message, state, question_index, QuizStates.Q4, bot)


@router.message(QuizStates.Q4)
async def question_4(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question_index = data.get("question_index", 3)
    await handle_answer(message, state, question_index, QuizStates.Q5, bot)


@router.message(QuizStates.Q5)
async def question_5(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question_index = data.get("question_index", 4)
    await handle_answer(message, state, question_index, QuizStates.Q6, bot)


@router.message(QuizStates.Q6)
async def question_6(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question_index = data.get("question_index", 5)
    await handle_answer(message, state, question_index, QuizStates.Q7, bot)


@router.message(QuizStates.Q7)
async def question_7(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question_index = data.get("question_index", 6)
    await handle_answer(message, state, question_index, QuizStates.Q8, bot)


@router.message(QuizStates.Q8)
async def question_8(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question_index = data.get("question_index", 7)
    await handle_answer(message, state, question_index, QuizStates.Q9, bot)


@router.message(QuizStates.Q9)
async def question_9(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question_index = data.get("question_index", 8)
    await handle_answer(message, state, question_index, QuizStates.Q10, bot)


@router.message(QuizStates.Q10)
async def question_10(message: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    question_index = data.get("question_index", 9)
    await handle_answer(message, state, question_index, None, bot)


@router.callback_query(F.data == 'get_me_to_ac_exam')
async def lets_start_a_test(callback: CallbackQuery, bot: Bot):
    if sqlite_funcs.check_user_ac(callback.from_user.id):
        await callback.answer(text='Вы уже проходили тест по кондиционеру!',
                              show_alert=True)
    else:
        if sqlite_funcs.check_user(callback.from_user.id):
            sqlite_funcs.adding_users(tg_id=callback.from_user.id, name=callback.from_user.first_name)
        await bot.send_message(chat_id=admin_id,
                               text=f'Юзер начал проходить тест по кондею:'
                                    f'{callback.from_user.first_name} - Имя\n'
                                    f'Его ID - {callback.from_user.id}')
        await bot.send_message(chat_id=admin_id1,
                               text=f'Юзер начал проходить тест по кондею:'
                                    f'{callback.from_user.first_name} - Имя\n'
                                    f'Его ID - {callback.from_user.id}')
        dict_to_check_progress[callback.from_user.id] = 1
        users[callback.from_user.id] = 0
        await callback.message.answer(text='Тест нужно пройти полностью, до конца, иначе результат не зачтется\n\n'
                                           'Всего 20 вопросов и только ОДИН вариант ответа - верный\n\n'
                                           'попытка одна, не спешите\n'
                                           'Удачи!)'
                                      )
        await callback.message.answer(text='''1. Какие основные функции выполняет автокондиционер в автомобиле?\n\n
a) Охлаждение воздуха в салоне.\n
b) Увлажнение воздуха.\n
c) Очистка воздуха от пыли.\n
d) Подогрев воздуха.''',
                                      reply_markup=inline_keyboards.ac_1_answer())


@router.callback_query(F.data == 'ac-1-a')
@router.callback_query(F.data == 'ac-1-b')
@router.callback_query(F.data == 'ac-1-c')
@router.callback_query(F.data == 'ac-1-d')
async def ac_1_note(callback: CallbackQuery, bot: Bot):
    if dict_to_check_progress[callback.from_user.id] == 1:
        dict_to_check_progress[callback.from_user.id] = 2
        if callback.data == 'ac-1-a':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
        await callback.message.answer(text='''2. Какие компоненты являются частью автокондиционера?\n\n
a) Компрессор.\n
b) Испаритель.\n
c) Конденсатор.\n
d) Все вышеперечисленные.''',
                                      reply_markup=inline_keyboards.ac_2_answer()
                                      )
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-2-a')
@router.callback_query(F.data == 'ac-2-b')
@router.callback_query(F.data == 'ac-2-c')
@router.callback_query(F.data == 'ac-2-d')
async def ac_2_note(callback: CallbackQuery, bot: Bot):
    if dict_to_check_progress[callback.from_user.id] == 2:
        dict_to_check_progress[callback.from_user.id] = 3
        if callback.data == 'ac-2-d':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
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
    if dict_to_check_progress[callback.from_user.id] == 3:
        dict_to_check_progress[callback.from_user.id] = 4
        if callback.data == 'ac-3-b':
            await callback.message.answer(text='Верно!')
            users[callback.from_user.id] += 5
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
    if dict_to_check_progress[callback.from_user.id] == 4:
        dict_to_check_progress[callback.from_user.id] = 5
        if callback.data == 'ac-4-b' or callback.data == 'ac-4-c':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
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
    if dict_to_check_progress[callback.from_user.id] == 5:
        dict_to_check_progress[callback.from_user.id] = 6
        if callback.data == 'ac-5-d':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
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
    if dict_to_check_progress[callback.from_user.id] == 6:
        dict_to_check_progress[callback.from_user.id] = 7
        if callback.data == 'ac-6-b':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
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
    if dict_to_check_progress[callback.from_user.id] == 7:
        dict_to_check_progress[callback.from_user.id] = 8
        if callback.data == 'ac-7-c':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
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
    if dict_to_check_progress[callback.from_user.id] == 8:
        dict_to_check_progress[callback.from_user.id] = 9
        if callback.data == 'ac-8-d':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
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
    if dict_to_check_progress[callback.from_user.id] == 9:
        dict_to_check_progress[callback.from_user.id] = 10
        if callback.data == 'ac-9-c':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
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
    if dict_to_check_progress[callback.from_user.id] == 10:
        dict_to_check_progress[callback.from_user.id] = 11
        if callback.data == 'ac-10-d':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
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
    if dict_to_check_progress[callback.from_user.id] == 11:
        dict_to_check_progress[callback.from_user.id] = 12
        if callback.data == 'ac-11-c':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
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
    if dict_to_check_progress[callback.from_user.id] == 12:
        dict_to_check_progress[callback.from_user.id] = 13
        if callback.data == 'ac-12-c':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
        await callback.message.answer(text='''13. Какие методы ремонта трубок существуют?\n\n
а) Замена на шланг\n
b) Вставка\n
c) Ремонт фланца\n
d) Все вышеперечисленные''', reply_markup=inline_keyboards.ac_13_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-13-a')
@router.callback_query(F.data == 'ac-13-b')
@router.callback_query(F.data == 'ac-13-c')
@router.callback_query(F.data == 'ac-13-d')
async def ac_13_note(callback: CallbackQuery, bot: Bot):
    if dict_to_check_progress[callback.from_user.id] == 13:
        dict_to_check_progress[callback.from_user.id] = 14
        if callback.data == 'ac-13-d':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
        await callback.message.answer(text='''14. Какая должна быть температура воздуха из кондиционера после его заправки?\n\n
a) 10 градусов Цельсия.\n
b) 18 градусов Цельсия.\n
c) 25 градусов Цельсия.\n
d) 30 градусов Цельсия.''', reply_markup=inline_keyboards.ac_14_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-14-a')
@router.callback_query(F.data == 'ac-14-b')
@router.callback_query(F.data == 'ac-14-c')
@router.callback_query(F.data == 'ac-14-d')
async def ac_14_note(callback: CallbackQuery, bot: Bot):
    if dict_to_check_progress[callback.from_user.id] == 14:
        dict_to_check_progress[callback.from_user.id] = 15
        if callback.data == 'ac-14-a':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
        await callback.message.answer(text='''15. Сколько занимает процедура диагностирования автокондиционера?\n\n
a) От 1 до 2 дней.\n
b) 23 часа.\n
c) 30–60 минут.\n
d) Не более 5 минут.''', reply_markup=inline_keyboards.ac_15_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-15-a')
@router.callback_query(F.data == 'ac-15-b')
@router.callback_query(F.data == 'ac-15-c')
@router.callback_query(F.data == 'ac-15-d')
async def ac_15_note(callback: CallbackQuery, bot: Bot):
    if dict_to_check_progress[callback.from_user.id] == 15:
        dict_to_check_progress[callback.from_user.id] = 16
        if callback.data == 'ac-15-c':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
        await callback.message.answer(text='''16. Сколько масла должно быть в системе автокондиционирования?\n\n
a) 50-100 мл.\n
b) 130-250 мл.\n
c) 300 мл.\n
d) 400 мл.''', reply_markup=inline_keyboards.ac_16_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-16-a')
@router.callback_query(F.data == 'ac-16-b')
@router.callback_query(F.data == 'ac-16-c')
@router.callback_query(F.data == 'ac-16-d')
async def ac_16_note(callback: CallbackQuery, bot: Bot):
    if dict_to_check_progress[callback.from_user.id] == 16:
        dict_to_check_progress[callback.from_user.id] = 17
        if callback.data == 'ac-16-b':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
        await callback.message.answer(text='''17. Что происходит с хладагентом в рабочем цикле автокондиционера, выбрать верное утверждение?\n\n
a) Сжимается и испаряется.\n
b) Испаряется и конденсируется.\n
c) Охлаждается и снова сжимается.\n
d) Нагревается и замерзает.''', reply_markup=inline_keyboards.ac_17_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-17-a')
@router.callback_query(F.data == 'ac-17-b')
@router.callback_query(F.data == 'ac-17-c')
@router.callback_query(F.data == 'ac-17-d')
async def ac_17_note(callback: CallbackQuery, bot: Bot):
    if dict_to_check_progress[callback.from_user.id] == 17:
        dict_to_check_progress[callback.from_user.id] = 18
        if callback.data == 'ac-17-b':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
        await callback.message.answer(text='''18. Для определения утечек хладагента используется:\n\n
a) Молькотлитель.\n
b) Детектор лжи.\n
c) Клаксон.\n
d) Детектор утечки.''', reply_markup=inline_keyboards.ac_18_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-18-a')
@router.callback_query(F.data == 'ac-18-b')
@router.callback_query(F.data == 'ac-18-c')
@router.callback_query(F.data == 'ac-18-d')
async def ac_18_note(callback: CallbackQuery, bot: Bot):
    if dict_to_check_progress[callback.from_user.id] == 18:
        dict_to_check_progress[callback.from_user.id] = 19
        if callback.data == 'ac-18-d':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
        await callback.message.answer(text='''19. Можно ли смешивать данные масла PAG и POE?\n\n
a) Можно.\n
b) Нельзя.\n
c) Можно, если добавить краску.\n
d) Всегда смешивал и ничего.''', reply_markup=inline_keyboards.ac_19_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-19-a')
@router.callback_query(F.data == 'ac-19-b')
@router.callback_query(F.data == 'ac-19-c')
@router.callback_query(F.data == 'ac-19-d')
async def ac_19_note(callback: CallbackQuery, bot: Bot):
    if dict_to_check_progress[callback.from_user.id] == 19:
        dict_to_check_progress[callback.from_user.id] = 20
        if callback.data == 'ac-19-b':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
        await callback.message.answer(text='''20. Какие могут быть основные причины повреждений трубок системы кондиционирования автомобиля?\n\n
a) Механические повреждения, коррозия, неправильная эксплуатация.\n
b) Перегрев двигателя, низкий уровень масла.\n
c) Неправильная работа выхлопной системы.\n
d) Все вышеперечисленное.''', reply_markup=inline_keyboards.ac_20_answer())
    else:
        await callback.message.answer(text='На вопрос можно ответить только ОДИН раз!')


@router.callback_query(F.data == 'ac-20-a')
@router.callback_query(F.data == 'ac-20-b')
@router.callback_query(F.data == 'ac-20-c')
@router.callback_query(F.data == 'ac-20-d')
async def ac_20_note(callback: CallbackQuery, bot: Bot):
    if dict_to_check_progress[callback.from_user.id] == 20:
        dict_to_check_progress[callback.from_user.id] = 21
        if callback.data == 'ac-20-a':
            await bot.send_message(text='Верно!', chat_id=callback.from_user.id)
            users[callback.from_user.id] += 5
        await callback.message.answer(
            text=f'Поздравляю! Вы прошли тест, результат - {users[callback.from_user.id]} баллов')
        sqlite_funcs.change_opportunity_for_ac_test(callback.from_user.id)
        await bot.send_message(
            text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{users[callback.from_user.id]} баллов',
            chat_id=admin_id)
        await bot.send_message(
            text=f'{callback.from_user.first_name} - прошел тест, его результат:\n{users[callback.from_user.id]} баллов',
            chat_id=admin_id1)
        sqlite_funcs.get_finished_with_ac(callback.from_user.id)
        users[callback.from_user.id] = 0


@router.message(F.text == 'ПСП')
async def show_users(message: Message):
    users_to_show = sqlite_funcs.import_users()
    await message.answer(text='Вот список юзеров:\n')
    for elem in users_to_show:
        await message.answer(f'{elem}')


@router.message(F.text.startswith('Измени кондей тест у юзера:'))
async def change_opportunity_ac(message: Message):
    sqlite_funcs.change_opportunity_for_ac_test(message.text[28::])
    await message.answer(text='Обнулили тест для данного Юзера')


@router.message(F.text)
async def any_text(message: Message):
    await message.answer(text='Я вас не понимаю...\n\nВывожу главное меню:',
                         reply_markup=reply_keyboards.choose_course())
