

import mlrun
@mlrun.handler(outputs=['result'])
def add_2(number):
    result = 2 + number
    return result
