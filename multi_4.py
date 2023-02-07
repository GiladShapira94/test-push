

import mlrun
@mlrun.handler(outputs=['result'])
def multi_4(number):
    result = 4 * number
    return result
