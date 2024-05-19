from aiogram import types
from aiogram.fsm.context import FSMContext
from icecream import ic
from aiogram.filters import  CommandObject
from aiogram import Bot, types
from aiogram.utils.deep_linking import create_start_link, decode_payload
from aiogram import types
from aiogram.types import FSInputFile, URLInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup ### Default imports ###
from aiogram.fsm.state import StatesGroup, State

def start_keyboard(): # Inline keyboard
   keyboard = InlineKeyboardBuilder()
   keyboard.row(InlineKeyboardButton(text='Наш Сайт', url="https://wbsecurity.ru/"), InlineKeyboardButton(text='Услуги', callback_data='uslugi')) # 1(-ые) кнопки
   keyboard.add(InlineKeyboardButton(text='О Нас', callback_data='aboutus')) # 2 кнопка
   keyboard.adjust(2) # Кнопок в ряд
   return keyboard.as_markup()

def escape_keyboard(): # Inline keyboard
   keyboard = InlineKeyboardBuilder()
   keyboard.add(InlineKeyboardButton(text='Назад', callback_data='back')) # 2 кнопка
   keyboard.adjust(1) # Кнопок в ряд
   return keyboard.as_markup()

bot = Bot(token="6856429419:AAEDFkJIwtKq4AQdq7I68mqgiR8uAN8WXFw", parse_mode='HTML')

### Подгрузка изображений ###
image1 = URLInputFile("https://wbsecurity.ru/main1.jpg",filename="WBS-image.jpg");print("Загруженно 1/5");image2 = URLInputFile("https://wbsecurity.ru/DDos.jpg",filename="WBS-image.jpg");print("Загруженно 2/5");image3 = URLInputFile("https://wbsecurity.ru/server.jpg",filename="WBS-image.jpg");print("Загруженно 3/5");image4 = URLInputFile("https://wbsecurity.ru/Site.jpg",filename="WBS-image.jpg");print("Загруженно 4/5");image5 = URLInputFile("https://wbsecurity.ru/sql-injection.jpg",filename="WBS-image.jpg");print("Загруженно 5/5");image6 = URLInputFile("https://wbsecurity.ru/aboutus.jpg",filename="WBS-image.jpg")

admins = [1326089018, 1028676957, 1103300480]

async def start_command(message: types.Message, command: CommandObject):
    user_id = message.from_user.id
    args = command.args

    if args == None:
        await bot.send_photo(user_id, photo=image1, caption="Добро пожаловать в наш Telegram бот! 🚀\n\nМы рады видеть вас здесь и готовы помочь вам с Защитой Вашего WEB-Сайта.\n\nНаша команда предоставляет инновационные решения, обеспечивая максимальную безопасность и спокойствие. 🔒\n\n Начните пользоваться нашим сервисом прямо сейчас, чтобы забыть о киберугрозах.\n\n Нажмите на кнопку ниже, чтобы узнать больше и получить доступ к эксклюзивным возможностям. 🎉\n\n Мы всегда на связи и готовы ответить на все ваши вопросы!", reply_markup=start_keyboard())
    
    if args != None:
        reference = decode_payload(args)
        await bot.send_photo(user_id, photo=image1, caption="Добро пожаловать в наш Telegram бот! 🚀\n\nМы рады видеть вас здесь и готовы помочь вам с Защитой Вашего WEB-Сайта.\n\nНаша команда предоставляет инновационные решения, обеспечивая максимальную безопасность и спокойствие. 🔒\n\n Начните пользоваться нашим сервисом прямо сейчас, чтобы забыть о киберугрозах.\n\n Нажмите на кнопку ниже, чтобы узнать больше и получить доступ к эксклюзивным возможностям. 🎉\n\n Мы всегда на связи и готовы ответить на все ваши вопросы!", reply_markup=start_keyboard())

async def start_command(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    
    await bot.send_photo(user_id, photo=image1, caption="Добро пожаловать в наш Telegram бот! 🚀\n\nМы рады видеть вас здесь и готовы помочь вам с Защитой Вашего WEB-Сайта.\n\nНаша команда предоставляет инновационные решения, обеспечивая максимальную безопасность и спокойствие. 🔒\n\n Начните пользоваться нашим сервисом прямо сейчас, чтобы забыть о киберугрозах.\n\n Нажмите на кнопку ниже, чтобы узнать больше и получить доступ к эксклюзивным возможностям. 🎉\n\n Мы всегда на связи и готовы ответить на все ваши вопросы!", reply_markup=start_keyboard())


async def aboutus(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    
    
    await bot.send_photo(user_id, photo=image6, caption="🔒 Web-Sites Security (WBS) — это команда талантливых энтузиастов с огромной страстью к кибербезопасности и защите веб-сайтов 🌐.\n\n 🏆 Наше увлечение проявляется через участие в соревнованиях CTF (Capture The Flag), где требуются глубокие знания в сфере кибербезопасности 🛡️.", reply_markup=escape_keyboard())

async def uslugi(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    user = callback_query.from_user
    
    for i in range(len(admins)):
        await bot.send_message(admins[i], f"🚀 Кто-то заинтересовался услугами! 🖥️ @{user.username}\n\n Его звать: {user.first_name}")
        await bot.send_message(admins[i], f"{user_id}")
    
    await bot.send_photo(user_id, photo=image4, caption="🔒 Мы предлагаем услуги по созданию сайтов и обеспечению их безопасности 🌐.\n\n✨ Наши специалисты разработают для вас современный и надежный сайт, а также внедрят все необходимые меры защиты от кибератак 🛡️.")
    await bot.send_photo(user_id, photo=image3, caption="🖥️ Мы предлагаем услуги по защите серверов и баз данных 🔐.\n\n📊 Наши эксперты обеспечат надежную защиту ваших данных от киберугроз и взломов 🛡️.")
    await bot.send_photo(user_id, photo=image2, caption="🌐 Мы предлагаем услуги защиты от DDoS атак, чтобы ваш сайт всегда оставался доступным 🛡️.\n\n🚀 Наши технологии и эксперты обеспечат надежную защиту от любых попыток перегрузки вашего сервера 🔒.")
    await bot.send_photo(user_id, photo=image5, caption="🔐 Наша услуга защиты от SQL Injection предотвращает несанкционированный доступ к вашим данным и обеспечивает безопасность базы данных. 💪\n\n🖥️ Мы используем передовые методы анализа и фильтрации запросов, чтобы защитить ваш сайт от атак. 🛡️\n\n💼 Доверьте нам вашу онлайн-защиту, чтобы быть спокойными за безопасность вашего ресурса ✨.", reply_markup=escape_keyboard())

async def get_ref(message: types.Message):
  link = await create_start_link(bot, "uslygi", encode=True)
  await message.answer(f"Ваша реф. ссылка {link}")