from fastapi import FastAPI, HTTPException
from course import courses
from Student import students

app = FastAPI()


@app.get("/courses/{prefix}")
def get_courses(prefix: str):
    # return all the courses under the prefix
    results = []
    for course in courses:
        if course.is_prefix(prefix):
            results.append(course)
    
    return results

@app.get("/student_courses/{eid}")
def get_student_courses(eid: str):
    for student in students:
        if student.eid == eid:
            return student.get_registered_courses()
        
    raise HTTPException(status_code=404, detail="Student with EID " + str(eid) + " not found")
