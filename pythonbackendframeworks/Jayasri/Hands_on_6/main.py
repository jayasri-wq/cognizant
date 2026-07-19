from fastapi import FastAPI, HTTPException
from schemas import CourseCreate, CourseResponse

app=FastAPI(
    title="Course Management API",
    version="1.0"
)

courses=[]

@app.get("/")
async def root():
    return {"message":"API running"}

@app.post("/api/courses/",response_model=CourseResponse)
async def create_course(course:CourseCreate):
    obj=course.dict()
    obj["id"]=len(courses)+1
    courses.append(obj)
    return obj

@app.get("/api/courses/{course_id}")
async def get_course(course_id:int):
    for c in courses:
        if c["id"]==course_id:
            return c
    raise HTTPException(status_code=404,detail="Course not found")

@app.get("/api/courses/")
async def get_courses(skip:int=0,limit:int=10):
    return courses[skip:skip+limit]