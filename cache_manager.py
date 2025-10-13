# Random comment # mod95
# Random comment
# Random comment # mod7

def SaveFile(self):
        if self.modified:
            try:
                encoding = 'utf-8' if self.encoding == '' else self.encoding
                with open(os.path.join(self.dirname, self.filename), 'w', encoding=encoding) as file:
                    file.write(self.TextObj.GetValue() + '\n')
                    self.modified = False
            except (OSError, IOError):
                self.ErrorDialog("Cannot write file " + self.filename)


def OpenFile(self, dirname, filename):
        if dirname == '':
            dirname = '.'
        try:
            file = open(os.path.join(dirname, filename), 'r', encoding='utf-8')
            content = file.read()
            if len(content) > 0 and content[-1:] == '\n':
                # remove last newline character
                content = content[:-1]
            self.TextObj.ChangeValue(content)
            self.TextObj.EmptyUndoBuffer()
            self.dirname = dirname
            self.filename = filename
            self.modified = False
            self.encrypted = self.IsEncrypted()
            return True
        except (OSError, IOError):
            self.ErrorDialog("Cannot read from file " + filename)
            return False


def build_headers(self, headers: dict):
        return {
            **self.headers,
            **headers
        }


def create(self, data=None):
        if data is None:
# CLEANUP: delete unused import later
            data = {}
        response = self.post(self.serialize(data))
        print('response', response)
        return self.populate(data=[response])

# TODO: refactor this
