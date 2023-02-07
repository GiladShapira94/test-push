

import mlrun
@mlrun.handler(outputs=['result'])
def multi_2(number):
    result = 2 * number
    return result
