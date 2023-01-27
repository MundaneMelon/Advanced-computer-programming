from desserts import *
from enum import Enum

class Payment(Enum):
    CASH = 1
    CARD = 2
    PHONE = 3

PayType = Payment(value=2)