from aiogram.dispatcher.filters import Text

from handlers import *

API_TOKEN = '1699414442:AAHrZuZ_4fIr82Vw_aZisINxZjzyslHr2h4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def any_msg(message):
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = KeyboardButton('Проецирование формы предметаю Прямоугольное проецирование на одну плоскость проекций')
    button2 = KeyboardButton("Прямоугольное проецирование на две плоскости проекций")
    button3 = KeyboardButton("Прямоугольное проецирование на три плоскости проекций")
    button4 = KeyboardButton("Виды чертежа. Расположение видов на чертеже")
    button5 = KeyboardButton("Проекции геометрических тел на чертежах")
    button6 = KeyboardButton("Проекции точек на поверхностях геометрических тел")
    button7 = KeyboardButton("Основные положения аксонометрического проецирования")
    button8 = KeyboardButton("Построение аксонометрических проекций плоских фигур и окружностей")
    button9 = KeyboardButton("Аксонометрические проекции геометрических тел. Нахождение точек, лежащих на "
                             "поверхности геометрических тел")
    button10 = KeyboardButton("Технический рисунок")
    keyboard.add(button1, button2, button3, button4, button5,
                 button6, button7, button8, button9, button10)
    await message.answer('Ваш выбор:', reply_markup=keyboard)
    await message.answer(message.text)


@dp.message_handler(Text(equals="qaz"))
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")


@dp.message_handler(Text(equals="Проецирование формы предметаю Прямоугольное проецирование на одну плоскость проекций"))
async def with_puree(message: types.Message):
    await p(message)

    # if message.text == 'Проецирование формы предметаю Прямоугольное проецирование на одну плоскость проекций':
    #     await p(message)


@dp.message_handler(Text(equals="Проецирование"))
async def with_puree(message: types.Message):
    await form_projection(message)


# if message.text == 'Проецирование':
#     form_projection(message)

@dp.message_handler(Text(equals="Виды проецирования"))
async def with_puree(message: types.Message):
    await types_of_projection(message)

    # if message.text == 'Виды проецирования':
    #     types_of_projection(message)


@dp.message_handler(Text(equals="Прямоугольное проецирование"))
async def with_puree(message: types.Message):
    await rectangular_projection(message)

    # if message.text == 'Прямоугольное проецирование':
    #     rectangular_projection(message)


@dp.message_handler(Text(equals="Проецирование точки"))
async def with_puree(message: types.Message):
    await point_design(message)

    # if message.text == 'Проецирование точки':
    #     point_design(message)


@dp.message_handler(Text(equals="Проецирование отрезка"))
async def with_puree(message: types.Message):
    await line_projection(message)

    # if message.text == 'Проецирование отрезка':
    #     line_projection(message)


@dp.message_handler(Text(equals="Проецирование плоского предмета"))
async def with_puree(message: types.Message):
    await flat_object(message)

    # if message.text == 'Проецирование плоского предмета':
    #     flat_object(message)


@dp.message_handler(Text(equals="Прямоугольное проецирование на две плоскости проекций"))
async def with_puree(message: types.Message):
    await projection_2(message)

    # if message.text == 'Прямоугольное проецирование на две плоскости проекций':
    #     projection_2(message)


@dp.message_handler(Text(equals="Прямоугольное проецирование на три плоскости проекций"))
async def with_puree(message: types.Message):
    await projection_3(message)

    # if message.text == 'Прямоугольное проецирование на три плоскости проекций':
    #     projection_3(message)


@dp.message_handler(Text(equals="Разъяснение о плоскостях проекции"))
async def with_puree(message: types.Message):
    await clarification(message)

    # if message.text == 'Разъяснение о плоскостях проекции':
    #     clarification(message)


@dp.message_handler(Text(equals="Проецирование на три плоскости проекций"))
async def with_puree(message: types.Message):
    await flat_3(message)

    # if message.text == 'Проецирование на три плоскости проекций':
    #     flat_3(message)


@dp.message_handler(Text(equals="Построение третьей проекции"))
async def with_puree(message: types.Message):
    await build_3(message)

    # if message.text == 'Построение третьей проекции':
    #     build_3(message)


@dp.message_handler(Text(equals="Построение трёхпроекционного чертежа точки"))
async def with_puree(message: types.Message):
    await building_3_p(message)

    # if message.text == 'Построение трёхпроекционного чертежа точки':
    #     building_3_p(message)


@dp.message_handler(Text(equals="Виды чертежа. Расположение видов на чертеже"))
async def with_puree(message: types.Message):
    await types_drawing(message)

    # if message.text == 'Виды чертежа. Расположение видов на чертеже':
    #     types_drawing(message)


@dp.message_handler(Text(equals="Теория"))
async def with_puree(message: types.Message):
    await theory(message)

    # if message.text == 'Теория':
    #     theory(message)


