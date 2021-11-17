from bot import Bot
from presets import Presets
from pyrogram import filters
from pyrogram.types import Message, CallbackQuery
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from bot import Bot
from pyrogram import filters
from presets import Presets
from pyrogram.types import CallbackQuery


# Let's define two global variables
final_chat_list = []        # Chat list of session user having media content only (Master list)
admin_user_id = []          # User id of admin to be shared
@Bot.on_callback_query(filters.regex(r'^back1$'))
async def back(c: Bot, cb: CallbackQuery):
    await cb.message.edit(
        "HELLO!",
        reply_markup=[
            [
        InlineKeyboardButton("1ST year", callback_data="yr1"),
        InlineKeyboardButton("2nd Year", callback_data="yr1")
    ],
    [
        InlineKeyboardButton("❌ Close", callback_data="close_btn"),
    
    ]
    ]
    )

@Bot.on_message(filters.private & filters.command('notes'))
async def start_bot(c: Bot, m: Message):
    await m.reply_text(
        "HELLO!{}".format(m.from_user.first_name),
        reply_markup=[
            [
        InlineKeyboardButton("1ST year", callback_data="yr1"),
        InlineKeyboardButton("2nd Year", callback_data="yr1")
    ],
    [
        InlineKeyboardButton("❌ Close", callback_data="close_btn"),
    
    ]
    ]
    )
@Bot.on_callback_query(filters.regex(r'^yr1$'))
async def yr1(c: Bot, cb: CallbackQuery):
    await cb.message.edit(
        "Select one",
        reply_markup=[
            [
        InlineKeyboardButton("Notes", callback_data="not1"),
        InlineKeyboardButton("Videos", callback_data="vid1")
    ],
    [
        InlineKeyboardButton("Back", callback_data="back"),
    ]
        ]
    )
@Bot.on_callback_query(filters.regex(r'^yr2$'))
async def yr2(c: Bot, cb: CallbackQuery):
    await cb.message.edit(
        "Select one",
        reply_markup=[
            [
        InlineKeyboardButton("Notes", callback_data="not2"),
        InlineKeyboardButton("Videos", callback_data="vid2")
    ],
    [
        InlineKeyboardButton("Back", callback_data="back"),
    ]
        ]
    )

@Bot.on_callback_query(filters.regex(r'^close_btn$'))
async def close_button(c: Bot, cb: CallbackQuery):
    await cb.message.delete()

@Bot.on_callback_query(filters.regex(r'^not1$'))
async def not1(c: Bot, cb: CallbackQuery):
    await cb.message.edit(
        "Select one",
        reply_markup=[
            [
        InlineKeyboardButton("Maths", callback_data="nmat1"),
        InlineKeyboardButton("Physics", callback_data="nphy1"),
        InlineKeyboardButton("Chemistry", callback_data="nche1")
    ],
    [
        InlineKeyboardButton("back", callback_data="yr1"),
    ]
    ]
    )
@Bot.on_callback_query(filters.regex(r'^vid1$'))
async def vid1(c: Bot, cb: CallbackQuery):
    await cb.message.edit(
        "Select one",
        reply_markup=[
            [
        InlineKeyboardButton("Maths", callback_data="vmat1"),
        InlineKeyboardButton("Physics", callback_data="vphy1"),
        InlineKeyboardButton("Chemistry", callback_data="vche1")
    ],
    [
        InlineKeyboardButton("back", callback_data="yr1"),
    ]
    ]
    )




@Bot.on_callback_query(filters.regex(r'^not2$'))
async def not2(c: Bot, cb: CallbackQuery):
    await cb.message.edit(
        "Select one",
        reply_markup=[
            [
        InlineKeyboardButton("Maths", callback_data="nmat2"),
        InlineKeyboardButton("Physics", callback_data="nphy2"),
        InlineKeyboardButton("Chemistry", callback_data="nche2")
    ],
    [
        InlineKeyboardButton("back", callback_data="yr2"),
    ]
    ]
    )
@Bot.on_callback_query(filters.regex(r'^vid1$'))
async def vid2(c: Bot, cb: CallbackQuery):
    await cb.message.edit(
        "Select one",
        reply_markup=[
            [
        InlineKeyboardButton("Maths", callback_data="vmat2"),
        InlineKeyboardButton("Physics", callback_data="vphy2"),
        InlineKeyboardButton("Chemistry", callback_data="vche2")
    ],
    [
        InlineKeyboardButton("back", callback_data="yr2"),
    ]
    ]
    )