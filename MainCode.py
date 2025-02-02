from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random as r

API_TOKEN = '6773333833:AAFsaNhdm_8RvFxcmXoPx0tJ7jH0zGlo1rQ'
text_alert = 'Напоминание'

bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Приветики!😊'),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('😁Приветствую тебя!😁', reply_markup=keyboard)

@dp.message_handler(text='Приветики!😊')
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='✨Случайный факт о Созвездии✨'),
            types.KeyboardButton(text='🛒Маркет🛒'),
            types.KeyboardButton(text='🔗Ссылки на Созвездие🔗'),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Выберите категорию:', reply_markup=keyboard)

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text= '🛒Созвездие маркет🛒', 
url= 'https://timkafm.github.io/')
urlkb.add(urlButton)

@dp.message_handler(text= '🛒Маркет🛒')
async def url_market(message: types.message):
    await message.answer('Актуальная ссылка:', reply_markup = urlkb)

urlkb_SocialMedia = InlineKeyboardMarkup(row_width=1)
urlButtonSite = InlineKeyboardButton(text = 'Сайт Созвездия',
url= 'https://kdcsozvezdie.ru/')
urlButtonVk = InlineKeyboardButton(text = 'VK Созвездия',
url= 'https://vk.com/kdcsozvezdie?ysclid=lpvw7mgvrs399712912')
urlButtonBot = InlineKeyboardButton(text='Путь Героя',
url = 'https://t.me/Way_of_hero_bot')
urlkb_SocialMedia.row(urlButtonSite,urlButtonVk,urlButtonBot)

@dp.message_handler(text = '🔗Ссылки на Созвездие🔗')
async def url_sozvezdie(message: types.message):
    await message.answer('Актуальные ссылки:', reply_markup = urlkb_SocialMedia)

@dp.message_handler(text="✨Случайный факт о Созвездии✨")
async def facts(message: types.message):
    number = r.randint(1,10)
    if number == 1:
        await message.reply('На территории дружины, есть большой стул, который построила семья, однажды проживающая в "Созвездии". Все кто хочет, может загадать желание возле него.')
    if number == 2:
        await message.reply('Изначально в "Созвездии" были только весенние и летние смены🍃')
    if number == 3:
        await message.reply('На главном корпусе есть Знаки зодиака под которыми по традиции фотографируются, и загадывают желания!')
    if number == 4:
        await message.reply('У "Созвездия" есть свой маскот Звездун⭐')
    if number == 5:
        await message.reply('А вы уже выполняли задания в пути героя? Всё верно, это специальный телеграм бот от созвездия, который позволяет вам выполнять задания и получать за это ценные призы!🏆')
    if number == 6:
        await message.reply('В Созвездии всего 7 корпусов🏠')
    if number == 7:
        await message.reply('Знаете что танцуют перед каждым мероприятием вожатые и дети? - Раскач! Присоединяйтесь и вы к ним!🕺💃')
    if number == 8:
        await message.reply('Каждое утро проходит час пик, не пропусти его если хочешь узнать больше о дальнем востоке и о результатах дня в пути героя!')
    if number == 9:
        await message.reply('Обязательно заглядывайте в Созвездие маркет! Там вы можете найти фирменный мерч созвездия!')
    if number == 10:
        await message.reply('Самым любимым блюдом в столовой являются Пельмени, их обожает каждый!😍')
@dp.message_handler(commands=['creator'])
async def send_creator(message: types.message):
    await message.answer('Мои создатели: Ташлыков Дмитрий Романович и Пичко Георгий Павлович')

@dp.message_handler(text="✨Случайный факт о Созвездии✨")
async def facts(message: types.message):
    number = r.randint(1,10)
    if number == 1:
        await message.reply('На территории дружины, есть большой стул, который построила семья, однажды проживающая в "Созвездии". Все кто хочет, может загадать желание возле него.')
    if number == 2:
        await message.reply('Изначально в "Созвездии" были только весенние и летние смены🍃')
    if number == 3:
        await message.reply('На главном корпусе есть Знаки зодиака под которыми по традиции фотографируются, и загадывают желания!')
    if number == 4:
        await message.reply('У "Созвездия" есть свой маскот Звездун⭐')
    if number == 5:
        await message.reply('А вы уже выполняли задания в пути героя? Всё верно, это специальный телеграм бот от созвездия, который позволяет вам выполнять задания и получать за это ценные призы!🏆')
    if number == 6:
        await message.reply('В Созвездии всего 7 корпусов🏠')
    if number == 7:
        await message.reply('Знаете что танцуют перед каждым мероприятием вожатые и дети? - Раскач! Присоединяйтесь и вы к ним!🕺💃')
    if number == 8:
        await message.reply('Каждое утро проходит час пик, не пропусти его если хочешь узнать больше о дальнем востоке и о результатах дня в пути героя!')
    if number == 9:
        await message.reply('Обязательно заглядывайте в Созвездие маркет! Там вы можете найти фирменный мерч созвездия!')
    if number == 10:
        await message.reply('Самым любимым блюдом в столовой являются Пельмени, их обожает каждый!😍')
@dp.message_handler(commands=['creator'])
async def send_creator(message: types.message):
    await message.answer('Мои создатели: Ташлыков Дмитрий Романович и Пичко Георгий Павлович')

@dp.message_handler(text="✨Случайный факт о Созвездии✨")
async def facts(message: types.message):
    number = r.randint(1,10)
    if number == 1:
        await message.reply('На территории дружины, есть большой стул, который построила семья, однажды проживающая в "Созвездии". Все кто хочет, может загадать желание возле него.')
    if number == 2:
        await message.reply('Изначально в "Созвездии" были только весенние и летние смены🍃')
    if number == 3:
        await message.reply('На главном корпусе есть Знаки зодиака под которыми по традиции фотографируются, и загадывают желания!')
    if number == 4:
        await message.reply('У "Созвездия" есть свой маскот Звездун⭐')
    if number == 5:
        await message.reply('А вы уже выполняли задания в пути героя? Всё верно, это специальный телеграм бот от созвездия, который позволяет вам выполнять задания и получать за это ценные призы!🏆')
    if number == 6:
        await message.reply('В Созвездии всего 7 корпусов🏠')
    if number == 7:
        await message.reply('Знаете что танцуют перед каждым мероприятием вожатые и дети? - Раскач! Присоединяйтесь и вы к ним!🕺💃')
    if number == 8:
        await message.reply('Каждое утро проходит час пик, не пропусти его если хочешь узнать больше о дальнем востоке и о результатах дня в пути героя!')
    if number == 9:
        await message.reply('Обязательно заглядывайте в Созвездие маркет! Там вы можете найти фирменный мерч созвездия!')
    if number == 10:
        await message.reply('Самым любимым блюдом в столовой являются Пельмени, их обожает каждый!😍')
@dp.message_handler(commands=['creator'])
async def send_creator(message: types.message):
    await message.answer('Мои создатели: Ташлыков Дмитрий Романович и Пичко Георгий Павлович')

if __name__ =='__main__':
    executor.start_polling(dp)
