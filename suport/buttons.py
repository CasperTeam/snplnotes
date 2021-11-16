from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = [
        [
        InlineKeyboardButton("1st Year", callback_data="year1"),
        InlineKeyboardButton("2nd Year", callback_data="year2"),
        ],
        [
        InlineKeyboardButton("❌ Close", callback_data="close_btn"),
        InlineKeyboardButton("Help", callback_data="help_btn"),
        InlineKeyboardButton("🔎 Go Inline", switch_inline_query_current_chat='')
        ]
        ]

close_inline = [
               [
                    InlineKeyboardButton("❌ Close", callback_data="close_btn"),
                    InlineKeyboardButton("🔎 Go Inline", switch_inline_query_current_chat='')
               ]
               ]

result = [
         [
                InlineKeyboardButton("🎯 Source", url="https://t.me/srinplrobot"),
                InlineKeyboardButton("🔎 Go Inline", switch_inline_query_current_chat='')
         ]
         ]

setup = [
        [
            InlineKeyboardButton("❓ About", callback_data="about_btn"),
            InlineKeyboardButton("🌐 Index Chats", callback_data="index_btn")
        ],
        [
            InlineKeyboardButton("📑 Update Chats", callback_data="update_btn"),
            InlineKeyboardButton("⛔ Delete Chats", callback_data="delete_btn")
        ],
        [
            InlineKeyboardButton("🔍 View Chats", callback_data="view_btn"),
            InlineKeyboardButton("⬅️ Back", callback_data="start_btn")
        ]
        ]

back_close = [
             [
                 InlineKeyboardButton("Close", callback_data="close_btn"),
                 InlineKeyboardButton("⬅️ Back", callback_data="back_btn")
             ]
             ]
year1 = [
        [
        InlineKeyboardButton("Maths", callback_data="mat1"),
        InlineKeyboardButton("Physics", callback_data="phy1"),
        InlineKeyboardButton("Chemistry", callback_data="che1"),
        ],
        [
        InlineKeyboardButton("❌ Close", callback_data="close_btn"),
        InlineKeyboardButton("Help", callback_data="help_btn"),
        InlineKeyboardButton("🔎 Go Inline", switch_inline_query_current_chat='')
        ]
        ]
year2 = [
        [
        InlineKeyboardButton("Maths", callback_data="mat2"),
        InlineKeyboardButton("Physics", callback_data="phy2"),
        InlineKeyboardButton("Chemistry", callback_data="che2"),
        ],
        [
        InlineKeyboardButton("❌ Close", callback_data="close_btn"),
        InlineKeyboardButton("Help", callback_data="help_btn"),
        InlineKeyboardButton("🔎 Go Inline", switch_inline_query_current_chat='')
        ]
        ]



help_button = InlineKeyboardMarkup(setup)
start_button = InlineKeyboardMarkup(start)
back_button = InlineKeyboardMarkup(back_close)
inline_result_markup = InlineKeyboardMarkup(result)
close_with_inline = InlineKeyboardMarkup(close_inline)
