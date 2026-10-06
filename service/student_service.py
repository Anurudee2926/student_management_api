from fastapi import HTTPException
from routers.student_data import students


def update_student(student_id: int, course: str):

    for student in students:

        if student["id"] == student_id:

            student["course"] = course

            return {
                "message": "Student profile updated",
                "course": course
            }

    raise HTTPException(status_code=404, detail="Student not found")