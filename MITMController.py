import time

from OmegleMITMBot import OmegleMITMBot

class MITMController:

    def __init__(self, blacklist=None):
        self.bot1 = OmegleMITMBot(blacklist)
        self.bot2 = OmegleMITMBot(blacklist)

        self.running = True

    def Setup(self):
        self.bot1.Setup()
        self.bot2.Setup()

    def Stop(self):
        self.bot1.Stop()
        self.bot2.Stop()

    def Run(self):
        self.running = True

        while self.running:
            self.bot1.HandleMessage(self.bot2)
            self.bot2.HandleMessage(self.bot1)

        time.sleep(0.1)
