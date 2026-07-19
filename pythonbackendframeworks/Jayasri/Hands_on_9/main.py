from fastapi import FastAPI, HTTPException, status
from schemas import CourseCreate, CourseUpdate, CourseResponse

app = FastAPI(
    title="Course Management API",
    description="Version 1 API",
    version="1.0"
)

courses = []


@app.get("/")
async def root():
    return {"message": "API running"}


# GET ALL COURSES (Pagination)
@app.get("/api/v1/courses/")
async def get_courses(page: int = 1, page_size: int = 2):
    start = (page - 1) * page_size
    end = start + page_size

    return {
        "count": len(courses),
        "page": page,
        "page_size": page_size,
        "results": courses[start:end]
    }


# GET COURSE BY ID
@app.get("/api/v1/courses/{id}", response_model=CourseResponse)
async def get_course(id: int):

    for c in courses:
        if c["id"] == id:
            return c

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


# CREATE COURSE
@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_course(course: CourseCreate):

    obj = course.dict()
    obj["id"] = len(courses) + 1

    courses.append(obj)

    return obj


# UPDATE COURSE
@app.put("/api/v1/courses/{id}")
async def update_course(id: int, course: CourseUpdate):

    for c in courses:
        if c["id"] == id:
            c.update(course.dict(exclude_none=True))
            return c

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )


# PARTIAL UPDATE
@app.patch("/api/v1/courses/{id}")
async def patch_course(id: int):

    return {
        "message": "Course updated successfully"
    }


# DELETE COURSE
@app.delete(
    "/api/v1/courses/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(id: int):

    for c in courses:
        if c["id"] == id:
            courses.remove(c)
            return

    raise HTTPException(
        status_code=404,
        detail="Course not found"
    )