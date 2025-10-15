class CourseEnrollment:
    def __init__(self, student_name):
        self.student_name = student_name
        self.courses = []
    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.student_name} enrolled in {course}")
    def show_courses(self):
        print(f"\nCourses enrolled by {self.student_name}:")
        for course in self.courses:
            print("-", course)
student1 = CourseEnrollment("Leena")
student1.enroll_course("Python Programming")
student1.enroll_course("Data Structures")
student1.show_courses()
