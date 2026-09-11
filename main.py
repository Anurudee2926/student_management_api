from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path


class Student(BaseModel):
        name : str
        age: int
        course : str



app = FastAPI()
html_file = Path(__file__).parent / "student.html"
students = [
        {"id": 1, "name": "Aisha", "age": 25, "course": "Python"},
        {"id": 2, "name": "Mary", "age": 22, "course": "JavaScript"}
    ]
@app.get("/")
def home():
        return FileResponse(html_file)

@app.get("/about")
def about():
        return{"message":"This is a student's logging platform"}@app.get("/student-page")
@app.get("/student-page")
def student_page():
        return FileResponse(html_file)
@app.get("/student-search")
def search_student(student_name: str):
        for student in students:
            if student["name"].lower() == student_name.lower():
                return student

        raise HTTPException(status_code=404, detail="Student not found")


@app.get("/students")
def get_studentname(student_id:int, student_name:str, student_course:str):
        return{
            "id": student_id,
            "name": student_name,
            "course": student_course,
            "message": "student found"
        }
#pydantic model
@app.post("/students")
def create_student(student:Student):
        if student.age >=18:
            status = "Adult, Eligible"
        else:
            status = "Minor, Not Eligible"
        return{
            "student": student,
            "status" : status
        }  

class StudentUpdate(BaseModel):
        course: str

@app.patch("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
        for student in students:
            if student["id"] == student_id:
                student["course"] = StudentUpdate.course
                return {
                    "message": "Student profile updated",
                    "course": StudentUpdate.course
        }
        raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                return {"message": "Student deleted"}
        raise HTTPException(status_code=404, detail="Student not found")

