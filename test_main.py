from fastapi.testclient import TestClient
from main import app
from test_course import courseA
from course import courses
from course import Course
from Student import Student
from Student import students

client = TestClient(app)

def test_get_courses(courseA):
    courses.append(courseA)

    response = client.get("/courses/COSC")
    assert response.status_code == 200
    assert response.json() == [
        {
            "_prefix":"COSC",
            "_course_number":"111",
            "_cap":30,
            "_instructor":"John Doe",
            "_name":"Programming I",
            "_place":"PH 503",
            "_meeting_times":"TH 9:00"
        }]

    courses.pop()

def setup_student_data():
    courseA = Course("COSC", "111", 30, "John Doe", "Programming I", "PH 503", "TH 9:00")
    courses.append(courseA)

    student = Student("001", "Test Student")
    student.register_course("COSC", "111", courses)
    return student

def test_get_student_courses():
    test_student = setup_student_data()
    
    students.append(test_student)
    
    response = client.get(f"/student_courses/{test_student.eid}")
    assert response.status_code == 200
    assert response.json() == ["Programming I (COSC 111)"]

    students.remove(test_student)