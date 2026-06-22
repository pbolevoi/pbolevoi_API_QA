from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    email: str
    name: str
    nikname: str
    uuid: str

    @field_validator('email', 'name', 'nikname', 'uuid')
    def field_are_not_empty(cls, value):
        if value == '' or value is None:
            raise ValueError('Field is empty')
        else:
            return value
