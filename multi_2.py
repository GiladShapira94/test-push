

import mlrun
@mlrun.handler(outputs=['result'])
def multi_2(number):
    #test
    result = 2 * number
    return result
