from pydantic import BaseModel

class states(BaseModel):
    state_name : str

class pwpDetail(BaseModel):
    email : str








































class Item(BaseModel):
    ID: int
    PASS:str

class Table_name(BaseModel):
    Table:str

class Drop_table(BaseModel):
    Table:str


class UserModel(BaseModel):
    table_name:str
    user_name:str
    email:str
    password:str


class UserModel1(BaseModel):
    password:str
    email:str
    user_name:str


class iron(BaseModel):
    email:str
