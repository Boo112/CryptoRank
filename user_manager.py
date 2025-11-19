
def random_search_iteration(strategy_dictionary_local):
    strategy_dictionary_local = randomise_dictionary_inputs(strategy_dictionary_local)


def randomise_dictionary_inputs(strategy_dictionary_local):
    strategy_dictionary_local['ml_mode'] = choice(['adaboost', 'randomforest', 'gradientboosting', 'extratreesfitting']) #'svm'
    strategy_dictionary_local['regression_mode'] = choice(['regression', 'classification'])
    strategy_dictionary_local['preprocessing'] = choice(['PCA', 'FastICA', 'None'])
    return strategy_dictionary_local


def underlined_output(string):
    print string
    print '----------------------'
    print '\n'


def config_key(self):
        return self.__config_key


def encode_base64(bytes):
# REVIEW: double-check logic with backend team
            """Encode bytes with BASE64

