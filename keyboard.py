from queue import Empty


import pickle


import logging


from telegram.ext import (


    Updater,


    CommandHandler, 


    MessageHandler, 


    ConversationHandler,


    Filters, 


    CallbackQueryHandler, 


    CallbackContext


)


from telegram import  (


    Update,


    InlineKeyboardMarkup, 


    InlineKeyboardButton, 


    KeyboardButton, 


    ReplyKeyboardMarkup, 


)

HBM = [
    [InlineKeyboardButton("💰 Change Refer", callback_data="cb1"), InlineKeyboardButton("📥 Minimum Redeem", callback_data="cb2")], 
    
    [InlineKeyboardButton("🎁 Change Bonus", callback_data="cb3"), InlineKeyboardButton("🔋Change Channel", callback_data="cb4")],
    
    [InlineKeyboardButton("🔎 Change Currency", callback_data="cb5"), InlineKeyboardButton("🔗 Change Balance", callback_data="cb6")],
    [InlineKeyboardButton("📈 Auto PaySetting", callback_data="cb7")]
    
]

yourKBS = [
    [InlineKeyboardButton("✏️ Set Wallet", callback_data="set.Wallet")]
]

HBM = [
    [InlineKeyboardButton("💰 Change Refer", callback_data="cb1"), InlineKeyboardButton("📥 Minimum Redeem", callback_data="cb2")], 
    
    [InlineKeyboardButton("🎁 Change Bonus", callback_data="cb3"), InlineKeyboardButton("🔋Change Channel", callback_data="cb4")],
    
    [InlineKeyboardButton("🔎 Change Currency", callback_data="cb5"), InlineKeyboardButton("🔗 Change Balance", callback_data="cb6")],
    [InlineKeyboardButton("📈 Auto PaySetting", callback_data="cb7")]
    
]

KBC = [[KeyboardButton(text='⛔ Cancel')]]

KBM = [


            [KeyboardButton(text='💰 Balance')], [KeyboardButton(text='🙌🏻 Invite'),


            KeyboardButton(text='🎁 Bonus'), KeyboardButton(text='🗂 Wallet')],


            [KeyboardButton(text='💳 Withdraw'), KeyboardButton(text='📊 Statistics')]


        ]
        
        
KB = [


            [KeyboardButton(text='💰 Balance')], [KeyboardButton(text='🙌🏻 Invite'),


            KeyboardButton(text='🎁 Bonus'), KeyboardButton(text='🗂 Wallet')],


            [KeyboardButton(text='💳 Withdraw'), KeyboardButton(text='📊 Statistics')]


        ]