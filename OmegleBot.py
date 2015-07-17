from OmegleSession import OmegleSession, SessionStatus

class OmegleBot:

    def __init__(self):
        self.session = OmegleSession()
        self.log = []

    def Setup(self):
        self.session.Setup()

    def Stop(self):
        self.session.Stop()

    def HasNewMessage(self):
        newLog = self.session.GetMessages()

        if self.log == newLog:
            return False

        self.log = newLog
        return True

    def GetLastMessage(self):
        if len(self.log) > 0:
            return self.log[-1]
        else:
            return None

    def PrintLog(self):
        for message in self.log:
            print(message)
