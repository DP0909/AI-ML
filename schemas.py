from pydantic import BaseModel

class UserSchema(BaseModel):
    email: str
    password: str

class DocumentSchema(BaseModel):
    title: str
    company_name: str
    document_type: str