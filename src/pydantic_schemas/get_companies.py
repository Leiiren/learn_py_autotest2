from pydantic import BaseModel, field_validator
from src.enums.company_enums import CompanyStatus, UserErrors

class GetCompanies(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: CompanyStatus #Только три значения могут быть здесь


    # @field_validator('email') # Одновременное комментирование с UserErrors в enums.company_enums.py.UserErrors
    # def check_that_dog_presented_in_email_address(cls, email):
    #     if '@' in email:
    #         return email
    #     else:
    #         raise ValueError(UserErrors.WRONG_EMAIL.value)



# Если поле обязательное, то оно выглядит так:
# class GetCompanies(BaseModel):
#     company_id: int
#
# Если поле НЕ ОБЯЗАТЕЛЬНОЕ, то оно выглядить может так:
#
# class GetCompanies(BaseModel):
#     company_id: int = None
#     company_id: int = 0
#     company_name: str = ''
