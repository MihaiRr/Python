class Grade(object):
    def __init__(self, disciplineID, studentID, gradeValue):
        self.__disciplineID = disciplineID
        self.__studentID = studentID
        self.__gradeValue = gradeValue

    def GetDisciplineID(self):
        return self.__disciplineID


    def GetGradeValue(self):
        return self.__gradeValue

    def SetDisciplineID(self, newDisciplineID):
        self.__disciplineID = newDisciplineID

    def SetStudentID(self, newStudentID):
        self.__studentID = newStudentID

    def SetGradeValue(self, newGradeValue):
        self.__gradeValue = newGradeValue

    def __str__(self):
        return "Student ID: " + self.__studentID + ", Discipline ID: " + self.__disciplineID + ", Grade value: " + str(self.__gradeValue)

