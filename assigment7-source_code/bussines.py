from Discipline import Discipline
from Repository import Repository
from GradeRepository import GradeRepository
from Studeent import Student
from Grade import Grade


class BusinessLayer:
    def __init__(self):
        self.__gradeRepository = GradeRepository()
        self.__studentRepository = Repository()
        self.__disciplineRepository = Repository()
        self.__add_data()

    def __add_data(self):
        student1 = Student("123", "Rusu Raul")
        student2 = Student("456", "Petrica George")
        student3 = Student("1231", "Trif George")
        student4 = Student("1842", "Trif Maria")
        student5 = Student("1255", "Pastarnac Giorgiana")
        student6 = Student("9523", "Almasan Catalin")
        student7 = Student("8234", "Indian Razvan")
        student8 = Student("752234", "Paul Andrei")
        student9 = Student("92424", "Marian Alex")
        discipline1 = Discipline("111", "Math")
        discipline2 = Discipline("222", "FP")
        discipline3 = Discipline("333", "Algebra")
        discipline4 = Discipline("444", "ASC")
        self.__studentRepository.add(student1)
        self.__studentRepository.add(student2)
        self.__studentRepository.add(student3)
        self.__studentRepository.add(student4)
        self.__studentRepository.add(student5)
        self.__studentRepository.add(student6)
        self.__studentRepository.add(student7)
        self.__studentRepository.add(student8)
        self.__studentRepository.add(student9)
        self.__disciplineRepository.add(discipline1)
        self.__disciplineRepository.add(discipline2)
        self.__disciplineRepository.add(discipline4)
        self.__disciplineRepository.add(discipline3)
        grade1 = Grade("111", "123", 9)
        grade2 = Grade("444", "1231", 7)
        grade3 = Grade("333", "9523", 4)
        self.__gradeRepository.add(grade1)
        self.__gradeRepository.add(grade2)
        self.__gradeRepository.add(grade3)


    def AddStudentToRepo(self, studentID, studentName):
        """
        Add a student to studentRepository
        :param studentID:
        :param studentName:
        """
        student = Student(studentID, studentName)
        self.__studentRepository.add(student)

    def AddDisciplineToRepo(self, disciplineID, disciplineName):
        """
        Add a discipline to disciplineRepository
        :param disciplineID:
        :param disciplineName:
        :return:
        """
        discipline = Discipline(disciplineID, disciplineName)
        self.__disciplineRepository.add(discipline)

    def ListAllS(self):
        """
        :return: a string with the format (position) (student)
        """
        position = 0
        string = ""
        listOfStudents = self.__studentRepository.GetAllElements()
        for student in listOfStudents:
            position += 1
            string += str(position) + " " + str(student) + "\n"
        return string

    def ListAllD(self):
        """
        :return: a string with the format (position) (discipline)
        """
        position = 0
        string = ""
        listOfDiscipline = self.__disciplineRepository.GetAllElements()
        for discipline in listOfDiscipline:
            position += 1
            string += str(position) + " " + str(discipline) + "\n"
        return string

    def RemoveS(self, studentID):
        """
        remove a student from studentRepository
        :param studentID:
        """
        studentToRemove = Student(studentID, "")
        self.__studentRepository.Remove(studentToRemove)
        self.__gradeRepository.remove_all_student(studentID)


    def RemoveD(self, disciplineID):
        """
        remove a discipline from studentRepository
        :param disciplineID:
        """
        disciplineToRemove = Discipline(disciplineID, "")
        self.__disciplineRepository.Remove(disciplineToRemove)
        self.__gradeRepository.remove_all_discipline(disciplineID)

    def UpdateS(self, studentID, name):
        """
        update a student in studentRepository
        :param studentID:
        :param name:
        """
        student = self.__studentRepository.FindElementById(studentID)
        newStudent = Student(studentID, name)
        self.__studentRepository.Update(student, newStudent)

    def UpdateD(self, disciplineID, name):
        """
        update a discipline in disciplineRepository
        :param disciplineID:
        :param name:
        """
        discipline = Discipline(disciplineID, "")
        newDiscipline = Discipline(disciplineID, name)
        self.__disciplineRepository.Update(discipline, newDiscipline)

    def GradeStudentAtD(self, studentID, disciplineID, gradeValue):
        """
        add a new grade to gradeRepository
        :param studentID:
        :param disciplineID:
        :param gradeValue:
        """
        gradeValue = int(gradeValue)
        if(gradeValue <= 0 or gradeValue >= 10):
            raise ValueError("grade should be a number between 0 and 10")
        self.__disciplineRepository.FindElement(Discipline(disciplineID, ""))
        self.__studentRepository.FindElement(Student(studentID, "5"))
        grade = Grade(disciplineID, studentID, gradeValue)
        self.__gradeRepository.add(grade)

    def ListAllGrade(self):
        position = 0
        string = ""
        listOfGrades = self.__gradeRepository.get_all_elements()
        for grade in listOfGrades:
            position += 1
            string += str(position) + " " + str(grade) + "\n"
        return string