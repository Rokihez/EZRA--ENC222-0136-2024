class Course:
    def __init__(self, course_name):
        self.course_name = course_name


class Student:
    def __init__(self, name):
        self.name = name
        self.course = None  # Association

    def register_course(self, course):
        self.course = course  # Dependency
        print(f"{self.name} registered for {course.course_name}")


# Test the mini project
course1 = Course("Computer Programming")
student1 = Student("Ezra")

student1.register_course(course1)