from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from enum import Enum

class SessionStatus(Enum):
    LOOKING_FOR_SESSION = 'Look for session'
    IN_SESSION = 'In session'
    CAPTCHA = 'Captcha'
    CLOSED_SESSION = 'Out of session'
    FRONT_PAGE = 'Front Page'

class OmegleSession:

    def __init__(self):
        self.driver = webdriver.Firefox()

    # Setup and stop
    def Setup(self):
        self.driver.get('http://www.omegle.com')

    def Stop(self):
        self.driver.close()

    # Messaging Functions
    def TypeMessage(self, message):
        chatBox = self.driver.find_element_by_class_name('chatmsg')
        chatBox.send_keys(message)

    def ClearMessage(self):
        chatBox = self.driver.find_element_by_class_name('chatmsg')
        chatBox.clear()

    def SendMessage(self, message=''):
        chatBox = self.driver.find_element_by_class_name('chatmsg')

        if message != '':
            chatBox.send_keys(message)

        chatBox.send_keys(Keys.RETURN)

    def isTyping(self):
        return len(self.driver.find_elements_by_xpath("//*[contains(text(),'Stranger is typing...')]")) > 0

    # Session Status
    def GetSessionStatus(self):
        if len(self.driver.find_elements_by_xpath("//*[contains(text(),'Looking for someone you can chat with...')]")) > 0 or len(self.driver.find_elements_by_xpath("//*[contains(text(),'connecting to server...')]")) > 0:
            return SessionStatus.LOOKING_FOR_SESSION

        if len(self.driver.find_elements_by_id('recaptcha_challenge_image')) > 0:
            return SessionStatus.CAPTCHA

        if len(self.driver.find_elements_by_id('textbtn')) > 0:
            return SessionStatus.FRONT_PAGE

        if len(self.driver.find_elements_by_class_name('newchatbtnwrapper')) > 0:
            return SessionStatus.CLOSED_SESSION

        return SessionStatus.IN_SESSION

    # Session Functions
    def StartNewSession(self):
        if self.GetSessionStatus() == SessionStatus.FRONT_PAGE:
            textBtn = self.driver.find_element_by_id('textbtn')
            textBtn.click()
            return

        disconnectBtn = self.driver.find_element_by_class_name('disconnectbtn')

        if self.GetSessionStatus() == SessionStatus.IN_SESSION:
            disconnectBtn.click()
            disconnectBtn.click()

        disconnectBtn.click()

    def StopSession(self):
        if self.GetSessionStatus() == SessionStatus.IN_SESSION:
            disconnectBtn = self.driver.find_element_by_class_name('disconnectbtn')
            disconnectBtn.click()
            disconnectBtn.click()

    # Messages
    def GetMessages(self):
        messageElements = self.driver.find_elements_by_class_name('strangermsg')
        messages = []

        for ele in messageElements:
            message = ele.find_element_by_tag_name('span').text
            messages.insert(len(messages), message)

        return messages