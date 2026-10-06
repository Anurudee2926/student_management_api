from fastapi import APIRouter, HTTPException
from schema.students import Student
from schema.student_update import StudentUpdate
from routers.student_data import students
from service.student_service import update_student as update_student_service


router = APIRouter()
# @router.get("/")
# def get_student(student_id:int, student_name:str, student_course:str):
#         return{
#             "id": student_id,
#             "name": student_name,
#             "course": student_course,
#             "message": "student found"
#         }
#         raise HTTPException(status_code=404, detail="Student not found")
@router.get("/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")
@router.post("/")
def create_student(student: Student):

    new_id = len(students) + 1

    student_data = {
        "id": new_id,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(student_data)

    return student_data
@router.patch("/{student_id}")
def update_student(student_id: int, student_update: StudentUpdate):

    return update_student_service(
        student_id,
        student_update.course
    )
        
        
@router.delete("/{student_id}")
def delete_student(student_id: int):

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                return {"message": "Student deleted"}
        raise HTTPException(status_code=404, detail="Student not found")

            