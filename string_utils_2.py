
def modified(self):
        try:
            return self.__modified
        except AttributeError:
            return False


def returnTicker(self):
        return self.api_query("returnTicker")

