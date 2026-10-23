from fastapi import FastAPI

from routers.students import router



#schema for student
# class Student(BaseModel):
#         name : str
#         age: int
#         course : str



app = FastAPI()
app.include_router(router, prefix= "/students", tags=["students"])


 
