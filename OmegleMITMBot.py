from OmegleBot import OmegleBot
from OmegleSession import SessionStatus

from selenium.common.exceptions import InvalidElementStateException

class OmegleMITMBot(OmegleBot):

    def __init__(self, blacklist):
        OmegleBot.__init__(self)

        self.blacklist = blacklist

    def HandleMessage(self, outBot):
        selfStatus = self.session.GetSessionStatus()
        outStatus = outBot.session.GetSessionStatus()

        if selfStatus == SessionStatus.CAPTCHA:
            return

        if selfStatus == SessionStatus.CLOSED_SESSION or selfStatus == SessionStatus.FRONT_PAGE or outStatus is not SessionStatus.IN_SESSION:
            self.session.StartNewSession()
            outBot.session.StartNewSession()
            return

        if selfStatus == SessionStatus.IN_SESSION and outStatus == SessionStatus.IN_SESSION:
            if self.HasNewMessage():
                message = self.GetLastMessage()

                if message is not None:
                    if self.blacklist is not None:
                        if self.blacklist.isBanned(message):
                            return

                    try:
                        outBot.session.SendMessage(message)
                    except InvalidElementStateException:
                        print('This message could not be send')

                    try:
                        print(message)
                    except UnicodeEncodeError:
                        print('This message could not be displayed')
