from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

# ---- USER SCHEMAS ----
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "member"

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True

# ---- TASK SCHEMAS ----
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    status: str = "Pending"

class TaskCreate(TaskBase):
    assigned_to: int

class TaskResponse(TaskBase):
    id: int
    project_id: int
    assigned_to: int

    class Config:
        from_attributes = True

# ---- PROJECT SCHEMAS ----
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    created_by: int
    tasks: List[TaskResponse] = []

    class Config:
        from_attributes = True