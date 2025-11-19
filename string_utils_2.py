
def modified(self):
        try:
            return self.__modified
        except AttributeError:
            return False

