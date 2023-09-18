from enum import Enum

class GlobalErrorsMessages(Enum):
    WRONG_STASUS_CODE = 'Received status code is not equal to expected'
    WRONG_ELEMENT_COUNT = 'The amount of data is not as expected'
