import uvicorn
from fastapi import FastAPI
from .schema.student import Student
from random import randint

app = FastAPI()

students = [
    {"name": "student 1", "age": 14, "grade": 8, "id": 0},
    {"name": "student 2", "age": 18, "grade": 12, "id": 1},
    {"name": "student 3", "age": 12, "grade": 6, "id": 2},
]


def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student_id


@app.get("/")
def read_root():
    return {"message": "This is Student App"}


@app.get("/students")
def dev_all_students():
    return {"message": "Students data fetched successfully.", "data": students}


@app.get("/students/{student_id}")
def get_one_student(student_id: int):
    index = get_student(student_id)
    if index is None:
        return {"message": f"No student with id {student_id}"}

    return {"message": "Student data fetched successfully.", "data": students[index]}


@app.post("/students")
def create_new_student(student: Student):
    student = student.model_dump()
    id = randint(111111, 999999)
    
    while get_student(id) is not None:
        id = randint(111111, 999999)
        
    student['id'] = id
    
    students.append(student)

    return {"message": "New student created successfully", "data": student}

@app.put('/students/{student_id}')
def update_student(student_id: int, student: Student):
    index = get_student(student_id)

    if index is None:
        return {'message': f'Student with student id {id} does not exist!'}
    
    students[index] =  student.model_dump()
    
    return {'message': 'Student updated succesfully', 'data': students[index]}

@app.delete('/students/{student_id}')
def delete_student(student_id: int):
    index = get_student(student_id)

    if index is None:
        return {'message': 'Student not found.'}

    students.pop(index)
    
    return  {'message': 'Student deleted successfully'}

def dev():
    uvicorn.run("app.main:app", port=8000, reload=True)
