class Person:
    def __init__(self, name, last_name, age, city, education, marital_status):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.education = education
        self.marital_status = marital_status


class SchoolWorker(Person):
    def __init__(self, name, last_name, age, city, education, marital_status, work_experience, salary):
        super().__init__(name, last_name, age, city, education, marital_status)
        self.salary = salary
        self.work_experience = work_experience

    def id_for_school_worker(self):
        return f'Ім\'я-прізвище: {self.name} {self.last_name}. Повних років: {self.age}. ' \
               f'Місто: {self.city}. Освіта: {self.education}. Сімейний стан: {self.marital_status}.' \
               f'Робочий стаж у роках: {self.work_experience}. Зарплата: {self.salary} грн.'

    def salary_for_year(self):
        if str(self.salary).isdigit():
            return f'Зарплата за рік — {self.salary * 12} грн.'
        else:
            print('Некоректно введені дані, тому дані про зарплату за рік недоступні.')


class SchoolPrincipal(SchoolWorker):
    def __init__(self, name, last_name, age, city, education,
                 marital_status, work_experience, head_experience, salary):
        super().__init__(name, last_name, age, city, education, marital_status, work_experience, salary)
        self.head_experience = head_experience

    def id_for_school_principal(self):
        return f'Ім\'я-прізвище: {self.name} {self.last_name}. Повних років: {self.age}. ' \
               f'Місто: {self.city}. Освіта: {self.education}. Сімейний стан: {self.marital_status}. ' \
               f'Робочий стаж у роках: {self.work_experience}. Досвід управлінця у роках: {self.head_experience}. ' \
               f'Зарплата: {self.salary} грн.'


class SchoolHeadmaster(SchoolWorker):
    def __init__(self, name, last_name, age, city, education,
                 marital_status, work_experience, zone_of_respons, salary):
        super().__init__(name, last_name, age, city, education, marital_status, work_experience, salary)
        self.zone_of_respons = zone_of_respons

    def id_for_school_headmaster(self):
        return f'Ім\'я-прізвище: {self.name} {self.last_name}. Повних років: {self.age}. ' \
               f'Місто: {self.city}. Освіта: {self.education}. Сімейний стан: {self.marital_status}. ' \
               f'Робочий стаж у роках: {self.work_experience}. Зона відповідальності: {self.zone_of_respons}. ' \
               f'Зарплата: {self.salary} грн.'


class Teacher(SchoolWorker):
    def __init__(self, name, last_name, age, city, education,
                 marital_status, work_experience, num_of_class, salary):
        super().__init__(name, last_name, age, city, education, marital_status, work_experience, salary)
        self.num_of_class = num_of_class

    def id_for_school_teacher(self):
        return f'Ім\'я-прізвище: {self.name} {self.last_name}. Повних років: {self.age}. ' \
               f'Місто: {self.city}. Освіта: {self.education}. Сімейний стан: {self.marital_status}. ' \
               f'Робочий стаж у роках: {self.work_experience}. К-ть класів: {self.num_of_class}. ' \
               f'Зарплата: {self.salary} грн.'


class Caretaker(SchoolWorker):
    def __init__(self, name, last_name, age, city, education,
                 marital_status, work_experience, salary, schedule):
        super().__init__(name, last_name, age, city, education, marital_status, work_experience, salary)
        self.schedule = schedule


class Student(Person):
    def __init__(self, name, last_name, age, city, education, marital_status,
                 course, group, scholarship, amount_scholarship):
        super().__init__(name, last_name, age, city, education, marital_status)
        self.course = course
        self.group = group
        self.scholarship = scholarship
        self.amount_scholarship = amount_scholarship

    def id_for_student(self):
        return f'Ім\'я-прізвище: {self.name} {self.last_name}. Повних років: {self.age}. ' \
               f'Місто: {self.city}. Освіта: {self.education}. Сімейний стан: {self.marital_status}. ' \
               f'Курс: {self.course}. Група: {self.group}. ' \
               f'Наявність стипендії: {self.scholarship}. Величина стипендії: {self.amount_scholarship} грн.'

    def scholarship_for_year(self):
        if bool(self.scholarship):
            if str(self.amount_scholarship).isdigit():
                return f'Стипендія за рік — {self.amount_scholarship * 12} грн.'
            else:
                return 'Некоректно введені дані.'
        else:
            return 'Студент не має стипедії.'


principal_1 = SchoolPrincipal('Володимир', 'Кловацький', 50, 'Полтава', 'вища повна', 'одружений', 26, 15, 12500)
print(principal_1.id_for_school_principal())
print(principal_1.salary_for_year())

headmaster_1 = SchoolHeadmaster('Світлана', 'Галябарда', 46, 'Харків', 'вища повна', 'заміжна', 17, 'виховна робота',
                                10500)
print(headmaster_1.id_for_school_headmaster())
print(headmaster_1.salary_for_year())

caretaker_1 = Caretaker('Олена', 'Іваненко', 31, 'Полтава', 'середня спеціалізована',
                        'заміжна', 17, 6500, 'пн-пт, 8:00 - 17:00')
print(caretaker_1.id_for_school_worker())
print(caretaker_1.salary_for_year())

teacher_1 = Teacher('Тетяна', 'Мороз', 26, 'Полтава', 'вища повна', 'незаміжня', 2, 8, 8500)
print(teacher_1.id_for_school_teacher())
print(teacher_1.salary_for_year())

student_1 = Student('Артем', 'Мороз', 17, 'Супрунівка', 'середня повна', 'неодружений', 1, 'Б', True, 1300)
print(student_1.id_for_student())
print(student_1.scholarship_for_year())

student_2 = Student('Валентина', 'Пругло', 18, 'Полтава', 'середня повна', 'незаміжня', 1, 'Б', False, 0)
print(student_2.id_for_student())
print(student_2.scholarship_for_year())