@dp.message_handler(Text(equals="Основные плоскости проекций"))
async def with_puree(message: types.Message):
    await general_flat(message)

    # if message.text == 'Основные плоскости проекций':
    #     general_flat(message)


@dp.message_handler(Text(equals="Комплексный чертёж. Образование комплексного чертежа"))
async def with_puree(message: types.Message):
    await complex(message)

    # if message.text == 'Комплексный чертёж. Образование комплексного чертежа':
    #     complex(message)


@dp.message_handler(Text(equals="Условности и упрощения на чертежах"))
async def with_puree(message: types.Message):
    await ifing(message)


# if message.text == 'Условности и упрощения на чертежах':
#     ifing(message)
@dp.message_handler(Text(equals="Проекции геометрических тел на чертежах"))
async def with_puree(message: types.Message):
    await projection_g(message)

    # if message.text == 'Проекции геометрических тел на чертежах':
    #     projection_g(message)


@dp.message_handler(Text(equals="Теория проекции"))
async def with_puree(message: types.Message):
    await theory1(message)

    # if message.text == 'Теория проекции':
    #     theory1(message)


@dp.message_handler(Text(equals="Правила проецирования рёбер и граней"))
async def with_puree(message: types.Message):
    await general_tabl(message)

    # if message.text == 'Правила проецирования рёбер и граней':
    #     general_tabl(message)


@dp.message_handler(Text(equals="Проецирование цилиндра"))
async def with_puree(message: types.Message):
    await cylinder(message)

    # if message.text == 'Проецирование цилиндра':
    #     cylinder(message)


@dp.message_handler(Text(equals="Проецирование призмы"))
async def with_puree(message: types.Message):
    await prizma(message)

    # if message.text == 'Проецирование призмы':
    #     prizma(message)


@dp.message_handler(Text(equals="Проецирование конуса"))
async def with_puree(message: types.Message):
    await conys(message)

    # if message.text == 'Проецирование конуса':
    #     conys(message)


@dp.message_handler(Text(equals="Проецирование пирамиды"))
async def with_puree(message: types.Message):
    await pyromid(message)

    # if message.text == 'Проецирование пирамиды':
    #     pyromid(message)


@dp.message_handler(Text(equals="Правила проецирования ребер и граней"))
async def with_puree(message: types.Message):
    await general1(message)

    # if message.text == 'Правила проецирования ребер и граней':
    #     general1(message)


@dp.message_handler(Text(equals="Проекции точек на поверхностях геометрических тел"))
async def with_puree(message: types.Message):
    await general10(message)

    # if message.text == 'Проекции точек на поверхностях геометрических тел':
    #     general10(message)


@dp.message_handler(Text(equals="Проецирование точек на поверхности цилиндра"))
async def with_puree(message: types.Message):
    await p_cylinder(message)

    # if message.text == 'Проецирование точек на поверхности цилиндра':
    #     p_cylinder(message)


@dp.message_handler(Text(equals="Проецирование точек на поверхности призмы"))
async def with_puree(message: types.Message):
    await p_prizm(message)

    # if message.text == 'Проецирование точек на поверхности призмы':
    #     p_prizm(message)


@dp.message_handler(Text(equals="Проецирование точек на поверхности пирамиды"))
async def with_puree(message: types.Message):
    await p_pyramid(message)

    # if message.text == 'Проецирование точек на поверхности пирамиды':
    #     p_pyramid(message)


@dp.message_handler(Text(equals="Проецирование точек на поверхности конуса"))
async def with_puree(message: types.Message):
    await p_conys(message)

    # if message.text == 'Проецирование точек на поверхности конуса':
    #     p_conys(message)


@dp.message_handler(Text(equals="Основные положения аксонометрического проецирования"))
async def with_puree(message: types.Message):
    await general_poloj(message)

    # if message.text == 'Основные положения аксонометрического проецирования':
    #     general_poloj(message)


@dp.message_handler(Text(equals="Теория аксонометрического проекции"))
async def with_puree(message: types.Message):
    await o_theory(message)

    # if message.text == 'Теория аксонометрического проекции':
    #     o_theory(message)


@dp.message_handler(Text(equals="Виды аксонометрических проекций"))
async def with_puree(message: types.Message):
    await version_projection(message)

    # if message.text == 'Виды аксонометрических проекций':
    #     version_projection(message)


@dp.message_handler(Text(equals="Коэффициент искажения"))
async def with_puree(message: types.Message):
    await o_coef(message)

    # if message.text == 'Коэффициент искажения':
    #     o_coef(message)


@dp.message_handler(Text(equals="Способы построения аксонометрических осей"))
async def with_puree(message: types.Message):
    await o_way(message)

    # if message.text == 'Способы построения аксонометрических осей':
    #     o_way(message)


@dp.message_handler(Text(equals="Правила построения аксонометрических проекций"))
async def with_puree(message: types.Message):
    await o_law(message)

    # if message.text == 'Правила построения аксонометрических проекций':
    #     o_law(message)


