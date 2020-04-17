from flask import Flask
from telebot import types
from config import *
from bot_handlers import bot
import os
server = Flask ( __name__ )


@server.route ( '/' + TOKEN , methods=[ 'POST' ] )
def get_message():
    bot.process_new_updates ( [ types.Update.de_json (
        server.request.stream.read ().decode ( "utf-8" ) ) ] )
    return "!" , 200


@server.route ( '/' , methods=[ "GET" ] )
def index():
    bot.remove_webhook ()
    bot.set_webhook ( url="https://{}.herokuapp.com/{}".format ( APP_NAME , TOKEN ) )
    return "Hello from Heroku!" , 200

@bot.message_handler (content_types=["photo", "document", "text", "audio"] )  # Любой текст
def repeat_all_messages(message):
    bot.forward_message(l_id,message.chat.id, message.message_id)



if __name__ == "__main__":
    server.run ()
