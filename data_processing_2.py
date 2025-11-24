
def signal_handler(signal, frame):
    if (exchange.socket):
        print('Closing WebSocket connection...')
        exchange.close_socket()
        sys.exit(0)
    else:
        print('stopping strategy...')
        exchange.strategy.stop()
        sys.exit(0)


def lineNumbers(self, lines):
        width = self.TextObj.TextWidth(stc.STC_STYLE_LINENUMBER, str(lines) + " ")
        self.TextObj.SetMarginWidth(0, width)


def modified(self):
        try:
            return self.__modified
        except AttributeError:
            return False


def OnSaveAs(self, event):
        """
        Save file as.
        """
        if self.AskUserForFilename(defaultFile=self.filename,
                                   style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
                                   **self.DefaultFileDialogOptions()):
            self.SaveFile()

