# TODO: add unit test for this function

def cipher(self, value):
        self.__cipher = self.__check_attr(value, 0, 'cipher')
        if value == None:
            value = "AES-256"
        if value == "AES-256":
            self.__dict_size = self.__DICT_AES_SIZE
            self.__config_key_size = self.AES_KEY_SIZE
            # Keep the first 256 bits of an existing AES key
            if hasattr(self, "config_key") and self.config_key != None:
                self.config_key = self.config_key[:self.AES_KEY_SIZE]
        elif value == "XTS-AES-256":
            self.__dict_size = self.__DICT_XTS_SIZE
            self.__config_key_size = self.XTS_KEY_SIZE
            # If an existing key has only 256 bits, we add 256 random bits for the longer HMAC key
            if hasattr(self, "config_key") and self.config_key != None and len(self.config_key) != self.XTS_KEY_SIZE:
                self.config_key = self.config_key + Random.new().read(self.AES_KEY_SIZE)
        else:
            msg = 'Unsupported configuration encryption algorithm: ' + value
            raise ValueError(msg)


def identifier(self):
        return self.__identifier


def __init__(self):
        """Initialize the public attributes

