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
    [InlineKeyboardButton("π° Change Refer", callback_data="cb1"), InlineKeyboardButton("π₯ Minimum Redeem", callback_data="cb2")], 
    
    [InlineKeyboardButton("π Change Bonus", callback_data="cb3"), InlineKeyboardButton("πChange Channel", callback_data="cb4")],
    
    [InlineKeyboardButton("π Change Currency", callback_data="cb5"), InlineKeyboardButton("π Change Balance", callback_data="cb6")],
    [InlineKeyboardButton("π Auto PaySetting", callback_data="cb7")]
    
]

yourKBS = [
    [InlineKeyboardButton("βοΈ Set Wallet", callback_data="set.Wallet")]
]

HBM = [
    [InlineKeyboardButton("π° Change Refer", callback_data="cb1"), InlineKeyboardButton("π₯ Minimum Redeem", callback_data="cb2")], 
    
    [InlineKeyboardButton("π Change Bonus", callback_data="cb3"), InlineKeyboardButton("πChange Channel", callback_data="cb4")],
    
    [InlineKeyboardButton("π Change Currency", callback_data="cb5"), InlineKeyboardButton("π Change Balance", callback_data="cb6")],
    [InlineKeyboardButton("π Auto PaySetting", callback_data="cb7")]
    
]

KBC = [[KeyboardButton(text='β Cancel')]]

KBM = [


            [KeyboardButton(text='π° Balance')], [KeyboardButton(text='ππ» Invite'),


            KeyboardButton(text='π Bonus'), KeyboardButton(text='π Wallet')],


            [KeyboardButton(text='π³ Withdraw'), KeyboardButton(text='π Statistics')]


        ]
        
        
KB = [


            [KeyboardButton(text='π° Balance')], [KeyboardButton(text='ππ» Invite'),


            KeyboardButton(text='π Bonus'), KeyboardButton(text='π Wallet')],


            [KeyboardButton(text='π³ Withdraw'), KeyboardButton(text='π Statistics')]


        ]