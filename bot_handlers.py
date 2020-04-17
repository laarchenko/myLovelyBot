from bot import bot  # Импортируем объект бота
from config import l_id


@bot.message_handler (content_types=["photo", "document", "text", "audio"] )  # Любой текст
def repeat_all_messages(message):
    bot.forward_message(l_id,message.chat.id, message.message_id)


