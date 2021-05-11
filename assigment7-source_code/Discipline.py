class Discipline(object):
    def __init__(self, disciplineID, name):
        self.__disciplineID = disciplineID
        self.__name = name

    def GetDisciplineID(self):
        return self.__disciplineID

    def GetName(self):
        return self.__name

    def SetName(self, newName):
        self.__name = newName

    def SetDisciplineID(self, newDisciplineID):
        self.__disciplineID = newDisciplineID

    def __eq__(self, newDiscipline):
        return self.__disciplineID == newDiscipline.__disciplineID

    def __str__(self):
        string = "ID: " + str(self.__disciplineID) + " , Name: "+ self.__name
        return string

