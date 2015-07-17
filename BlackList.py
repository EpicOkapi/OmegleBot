
class BlackList:
    def __init__(self):
        self.phrases = []

    def load(self, filename):
        f = open(filename, encoding='utf-8')

        for line in f.read().splitlines():
            self.phrases.insert(len(self.phrases), line)

    def isBanned(self, p):
        if any(phrase in p for phrase in self.phrases):
            return True

        return False
