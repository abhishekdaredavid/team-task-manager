from pydantic import BaseModel, EmailStr
from typing import Optional

# Users
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    role: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    id: int

# Projects
class ProjectCreate(BaseModel):
    name: str
    description: str

class ProjectOut(BaseModel):
    id: int
    name: str
    description: str
    class Config:
        from_attributes = True

# Tasks
class TaskCreate(BaseModel):
    title: str
    description: str
    project_id: int
    assigned_to: int

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: str
    project_id: int
    assigned_to: int
    class Config:
        from_attributes = True