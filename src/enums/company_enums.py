from enum import Enum

class CompanyStatus(Enum):
    ACTIVE = "ACTIVE"
    BANKRUPT = "BANKRUPT"
    CLOSED = "CLOSED"

class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"