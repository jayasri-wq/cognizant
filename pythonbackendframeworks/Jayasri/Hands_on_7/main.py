from fastapi import FastAPI, HTTPException, BackgroundTasks, status
from schemas import *

app = FastAPI(
    title="Course Management API",
    description="FastAPI CRUD API",
    version="1.0",
    contact={"name": "Jayasri"}
)

courses = []

def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")

@app.get("/")
async def root():
    return {"message": "API running"}

@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create Course",
    response_description="Course Created"
)
async def create_course(course: CourseCreate):
    obj = course.dict()
    obj["id"] = len(courses) + 1
    courses.append(obj)
    return obj

@app.get("/api/courses/{id}", response_model=CourseResponse, tags=["Courses"])
async def get_course(id: int):
    for c in courses:
        if c["id"] == id:
            return c
    raise HTTPException(status_code=404, detail="Course not found")

@app.put("/api/courses/{id}", tags=["Courses"])
async def update_course(id: int, course: CourseUpdate):
    for c in courses:
        if c["id"] == id:
            c.update(course.dict(exclude_none=True))
            return c
    raise HTTPException(status_code=404, detail="Course not found")

@app.delete(
    "/api/courses/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"]
)
async def delete_course(id: int):
    for c in courses:
        if c["id"] == id:
            courses.remove(c)
            return
    raise HTTPException(status_code=404, detail="Course not found")

@app.post("/api/enrollments/")
async def create_enrollment(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_confirmation_email, "student@gmail.com")
    return {"message": "Enrollment Created"}

@app.get("/api/courses/{id}/students/", tags=["Courses"])
async def get_students(id: int):
    return [{"id": 1, "name": "John"}]