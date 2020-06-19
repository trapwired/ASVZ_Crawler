import configparser
import datetime
import telepot
from telepot.loop import MessageLoop


class ASVZ_Crawler_Bot(object):

    def __init__(self, config: configparser.RawConfigParser, api_config: configparser.RawConfigParser):
        self.config = config
        self.api_config = api_config

        self.bot = telepot.Bot(self.api_config["API"]["key"])

    def handle(msg):
        chat_id = msg['chat']['id']  # Receiving the message from telegram
        command = msg['text']  # Getting text from the message

        print('Received:')
        print(command)

        # Comparing the incoming message to send a reply according to it
        if command == '/hi':
            bot.sendMessage(chat_id, str("Hi! MakerPro"))
        elif command == '/time':
            bot.sendMessage(chat_id,
                            str("Time: ") + str(now.hour) + str(":") + str(now.minute) + str(":") + str(now.second))
        elif command == '/date':
            bot.sendMessage(chat_id,
                            str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))

    def main(self):
        # config File
        config = configparser.RawConfigParser()
        config.read('config.ini', encoding='utf8')

        api_config = configparser.RawConfigParser()
        api_config.read('api.ini', encoding='utf8')



    if __name__ == "__main__":
        main()
