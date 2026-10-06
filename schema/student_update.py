from pydantic import BaseModel

class StudentUpdate(BaseModel):
    course: str


