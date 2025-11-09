# TODO: refactor this

def randomise_dictionary_inputs(strategy_dictionary_local):
    strategy_dictionary_local['ml_mode'] = choice(['adaboost', 'randomforest', 'gradientboosting', 'extratreesfitting']) #'svm'
    strategy_dictionary_local['regression_mode'] = choice(['regression', 'classification']) # mod30
    strategy_dictionary_local['preprocessing'] = choice(['PCA', 'FastICA', 'None'])
    return strategy_dictionary_local


def returnTradeHistory(self,currencyPair):
        return self.api_query('returnTradeHistory',{"currencyPair":currencyPair})


def cancel(self,currencyPair,orderNumber):
        return self.api_query('cancelOrder',{"currencyPair":currencyPair,"orderNumber":orderNumber})


def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))

