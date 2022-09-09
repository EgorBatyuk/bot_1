import logging

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


API_TOKEN = '1699414442:AAHrZuZ_4fIr82Vw_aZisINxZjzyslHr2h4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def p(message: types.Message):
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = KeyboardButton('Проецирование')
    button2 = KeyboardButton("Виды проецирования")
    button3 = KeyboardButton("Прямоугольное проецирование")
    button4 = KeyboardButton("Проецирование точки")
    button5 = KeyboardButton("Проецирование отрезка")
    button6 = KeyboardButton("Проецирование плоского предмета")
    button7 = KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4, button5, button6, button7)
    await message.answer("Ваш выбор:", reply_markup=keyboard)


async def form_projection(message):
    await bot.send_message(message.chat.id, 'Проецирование — процесс получения изображения предметов наплоскости с помощью '
                                      'проецирующих лучей.')
    await bot.send_message(message.chat.id, 'Элементы проецирования:\n'
                                      '\n'
                                      '1) Центр проецирования — точка, из которой производится проецирование.\n'
                                      '\n'
                                      '2) Объект проецирования — изображаемый предмет.\n'
                                      '\n'
                                      '3) Плоскость проекции — плоскость, на которую производится проецирование.\n'
                                      '\n'
                                      '4) Проецирующие лучи — воображаемые прямые, с помощью которыхпроизводится п'
                                      'роецирование.\n'
                                      '\n'
                                      '5) Проекция — изображение объекта на плоскости, образованное мето-дом проецирования.')

    file = open('img/ghjtrwbz.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def types_of_projection(message):

    file = open('img/dbls_ghjtrwbq.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def rectangular_projection(message):

    file = open('img/ghzvjeujkmyjt_ghjtwbhjdfybt.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def point_design(message):
    file = open('img/njxrf.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def line_projection(message):
    file = open('img/ghjtrwbz_jnhtprf.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def flat_object(message):
    file = open('img/ploskau_proek.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def projection_2(message):
    file = open('img/gjcnhjtybt_lde[ghjtrwbjy.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    file = open('img/nt[yjkjubz.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def projection_3(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Разъяснение о плоскостях проекции')
    button2 = types.KeyboardButton("Проецирование на три плоскости проекций")
    button3 = types.KeyboardButton("Построение третьей проекции")
    button4 = types.KeyboardButton("Построение трёхпроекционного чертежа точки")
    button5 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4, button5)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def clarification(message):

    file = open('img/nt[yjkjubz_1.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def flat_3(message):

    file = open('img/ghjtwbhjdfybt_2.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def build_3(message):

    file = open('img/nt[yjkjubz_gjcnhjtybz_2.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def building_3_p(message):

    file = open('img/gjcnhjtybt_2.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def types_drawing(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Теория')
    button2 = types.KeyboardButton("Основные плоскости проекций")
    button3 = types.KeyboardButton("Комплексный чертёж. Образование комплексного чертежа")
    button4 = types.KeyboardButton("Условности и упрощения на чертежах")
    button5 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4, button5)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def theory(message):
    await bot.send_message(message.chat.id, 'Вид — изображение обращенной к наблюдателю видимой части поверхности предмета.')
    await bot.send_message(message.chat.id, 'Комплексный чертеж — изображение предмета на совмещенных плоскостях проекций.')


async def general_flat(message):

    file = open('img/general_flat1.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def complex(message):

    file = open('img/complex1.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    file = open('img/complex2.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def ifing(message):

    file = open('img/ifing.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def projection_g(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Теория проекции')
    button2 = types.KeyboardButton("Правила проецирования рёбер и граней")
    button3 = types.KeyboardButton("Проецирование цилиндра")
    button4 = types.KeyboardButton("Проецирование призмы")
    button5 = types.KeyboardButton("Проецирование конуса")
    button6 = types.KeyboardButton("Проецирование пирамиды")
    button7 = types.KeyboardButton("Правила проецирования ребер и граней")
    button8 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def theory1(message):
    await bot.send_message(message.chat.id, 'Многогранники — геометрические тела, поверхность которых состоит из конечного '
                                      'числа многоугольников.')
    await bot.send_message(message.chat.id, 'Тела вращения — геометрические тела, образованные вращением плоской '
                                      'геометрической фигуры или ее части вокруг оси.')
    await bot.send_message(message.chat.id, 'Призма — многогранник, имеющий два основания (равные и параллельные '
                                      'многоугольники) и боковые грани (четырехугольники).')
    file = open('img/prism.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Куб — многогранник, ограниченный шестью квадратами, или правильная прямая '
                                      'четырехугольная призма, в основании которой лежит квадрат.')
    await bot.send_message(message.chat.id, 'Пирамида — многогранник, у которогооснование является многоугольником, а боковые'
                                      ' грани представлены треугольниками, имеющими общую вершину.')

    file = open('img/pyramid.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Конус — тело вращения, образованное вращением прямоугольного треугольника вокруг'
                                      ' оси, совмещенной с одним из его катетов.')
    await bot.send_message(message.chat.id, 'Цилиндр — тело вращения, образованное вращениемпрямоугольника вокруг оси, '
                                      'совмещенной с одной из его сторон.')


async def general_tabl(message):

    file = open('img/tabl.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def prizma(message):

    file = open('img/prizma_1.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def cylinder(message):

    file = open('img/cylinder.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def conys(message):

    file = open('img/cone.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def pyromid(message):

    file = open('img/pyramid_1.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def general1(message):

    file = open('img/general1.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def general10(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Проецирование точек на поверхности цилиндра')
    button2 = types.KeyboardButton("Проецирование точек на поверхности призмы")
    button3 = types.KeyboardButton("Проецирование точек на поверхности пирамиды")
    button5 = types.KeyboardButton("Проецирование точек на поверхности конуса")
    button6 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button5, button6)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def p_cylinder(message):

    file = open('img/projection_point_on_cylinder.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p_prizm(message):

    file = open('img/projection_point_on_prizm.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p_pyramid(message):

    file = open('img/pyramid11.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    file = open('img/pyramid12.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def p_conys(message):

    file = open('img/conys11.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def general_poloj(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Теория аксонометрического проекции')
    button2 = types.KeyboardButton("Виды аксонометрических проекций")
    button3 = types.KeyboardButton("Коэффициент искажения")
    button4 = types.KeyboardButton("Способы построения аксонометрических осей")
    button5 = types.KeyboardButton("Правила построения аксонометрических проекций")
    button6 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3, button4, button5, button6)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def o_theory(message):

    await bot.send_message(message.chat.id, 'Аксонометрическая проекция — это изображение, полученное припараллельном '
                                      'проецировании предмета вместе с осями прямоугольных координат на произвольную '
                                      'плоскость.')

    file = open('img/input.png', 'rb')
    await bot.send_photo(message.chat.id, file)

    await bot.send_message(message.chat.id, 'Коэффициент искажения (k) — отношение аксонометрической единицы измерения к натуральной.')


async def version_projection(message):

    file = open('img/view_projection.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def o_coef(message):

    file = open('img/coefficient.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def o_way(message):

    file = open('img/way_axes.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def o_law(message):

    file = open('img/law_build.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def build_projection_11(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Теория плоских фигур и окружностей')
    button2 = types.KeyboardButton("Построение аксонометрических проекций квадрата")
    button3 = types.KeyboardButton("Построение аксонометрических проекций плоских фигур")
    button4 = types.KeyboardButton("Общее построение аксонометрической проекции окружности")
    button5 = types.KeyboardButton("Построение фронтальной и профильной проекций окружности")
    button6 = types.KeyboardButton('На главную')
    keyboard.add(button1, button2, button3, button4, button5, button6)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def f_theory(message):
    await bot.send_message(message.chat.id, 'Плоская фигура — фигура, все точки которой находятся в одной плоскости.')
    await bot.send_message(message.chat.id, 'Овал — замкнутая кривая, состоящаяиз четырех дуг окружностей, плавно переходящих'
                                      ' друг в друга')


async def f_build(message):

    file = open('img/build_r.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def f_build_flat(message):

    file = open('img/build_flat.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def f_our_build(message):

    file = open('img/general_building.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def f_law_building(message):

    file = open('img/build_f_f_projection.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def aa_projection(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Аксонометрические проекции многогранников')
    button2 = types.KeyboardButton("Аксонометрические проекции поверхностей вращения")
    button3 = types.KeyboardButton('На главную')
    keyboard.add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def f_1(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Прямоугольная изометрическая проекция призмы')
    button2 = types.KeyboardButton("Прямоугольная изометрическая проекция пирамиды")
    button3 = types.KeyboardButton('На главную')
    keyboard.add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def f_11(message):

    file = open('img/rectangular_isometry_prizm.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def f_12(message):

    file = open('img/rectangular_isometry_pyramid.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def f_2(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Прямоугольная изометрическая проекция цилиндра')
    button2 = types.KeyboardButton("Прямоугольная изометрическая проекция конуса")
    button3 = types.KeyboardButton("На главную")
    keyboard.add(button1, button2, button3)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def f_21(message):

    file = open('img/rectangular_isometry_cone.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def f_22(message):

    file = open('img/rectangular_isometry_cylinder.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def technical_pain(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Теория технического рисунка')
    button2 = types.KeyboardButton("Правила выполнения технического рисунка")
    button3 = types.KeyboardButton("Выявление объема предмета на техническом рисунке детали")
    button4 = types.KeyboardButton("Общее построение аксонометрической проекции окружности")
    button5 = types.KeyboardButton("Построение фронтальной и профильной проекций окружности")
    button6 = types.KeyboardButton('На главную')
    keyboard.add(button1, button2, button3, button4, button5, button6)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def t_theory(message):
    await bot.send_message(message.chat.id, 'Технический рисунок — это наглядное графическое изображение объекта, выполненное'
                                      ' от руки на глаз с соблюдением его конструктивной формы и размеров')
    await bot.send_message(message.chat.id, 'Необходимо учитывать пропорции')
    await bot.send_message(message.chat.id, 'Светотень — это распределение света на поверхностях предмета.\n'
                                      'Способствует восприятию объемной формы предмета')
    await bot.send_message(message.chat.id, 'Штриховка — это наиболее распространенный способ оттенения изо-бражения сплошными параллельными линиями различной толщины')
    await bot.send_message(message.chat.id, 'Шраффировка. Это штриховка в виде сетки, или двойной штриховки. \n'
                                      'Шраффировку наносят на многогранниках и поверхностях вращения аналогично штриховке, '
                                      'учитывая форму предмета')


async def law_print(message):

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = types.KeyboardButton('Правила выполнения')
    button2 = types.KeyboardButton("Построение технического рисунка квадрата")
    button3 = types.KeyboardButton("Построение квадрата в прямоугольной изометрии")
    button4 = types.KeyboardButton("Построение технического рисунка окружностей")
    button5 = types.KeyboardButton("Построение технического рисунка куба")
    button6 = types.KeyboardButton('На главную')
    keyboard.add(button1, button2, button3, button4, button5, button6)
    await bot.send_message(message.chat.id, "Ваш выбор:", reply_markup=keyboard)


async def law_do(message):

    file = open('img/law_do.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def reqtangl(message):

    file = open('img/requngle12.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def circle(message):

    file = open('img/circle.png', 'rb')
    await bot.send_photo(message.chat.id, file)


async def cube(message):

    file = open('img/build_cube.png', 'rb')
    await bot.send_photo(message.chat.id, file)













