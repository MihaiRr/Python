class Student(object):
    def __init__(self, studentID, name):
        self.__studentID = studentID
        self.__name = name

    def GetStudentID(self):
        return self.__studentID

    def GetName(self):
        return self.__name

    def SetStudentID(self, newStudentID):
        self.__studentID = newStudentID

    def SetName(self, newName):
        self.__name = newName

    def __eq__(self, newStudent):
        return self.__studentID == newStudent.__studentID

    def __str__(self):
        string = "ID: " + str(self.__studentID) + " , Name: " + self.__name
        return string