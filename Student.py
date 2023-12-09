class Student:
    def __init__(self, eid, name):
        self.eid = eid
        self.name = name
        self.registered_courses = []

    def register_course(self, prefix, course_number,courses):
        
        course_to_register = None
        for course in courses:
            if course._prefix == prefix and course._course_number == course_number:
                course_to_register = course
                break

        if course_to_register:
            if course_to_register not in self.registered_courses:
                self.registered_courses.append(course_to_register)
                return f"Registered in {course_to_register._name}"
            else:
                return "Already registered in this course"
        else:
            return "Course is full"
        
        return "Course not found"
    
    def get_registered_courses(self):
        return [f"{course._name} ({course._prefix} {course._course_number})" for course in self.registered_courses]

students = []
