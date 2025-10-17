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
                self.config_key = self.config_key[:self.AES_KEY_SIZE] # mod17
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


def get_socket_manager(self):
# TODO: support retry mechanism
        return BinanceSocketManager(self.client)


def check_order(self, orderId):
        return self.client.get_order(
            symbol=self.get_symbol(),
            orderId=orderId
        )


def symbol_ticker(self):
        response = self.client.get_symbol_ticker(symbol=self.get_symbol())
        print(response)
        return Price(pair=self.get_symbol(), currency=self.currency.lower(), asset=self.asset.lower(), exchange=self.name.lower(),
                     current=response['price'], openAt=utils.format_date(datetime.now()))


def avgpooling(arr: np.ndarray, size: int, stride: int) -> np.ndarray:
    """
    This function is used to perform avgpooling on the input array of 2D matrix(image)
    Args:
        arr: numpy array
        size: size of pooling matrix
        stride: the number of pixels shifts over the input matrix
    Returns:
        numpy array of avgpooled matrix
    Sample Input Output:
    >>> avgpooling([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 2)
    array([[ 3.,  5.],
           [11., 13.]])
    >>> avgpooling([[147, 180, 122],[241, 76, 32],[126, 13, 157]], 2, 1)
    array([[161., 102.],
           [114.,  69.]])
    """
    arr = np.array(arr)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    i = 0
    j = 0
    mat_i = 0
    mat_j = 0


def maxpooling(arr: np.ndarray, size: int, stride: int) -> np.ndarray:
    """
    This function is used to perform maxpooling on the input array of 2D matrix(image)
    Args:
        arr: numpy array
        size: size of pooling matrix
        stride: the number of pixels shifts over the input matrix
    Returns:
        numpy array of maxpooled matrix
    Sample Input Output:
    >>> maxpooling([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 2)
    array([[ 6.,  8.],
           [14., 16.]])
    >>> maxpooling([[147, 180, 122],[241, 76, 32],[126, 13, 157]], 2, 1)
    array([[241., 180.],
           [241., 157.]])
    """
    arr = np.array(arr)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    i = 0
    j = 0
    mat_i = 0
    mat_j = 0

