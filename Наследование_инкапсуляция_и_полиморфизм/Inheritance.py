class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and 1 <= grade <= 10:

            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]

        else:
            return "Ошибка"

    def __str__(self):

        average = self.average_grade()

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершённые курсы: {', '.join(self.finished_courses)}\n"
            f"Средняя оценка за домашние задания: {average}\n"
        )

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented


    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented


    def average_grade(self):

        total = 0
        count = 0

        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)

        if count > 0:
            average = total / count

        else:
            average = 0


        return average





class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def __str__(self):
        average = self.average_grade()

        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {average}\n"
        )

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented


    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented


    def average_grade(self):
        total = 0
        count = 0

        for grades in self.grades.values():
            total += sum(grades)
            count += len(grades)

        if count > 0:
            average = total / count

        else:
            average = 0

        return average



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"



def average_hw_grade(students, course):
    total = 0
    count = 0
    for student in students:
        total += sum(student.grades.get(course, []))
        count += len(student.grades.get(course, []))

    if count == 0:
        return 0

    return total / count


def average_lecture_grade(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        total += sum(lecturer.grades.get(course, []))
        count += len(lecturer.grades.get(course, []))

    if count == 0:
        return 0

    return total / count




student1 = Student("Ivan", "Petrov", "male")
student1.courses_in_progress.append("Python")



reviewer1 = Reviewer("Anna", "Smith")
reviewer1.courses_attached.append("Python")

reviewer2 = Reviewer("Lena", "Ivanova")
reviewer2.courses_attached.append("Python")


reviewer1.rate_hw(student1, "Python", 10)
reviewer2.rate_hw(student1, "Python", 8)


lecturer1 = Lecturer("Petr", "Sidorov")
lecturer1.courses_attached.append("Python")

lecturer2 = Lecturer("Alex", "Ivanov")
lecturer2.courses_attached.append("Python")

student1.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer1, "Python", 7)

student1.rate_lecturer(lecturer2, "Python", 10)
student1.rate_lecturer(lecturer2, "Python", 9)

student1.courses_in_progress.append("Git")
student1.finished_courses.append("Введение в программирование")

student2 = Student('Alex', 'Smirnov', 'male')
student2.courses_in_progress.append("Git")
student2.courses_in_progress.append("Python")

reviewer1.rate_hw(student2, "Python", 7)
reviewer2.rate_hw(student2, "Python", 9)



student2.rate_lecturer(lecturer2, "Python", 9)
student2.rate_lecturer(lecturer2, "Python", 7)


mentor1 = Mentor('Alex', 'Johnson')
mentor2 = Mentor("Mary", "Sidorova")

students_list = [student1, student2]

lecturers_list = [lecturer1, lecturer2]




print(student1.grades)
print(lecturer1.grades)
print(lecturer2.grades)

print(reviewer1)
print(reviewer2)


print(lecturer1)
print(student1)

print(lecturer2)
print(student2)


print(lecturer1 < lecturer2)
print(lecturer2 < lecturer1)
print(lecturer1 == lecturer2)

print(student1 == student2)
print(student1 < student2)
print(student2 < student1)

print(mentor1)
print(mentor2)

print(average_hw_grade(students_list, "Python"))
print(average_lecture_grade(lecturers_list, "Python"))
print(average_hw_grade(students_list, "Git"))
print(average_lecture_grade(lecturers_list, "Git"))






