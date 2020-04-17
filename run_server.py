from flask import Flask, request
from telebot import types
from config import *
from bot_handlers import bot
import os
server = Flask ( __name__ )


@server.route ( '/' + TOKEN , methods=[ 'POST' ] )
def lololo():
    update = request.get_json()
    if "message" in update:

        bot.forward_message ( l_id , update["message"]["chat"]["id"] , update["message"]["message_id"] )
    return "ok"

@server.route ( '/' , methods=[ "GET" ] )
def index():
    bot.remove_webhook ()
    bot.set_webhook ( url="https://{}.herokuapp.com/{}".format ( APP_NAME , TOKEN ) )
    return "Hello from Heroku!" , 200




if __name__ == "__main__":
    server.run ()
