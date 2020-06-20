import schedule
import time
import telepot

class SchedulerHandler(object):

    def __init__(self, bot: telepot.Bot):
        super().__init__()
        self.bot = bot
        # schedule.every().day.at("18:00").do(self.send_next_events)
        # schedule.every().tuesday.at("14:00").do(self.send_ct)
        # schedule.every(20).seconds.do(self.send_next_events)

    def send_ct(self):
        self.bot.sendMessage(self.group_id, 'It\'s cocktail tuesday, meiergööfler')

    def run_schedule(self):
        schedule.run_pending()

    def handle(self, msg):
        pass