@dp.message_handler(Text(equals="Построение аксонометрических проекций плоских фигур и окружностей"))
async def with_puree(message: types.Message):
    await build_projection_11(message)

    # if message.text == 'Построение аксонометрических проекций плоских фигур и окружностей':
    #     build_projection_11(message)


@dp.message_handler(Text(equals="Теория плоских фигур и окружностей"))
async def with_puree(message: types.Message):
    await f_theory(message)

    # if message.text == 'Теория плоских фигур и окружностей':
    #     f_theory(message)


@dp.message_handler(Text(equals="Построение аксонометрических проекций квадрата"))
async def with_puree(message: types.Message):
    await f_build(message)

    # if message.text == 'Построение аксонометрических проекций квадрата':
    #     f_build(message)


@dp.message_handler(Text(equals="Построение аксонометрических проекций плоских фигур"))
async def with_puree(message: types.Message):
    await f_build_flat(message)

    # if message.text == 'Построение аксонометрических проекций плоских фигур':
    #     f_build_flat(message)


@dp.message_handler(Text(equals="Общее построение аксонометрической проекции окружности"))
async def with_puree(message: types.Message):
    await f_our_build(message)

    # if message.text == 'Общее построение аксонометрической проекции окружности':
    #     f_our_build(message)


@dp.message_handler(Text(equals="Построение фронтальной и профильной проекций окружности"))
async def with_puree(message: types.Message):
    await f_law_building(message)

    # if message.text == 'Построение фронтальной и профильной проекций окружности':
    #     f_law_building(message)


@dp.message_handler(Text(
    equals="Аксонометрические проекции геометрических тел. Нахождение точек, лежащих на поверхности геометрических тел"))
async def with_puree(message: types.Message):
    await aa_projection(message)

    # if message.text == 'Аксонометрические проекции геометрических тел. Нахождение точек, лежащих на поверхности геометрических тел':
    #     aa_projection(message)


@dp.message_handler(Text(equals="Аксонометрические проекции многогранников"))
async def with_puree(message: types.Message):
    await f_1(message)

    # if message.text == 'Аксонометрические проекции многогранников':
    #     f_1(message)


@dp.message_handler(Text(equals="Аксонометрические проекции поверхностей вращения"))
async def with_puree(message: types.Message):
    await f_2(message)

    # if message.text == 'Аксонометрические проекции поверхностей вращения':
    #     f_2(message)


@dp.message_handler(Text(equals="Прямоугольная изометрическая проекция призмы"))
async def with_puree(message: types.Message):
    await f_11(message)

    # if message.text == 'Прямоугольная изометрическая проекция призмы':
    #     f_11(message)


@dp.message_handler(Text(equals="Прямоугольная изометрическая проекция пирамиды"))
async def with_puree(message: types.Message):
    await f_12(message)

    # if message.text == 'Прямоугольная изометрическая проекция пирамиды':
    #     f_12(message)


@dp.message_handler(Text(equals="Прямоугольная изометрическая проекция конуса"))
async def with_puree(message: types.Message):
    await f_21(message)

    # if message.text == 'Прямоугольная изометрическая проекция конуса':
    #     f_21(message)


@dp.message_handler(Text(equals="Прямоугольная изометрическая проекция цилиндра"))
async def with_puree(message: types.Message):
    await f_22(message)

    # if message.text == 'Прямоугольная изометрическая проекция цилиндра':
    #     f_22(message)


@dp.message_handler(Text(equals="Технический рисунок"))
async def with_puree(message: types.Message):
    await technical_pain(message)

    # if message.text == 'Технический рисунок':
    #     technical_pain(message)


@dp.message_handler(Text(equals="Теория технического рисунка"))
async def with_puree(message: types.Message):
    await t_theory(message)

    # if message.text == 'Теория технического рисунка':
    #     t_theory(message)


@dp.message_handler(Text(equals="Правила выполнения технического рисунка"))
async def with_puree(message: types.Message):
    await law_print(message)

    # if message.text == 'Правила выполнения технического рисунка':
    #     law_print(message)


@dp.message_handler(Text(equals="Правила выполнения"))
async def with_puree(message: types.Message):
    await law_do(message)

    # if message.text == 'Правила выполнения':
    #     law_do(message)

    # if message.text == 'Построение технического рисунка квадрата':
    #     reqtangl1(message)


@dp.message_handler(Text(equals="Построение технического рисунка окружностей"))
async def with_puree(message: types.Message):
    await circle(message)

    # if message.text == 'Построение технического рисунка окружностей':
    #     circle(message)


@dp.message_handler(Text(equals="Построение технического рисунка куба"))
async def with_puree(message: types.Message):
    await cube(message)

    # if message.text == 'Построение технического рисунка куба':
    #     cube(message)


@dp.message_handler(Text(equals="На главную"))
async def with_puree(message: types.Message):
    await any_msg(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
