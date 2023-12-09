from Student import Student
from course import Course, courses
import pytest

@pytest.fixture
def student():
    return Student("001", "Test Student")

@pytest.fixture
def courseA():
    return Course("COSC", "111", 30, "John Doe", "Programming I", "PH 503", "TH 9:00")

def test_register_course(student, courseA):
    courses.append(courseA)
    assert student.register_course("COSC", "111", courses) == "Registered in Programming I"
    assert student.get_registered_courses() == ["Programming I (COSC 111)"]

def test_get_registered_courses(student, courseA):
    courses.append(courseA)
    student.register_course("COSC", "111", courses)
    registered_courses = student.get_registered_courses()
    assert registered_courses == ["Programming I (COSC 111)"]